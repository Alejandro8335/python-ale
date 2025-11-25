
import pygame
import B_constantes as constantes
import math
#clases con la primera letra en mayusculas
class Personajes:
   def __init__(self,x,y,animaciones,vida,tipo_personaje,ancho,alto):
      self.animaciones = animaciones
      self.vida = vida
      # imagen de la animacion que se esta mostrando actualmente
      self.frame = 0
      # aqui se almecena la hora actual (en milisegundos desde el inicio de pygame)
      self.update_time =pygame.time.get_ticks()
      self.imagen = animaciones[self.frame]
      # variable para voltiar la imagen del personaje 
      self.flip = False
      # definiendo donde aparece y su forma
      # self.shape = pygame.Rect(0,0,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE)#x/y
      self.shape = pygame.Rect(x, y, ancho, alto)
      # los dos ceros despues se sobre escriven
      self.shape.center = (x,y)
      # monedas
      self.monedas = 0
      self.tipo = tipo_personaje # 1 player / enemigos:2 ESPINARIA Y 3 ESPORADOR
      if self.tipo == 2:
         self.velocidad = constantes.VELOCIDAD_ESPINARIA
         self.rango_vision = constantes.RANGO_VISION_ESPINARIA
         self.golpe = False
         self.ultimo_golpe = pygame.time.get_ticks()
      elif self.tipo == 3:
         self.velocidad = constantes.VELOCIDAD_ESPORADOR
         self.rango_vision = constantes.RANGO_VISION_ESPORADOR
         self.golpe = False
         self.ultimo_golpe = pygame.time.get_ticks()
      elif not self.tipo == 1:
         raise ValueError("Invalid character type")
   def Update(self):
      # comprobar si el personaje ha muerto
      self.vida = max(0, self.vida) # elege el mas grande
      cooldown_animacion = 100
      self.imagen = self.animaciones[self.frame]
      if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
         self.frame = self.frame + 1
         self.update_time = pygame.time.get_ticks()
      if self.frame >= len(self.animaciones):
         self.frame = 0
   def Draw(self,interfaz):
      image_flip = pygame.transform.flip(self.imagen,flip_x = self.flip ,flip_y = False)#invierte los dos ejes
      interfaz.blit(image_flip, self.shape.topleft)#este error es !claricimo!
      #pygame.draw.rect(interfaz, constantes.HITBOX, self.shape, 2)#el prime es el rojo/el segundo el verde/tercero el azul
      #el 2 es para que el rectangulo este vacio
   
   def Movimiento_enemigos(self,posicion_ventana,obstaculos_tiles,player):
      self.shape.move_ip(posicion_ventana)
      plus_X = 0
      plus_Y = 0
      clip_line = None
      distancia = math.hypot(self.shape.centerx - player.shape.centerx,self.shape.centery - player.shape.centery)
      for obs in obstaculos_tiles:
         if obs.clipline(((self.shape.centerx,self.shape.centery),(player.shape.centerx,player.shape.centery))):
            clip_line = True
            break
      if not clip_line and distancia < self.rango_vision: 
         if self.shape.centerx > player.shape.centerx:
            plus_X -= self.velocidad
         elif self.shape.centerx < player.shape.centerx:
            plus_X += self.velocidad
         if self.shape.centery > player.shape.centery:
            plus_Y -= self.velocidad
         elif self.shape.centery < player.shape.centery:
            plus_Y += self.velocidad
            
      if plus_X < 0:
         self.flip = True
      if plus_X > 0:
         self.flip = False
      self.shape.x += plus_X
      for obstaculo in obstaculos_tiles:
         if self.shape.colliderect(obstaculo):
            if plus_X > 0:  # derecha
                  self.shape.right = obstaculo.left
            elif plus_X < 0:  # izquierda
                  self.shape.left = obstaculo.right
      self.shape.y += plus_Y
      for obstaculo in obstaculos_tiles:
         if self.shape.colliderect(obstaculo):
            if plus_Y > 0:  # abajo
                  self.shape.bottom = obstaculo.top
            elif plus_Y < 0:  # arriba
                  self.shape.top = obstaculo.bottom
      if distancia < constantes.RANGO_ATAQUE and constantes.COOLDOWN_ATAQUE_ENEMIGOS < (pygame.time.get_ticks()-self.ultimo_golpe):
         player.vida -= 50
         self.ultimo_golpe = pygame.time.get_ticks()
   def Movimiento_player(self, delta_x, delta_y,obstaculos_tiles,pass_tile,list_tiles_x_izquierda,list_tiles_x_derecha,list_tiles_y_arriba,list_tiles_y_abajo):
      if delta_x < 0:
         self.flip = True
      if delta_x > 0:
         self.flip = False
      self.shape.x += delta_x
      for obstaculo in obstaculos_tiles:
         if self.shape.colliderect(obstaculo):
            if delta_x > 0:  # derecha
                  self.shape.right = obstaculo.left
            elif delta_x < 0:  # izquierda
                  self.shape.left = obstaculo.right
      self.shape.y += delta_y
      for obstaculo in obstaculos_tiles:
         if self.shape.colliderect(obstaculo):
            if delta_y > 0:  # abajo
                  self.shape.bottom = obstaculo.top
            elif delta_y < 0:  # arriba
                  self.shape.top = obstaculo.bottom
      nivel_completado = None
      if self.shape.colliderect(pass_tile):
         nivel_completado = True
      posicon_ventana = [0,0]
      limite_ventana = constantes.LIMITE_VENTANA
      diferencia_ancho_limite = constantes.ANCHO - limite_ventana
      izquierda_player = self.shape.left
      derecha_player = self.shape.right
      colision_tile_x_izquierda = False
      if izquierda_player < limite_ventana:
         for rect_tile in list_tiles_x_izquierda:
            if self.shape.colliderect(rect_tile):
               colision_tile_x_izquierda = True
               break
         if not colision_tile_x_izquierda:
            posicon_ventana[0] = limite_ventana- izquierda_player
            self.shape.left = limite_ventana
      colision_tile_x_derecha = False
      if derecha_player > diferencia_ancho_limite:
         for rect_tile in list_tiles_x_derecha:
            if self.shape.colliderect(rect_tile):
               colision_tile_x_derecha = True
               break
         if not colision_tile_x_derecha:
            posicon_ventana[0] = diferencia_ancho_limite- derecha_player
            self.shape.right = diferencia_ancho_limite
      diferencia_alto_limite = constantes.ALTO - limite_ventana
      arriba_player = self.shape.top
      abajo_player = self.shape.bottom
      colision_tile_y_arriba = False
      if arriba_player < limite_ventana:
         for rect_tile in list_tiles_y_arriba:
             if self.shape.colliderect(rect_tile):
               colision_tile_y_arriba = True
               break
         if not colision_tile_y_arriba:
            posicon_ventana[1] = limite_ventana- arriba_player
            self.shape.top = limite_ventana
      colision_tile_y_abajo = False
      if abajo_player > diferencia_alto_limite:
         for rect_tile in list_tiles_y_abajo:
             if self.shape.colliderect(rect_tile):
               colision_tile_y_abajo = True
               break
         if not colision_tile_y_abajo:
            posicon_ventana[1] = diferencia_alto_limite- abajo_player
            self.shape.bottom = diferencia_alto_limite
      return posicon_ventana,nivel_completado