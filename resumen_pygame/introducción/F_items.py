import pygame.sprite
from B_constantes import VIDA_POCION,VIDA_PERSONAJE

class Item(pygame.sprite.Sprite):
    def __init__(self,x,y,item,animacion_list):
        pygame.sprite.Sprite.__init__(self)
        self.item = item # 0 = monedas / 1 = posiones
        self.animacion = animacion_list
        self.frame = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def update(self,player):
        #comprobar colision entre el personaje y el items
        if self.rect.colliderect(player.shape):#lo que esta adentro parentecis aclara que tiera que ser con el personaje
            #monedas
            if self.item == 0:
                player.monedas += 1
            elif self.item == 1:
                player.vida += VIDA_POCION
                if player.vida >= VIDA_PERSONAJE:
                    self.vida = VIDA_PERSONAJE
                    
            self.kill()
        cooldown_animacion = 150
        self.image = self.animacion[self.frame]
        
        if pygame.time.get_ticks() - self.update_time > cooldown_animacion:
            self.frame += 1
            self.update_time = pygame.time.get_ticks()
            self.frame = (self.frame + 1) % len(self.animacion)
            #pygame.time.get_ticks:almacena un valor(no cuenta),
            #en el caso del self.update_time guarda el valor de cuando se creo el objeto(en microsegundos) y 
            #en el caso del if ese valor se actualiza todo el tiempo
        