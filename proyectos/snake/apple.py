class Apples:
    def __init__(self,size_tile,color_apples,list_snake,num_tiles_x,num_tiles_y):
        self.list_x_y_apples = []
        self.__list_snake = list_snake
        self.__color_apples = color_apples
        
        self.__size_tile = size_tile
        if not isinstance(self.__size_tile ,int) or self.__size_tile < 3:
            raise ValueError("Invalid size_tile: must be integer >= 3")
        
        self.__num_tiles_x = num_tiles_x
        if not isinstance(self.__num_tiles_x,int):
            raise ValueError("Invalid num_tiles_x: must be a integer")
        self.__num_tiles_y = num_tiles_y
        if not isinstance(self.__num_tiles_y,int):
            raise ValueError("Invalid num_tiles_y: must be a integer")
        
    def Random(self,max_random_value):raise NotImplementedError
    def Apples_draw_pixels(self,x,y,color):raise NotImplementedError
    def Apples_Create(self,tuple_x_and_y):
        self.list_x_y_apples.append((tuple_x_and_y))
        x,y = tuple_x_and_y
        x_center_circle = x + (self.__size_tile / 2) -1
        y_center_circle = y + (self.__size_tile / 2) -1
        radio = (self.__size_tile) / 2 -1
        for y_for in range(y,y + self.__size_tile):
            for x_for in range(x,x + self.__size_tile):
                if (x_for - x_center_circle)**2 + (y_for - y_center_circle)**2 < (radio)**2:
                    self.Apples_draw_pixels(x_for,y_for,self.__color_apples)
    
    def Apples_random(self):
        list_tiles_available = self.__Remove_tiles_that_are_in_use()
        return list_tiles_available[self.Random(len(list_tiles_available))]
    
    def __Remove_tiles_that_are_in_use(self):
        return [(self.__size_tile * x, self.__size_tile * y) for y in range(self.__num_tiles_y) for x in range(self.__num_tiles_x) 
                if (self.__size_tile * x, self.__size_tile * y) not in self.list_x_y_apples and 
                (self.__size_tile * x, self.__size_tile * y) not in self.__list_snake]