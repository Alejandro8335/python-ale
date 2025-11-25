import pygame
import B_constantes as constantes
from H_niveles import list_niveles
from F_items import Item
from C_personajes import Personajes
obstaculos = [1,2,3,5]
pass_level = 4
class Mundo:
    def __init__(self):
        self.map = []
        self.list_obstaculos = []
        self.list_items = []
        self.list_enemigos = []
        self.pass_tile = None
        self.list_tiles_x_izquierda = []
        self.list_tiles_x_derecha = []
        self.list_tiles_y_arriba = []
        self.list_tiles_y_abajo = []
    def Process_list(self,list_tiles,nivel,largo_de_filas,list_frame_items,animacion_enemigos):
        self.imagenes_tiles = list_tiles
        for posicion , tile in enumerate(list_niveles[nivel]):
            posicion_x = (((posicion) % (int(largo_de_filas)))*constantes.TILE_SIZE)
            posicion_y = (((posicion) // (int(largo_de_filas)))*constantes.TILE_SIZE)
            match tile:
                case 6:
                    self.list_items.append(Item(posicion_x,posicion_y,0,list_frame_items[0]))
                    tile = 0 # pq es el piso
                case 7:
                    self.list_items.append(Item(posicion_x,posicion_y,1,list_frame_items[1]))
                    tile = 0
                case 8:
                    self.list_enemigos.append(Personajes(posicion_x,posicion_y,animacion_enemigos[0],constantes.VIDA_ESPINARIA,2,constantes.ANCHO_ENEMIGOS,constantes.ALTO_ENEMIGOS))
                    tile = 0
                case 9:
                    self.list_enemigos.append(Personajes(posicion_x,posicion_y,animacion_enemigos[1],constantes.VIDA_ESPORADOR,3,constantes.ALTO_ENEMIGOS,constantes.ANCHO_ENEMIGOS))
                    tile = 0
            imagen = list_tiles[tile]
            imagen_rect = imagen.get_rect()
            imagen_rect.center = (posicion_x,posicion_y)
            self.map.append([imagen,imagen_rect,posicion_x,posicion_y,tile])
            if tile in obstaculos:
                self.list_obstaculos.append(imagen_rect)
            elif tile == pass_level:
                self.pass_tile = imagen_rect
            limite_ventana = constantes.LIMITE_VENTANA - 50
            if posicion_x <=  limite_ventana:
                self.list_tiles_x_izquierda.append(imagen_rect)
            elif posicion_x >= 1550 - limite_ventana:
                self.list_tiles_x_derecha.append(imagen_rect)
            if posicion_y <= limite_ventana:
                self.list_tiles_y_arriba.append(imagen_rect)
            elif posicion_y >= 1100 - limite_ventana:
                self.list_tiles_y_abajo.append(imagen_rect)
    def Cambiar_puerta(self,player):
        # x → posición horizontal (cuánto se mueve hacia la derecha).
        # y → posición vertical (cuánto se mueve hacia abajo).
        # width → ancho del rectángulo.
        # height → alto del rectángulo.
        # x e y NO son el centro, sino la esquina superior izquierda del rectángulo.
        proximidad_rect = pygame.Rect(player.shape.x - 50,player.shape.y - 50,player.shape.width + 2*50,player.shape.height + 2*50)
        for tile in self.map:
            if proximidad_rect.colliderect(tile[1]):
                if tile[4] == 5:
                    tile[4] = 6
                    tile[0] = self.imagenes_tiles[6]
                    if tile[1] in self.list_obstaculos:
                        self.list_obstaculos.remove(tile[1])
                elif tile[4] == 6:
                    tile[4] = 5
                    tile[0] = self.imagenes_tiles[5]
                    self.list_obstaculos.append(tile[1])
    def Update_mundo(self,list_position_player):
        if self.map:
            for tile in self.map:
                tile[1].move_ip(list_position_player)
    def Dibujar_mapa(self,ventana):
        for i in self.map:
            ventana.blit(i[0],i[1])
    def Reset_world(self,tuple_grupo):
        for i in [self.list_enemigos,self.list_items,self.list_obstaculos,self.map,self.list_tiles_x_derecha,self.list_tiles_x_izquierda,self.list_tiles_y_abajo,self.list_tiles_y_arriba]:
                i.clear()
        for i in tuple_grupo:
            i.empty()
        # es un método que elimina todos los sprites del grupo, pero no los destruye 
        # (los objetos siguen existiendo en memoria si los tenés referenciados en otro lado).