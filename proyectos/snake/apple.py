class Apples:
    def __init__(self,number_of_tiles,size_tile,color_apples):
        self.list_x_y_apples = []
        self.__color_apples = color_apples
        self.number_of_tiles = number_of_tiles
        if not isinstance(self.number_of_tiles,int):raise ValueError("number_of_tiles is not int")
        self.__size_tile = size_tile
        if isinstance(self.__size_tile ,float) or self.__size_tile < 3:
            raise ValueError("Invalid size_tile: must be integer >= 3")
    def Apples_random(number_of_tiles):raise NotImplementedError
    def Apples_draw_pixels(self,x,y,color):raise NotImplementedError
    def Apples_Create(self,x,y):
        self.list_x_y_apples.append((x,y))
        x_center_circle = x + (self.__size_tile - 1) / 2
        y_center_circle = y + (self.__size_tile - 1) / 2
        radio = (self.__size_tile) / 2 -1
        for y_for in range(y,y + self.__size_tile):
            for x_for in range(x,x + self.__size_tile):
                if (x_for - x_center_circle)**2 + (y_for - y_center_circle)**2 < (radio)**2:
                    self.Apples_draw_pixels(x_for,y_for,self.__color_apples)