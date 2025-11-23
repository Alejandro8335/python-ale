import pygame.sprite

class Damage_text(pygame.sprite.Sprite):#ya tiene sus funciones (update,draw)
    def __init__(self,x,y,damage,font,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, color)
        self.rect =  self.image.get_rect()
        self.rect.center = (x,y)
        self.contador = 0
        
    def update(self,posicion_ventana):
        self.rect.move_ip(posicion_ventana)
        self.rect.y -= 3
        self.contador += 1
        if self.contador > 50:
            self.kill()