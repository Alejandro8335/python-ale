import B_constantes as constantes
from H_niveles import list_niveles
class Mundo:
    def __init__(self):
        self.map = []
    
    def Process_list(self,list_tiles,nivel,largo_de_filas):
        for posicion , tile in enumerate(list_niveles[nivel]):
            imagen = list_tiles[tile]
            imagen_rect = imagen.get_rect()
            rect_x = (((posicion) % (int(largo_de_filas)))*constantes.TILE_SIZE)
            rect_y = (((posicion) // (int(largo_de_filas)))*constantes.TILE_SIZE)
            imagen_rect.center = (rect_x,rect_y)
            self.map.append([imagen,imagen_rect,rect_x,rect_y])
    
    def Update_mundo(self,list_position_player):
        if self.map:
            for tile in self.map:
                tile[1].move_ip(list_position_player)
    def Dibujar_mapa(self,ventana):
        for i in self.map:
            ventana.blit(i[0],i[1])