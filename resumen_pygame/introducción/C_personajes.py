
import pygame
import B_constantes as constantes
#clases con la primera letra en mayusculas
class Personajes:
   def __init__(self,x,y,animaciones,vida,tipo_personaje):
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
      self.shape =  self.imagen.get_rect()
      # los dos ceros despues se sobre escriven
      self.shape.center = (x,y)
      # monedas
      self.monedas = 0
      self.tipo = tipo_personaje # 1 player / 0 enemigos
   def Update(self):
      # comprobar si el personaje ha muerto
      self.vida = max(0, self.vida)
      self.vivo = (self.vida > 0)
        
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
   
   def Movimiento_enemigos(self,posicion_ventana):
      self.shape.move_ip(posicion_ventana)
   def Movimiento_player(self, delta_x, delta_y):
      if delta_x < 0:
         self.flip = True
      if delta_x > 0:
         self.flip = False      
      self.shape.x += delta_x
      self.shape.y += delta_y
      
      posicon_ventana = [0,0]
      if self.tipo:
         limite_ventana = constantes.LIMITE_VENTANA
         diferencia_ancho_limite = constantes.ANCHO - limite_ventana
         izquierda_player = self.shape.left
         derecha_player = self.shape.right
         if izquierda_player < limite_ventana:
            posicon_ventana[0] = limite_ventana- izquierda_player
            self.shape.left = limite_ventana
         elif derecha_player > diferencia_ancho_limite:
            posicon_ventana[0] = diferencia_ancho_limite- derecha_player
            self.shape.right = diferencia_ancho_limite
         diferencia_alto_limite = constantes.ALTO - limite_ventana
         arriba_player = self.shape.top
         abajo_player = self.shape.bottom
         if arriba_player < limite_ventana:
            posicon_ventana[1] = limite_ventana- arriba_player
            self.shape.top = limite_ventana
         elif abajo_player > diferencia_alto_limite:
            posicon_ventana[1] = diferencia_alto_limite- abajo_player
            self.shape.bottom = diferencia_alto_limite
         return posicon_ventana