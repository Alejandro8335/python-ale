
import pygame
import B_constantes as constantes
#clases con la primera letra en mayusculas
class Personajes:
     def __init__(self,x,y,animaciones,vida):
        self.animaciones = animaciones
        self.vida = vida
        #imagen de la animacion que se esta mostrando actualmente
        self.frame = 0
        #aqui se almecena la hora actual (en milisegundos desde el inicio de pygame)
        self.update_time =pygame.time.get_ticks()
        self.imagen = animaciones[self.frame]
        #variable para voltiar la imagen del personaje 
        self.flip = False
        #definiendo donde aparece y su forma
        #self.shape = pygame.Rect(0,0,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE)#x/y
        self.shape =  self.imagen.get_rect()
        #los dos ceros despues se sobre escriven
        self.shape.center = (x,y)
        #monedas
        self.monedas = 0
     def update(self):
        #comprobar si el personaje ha muerto
        self.vida = max(0, self.vida)
        self.vivo = (self.vida > 0)
        
        cooldown_animacion = 100
        self.imagen = self.animaciones[self.frame]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame = self.frame + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame >= len(self.animaciones):
            self.frame = 0
            
     def draw(self,interfaz):
      image_flip = pygame.transform.flip(self.imagen,flip_x = self.flip ,flip_y = False)#invierte los dos ejes
      interfaz.blit(image_flip, self.shape.topleft)#este error es !claricimo!
      #pygame.draw.rect(interfaz, constantes.HITBOX, self.shape, 2)#el prime es el rojo/el segundo el verde/tercero el azul
      #el 2 es para que el rectangulo este vacio
      
     def movimiento(self, delta_x, delta_y):
         if delta_x < 0:
            self.flip = True
         if delta_x > 0:
            self.flip = False      
         self.shape.x += delta_x
         self.shape.y += delta_y