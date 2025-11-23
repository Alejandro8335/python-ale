
import pygame
import B_constantes as constantes
import math
import random
class Weapon():
    def __init__(self,imagen,imagen_b):
        self.imagen_P = imagen
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_P,-self.angulo)
        self.shape = self.imagen.get_rect()
        self.imagen_b = imagen_b
        self.disparar = False
        self.ult_disparo = pygame.time.get_ticks()
        
    def update(self, player):
        #conecto los centros
        self.shape.center = player.shape.center
        #muevo el arma
        if player.flip:
            self.shape.midright = (player.shape.left + player.shape.width // 2, player.shape.centery)
        else:
            self.shape.midleft = (player.shape.right - player.shape.width // 2, player.shape.centery)
      
        #mover la weapon con el mouse
        mouse_posicion = pygame.mouse.get_pos()
        distancia_x = mouse_posicion[0] - self.shape.centerx
        distancia_y = mouse_posicion[1] - self.shape.centery
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))
        self.Flip()
        #print(self.angulo)
        
        #detectar los click del mouse
        bala = None
        if pygame.mouse.get_pressed()[0] and not self.disparar and (pygame.time.get_ticks()-self.ult_disparo) >= constantes.COOLDOWN_ARMA:#0 boton izquierdo /1 rueda /2 boton derecho
            bala = Bullet(self.imagen_b,self.shape.centerx,self.shape.centery,self.angulo)
            self.disparar = True
            self.ult_disparo = pygame.time.get_ticks()#esto almacena el milisegundos del ultimo disparo,no se reinicia
        #resetear el click del mause
        if not pygame.mouse.get_pressed()[0]:
                self.disparar = False
        return bala
        
    def Flip(self):
        self.imagen = pygame.transform.rotate(self.imagen_P, -self.angulo)
        self.shape = self.imagen.get_rect(center=self.shape.center)
    def draw(self, interfaz):
        interfaz.blit(self.imagen, self.shape)
        #pygame.draw.rect(interfaz, constantes.HITBOX_A, self.shape, 2)
        
    
class  Bullet(pygame.sprite.Sprite):
    def __init__(self, imagen,x,y,angulo):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_o = imagen
        self.angulo = angulo
        self.image = pygame.transform.rotate(self.imagen_o, -self.angulo)#angulo 0 para que no rote
        self.rect = self.image.get_rect(center=(x, y))
        self.rect_center = (x,y)
        #calculando la velosidad de la bala
        self.delta_x = math.cos(math.radians(self.angulo))*constantes.VELOCIDAD_BALA
        self.delta_y = math.sin(math.radians(self.angulo))*constantes.VELOCIDAD_BALA
    def update_b(self,lista_enemigo,list_obstaculos):
        dano = 0
        posicion_dano = None
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y
        
        #sacar las balas que salen de la pantalla
        if self.rect.right < 0 or self.rect.left > constantes.ANCHO or self.rect.bottom < 0 or self.rect.top > constantes.ALTO:
            #derecha < 0 / izquierda > ancho / abajo < 0 / arriba > alto (del cuadrado)
            #izquierda / derecha / arriba / abajo 
            self.kill()
        #verificar si hay colision con enemigos
        for enemigo in lista_enemigo:
            if enemigo.shape.colliderect(self.rect):
                dano = constantes.DANO_BALA + random.randint(-25,25)
                enemigo.vida -= dano
                posicion_dano = enemigo.shape
                self.kill()
                break
        for obs in list_obstaculos:
            if obs.colliderect(self.rect):
                self.kill()
                break
        return dano , posicion_dano
    def Draw_b(self,interfaz):
        interfaz.blit(self.image, self.rect.topleft)
        #pygame.draw.rect(interfaz, constantes.HITBOX_B, self.rect, 2)

