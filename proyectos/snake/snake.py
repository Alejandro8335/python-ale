# minimo tiene que ser un 3x3 el tile 
class Snake:
    def __init__(self,x,y,size_tile,size_snake,color_snake,color_eyes,windows_size_x,windows_size_y,color_BG,snake_direction = 0,second_color_BG = None):
        self._live = True
        self.__color_BG = color_BG
        self.__second_color_BG = second_color_BG
        self.__color_snake = color_snake
        self.__color_eyes = color_eyes
        self.__size_eyes = size_tile // 3
        self.__eyes_distance = size_tile - self.__size_eyes * 2
        
        self.__size_tile = size_tile
        if isinstance(self.__size_tile ,float) or self.__size_tile < 3:
            raise ValueError("Invalid size_tile: must be integer >= 3")
        
        self.__windows_size_x = windows_size_x
        if self.__windows_size_x % self.__size_tile != 0 and self.__windows_size_x // self.__size_tile > 2:
            raise ValueError("Invalid windows_size_x: must be divisible by size_tile and result in more than 2 tiles")
        
        self.__windows_size_y = windows_size_y
        if self.__windows_size_y % self.__size_tile != 0 and self.__windows_size_y // self.__size_tile > 2:
            raise ValueError("Invalid windows_size_y: must be divisible by size_tile and result in more than 2 tiles")
        
        self.__x = x
        if self.__x % self.__size_tile != 0 or self.__x > self.__windows_size_x:
            raise  ValueError("Invalid x: must be divisible by size_eyes and <= windows_size_x")
        
        self.__y = y
        if self.__y % self.__size_tile != 0 or self.__y > self.__windows_size_y:
            raise  ValueError("Invalid y: must be divisible by size_eyes and <= windows_size_y")
        
        self.__list_snake = [(x,y)]
        self.__snake_direction = snake_direction # 0 = top / 1 = right / 2 = bottom / 3 = left
        self._size_snake = size_snake
        if self._size_snake < 1:
            raise ValueError("Invalid snake size: must be >= 1")
        if snake_direction == 0:
            for i in range(1,self._size_snake-1):self.__list_snake.append((x,y + (self._size_snake*i)))
            if self.__list_snake[-1][1] > self.__windows_size_y:raise ValueError("Snake body out of bounds: Y position is greater than window height.")
        elif snake_direction == 1:
            for i in range(1,self._size_snake-1):self.__list_snake.append((x - (self._size_snake*i),y))
            if self.__list_snake[-1][0] < 0:raise ValueError("Snake body out of bounds: X position is less than zero.")
        elif snake_direction == 2:
            for i in range(1,self._size_snake-1):self.__list_snake.append((x,y - (self._size_snake*i)))
            if self.__list_snake[-1][1] < 0:raise ValueError("Snake body out of bounds: Y position is less than zero.")
        elif snake_direction == 3:
            for i in range(1,self._size_snake-1):self.__list_snake.append((x + (self._size_snake*i),y))
            if self.__list_snake[-1][0] > self.__windows_size_x:raise ValueError("Snake body out of bounds: X position is greater than window width.")
        else:
            raise ValueError("Invalid snake_direction: must be 0 (top), 1 (right), 2 (bottom), or 3 (left)")
        
    def Snake_Create_rectangle(self,x,y,w,h,color):raise NotImplementedError
    def Timer():raise NotImplementedError # the function must return true or false
    def Snake_movement(self,direction_of_movement):# 0 = top / 1 = right / 2 = bottom / 3 = left
        if self.Timer():
            match direction_of_movement:
                case None:
                    match self.__snake_direction:
                        case 0:
                            self.__y -= self.__size_tile
                            if self.__y < 0:
                                self.live = False
                            self.__snake_direction = 0
                            self.__list_snake.insert(0,(self.__x,self.__y))
                        case 1:
                            self.__x += self.__size_tile
                            if self.__x > self.__windows_size_x:
                                self.live = False
                            self.__snake_direction = 1
                            self.__list_snake.insert(0,(self.__x,self.__y))
                        case 2:
                            self.__y += self.__size_tile
                            if self.__y > self.__windows_size_y:
                                self.live = False
                            self.__snake_direction = 2
                            self.__list_snake.insert(0,(self.__x,self.__y))
                        case 3:
                            self.__x -= self.__size_tile
                            if self.__x < 0:
                                self.live = False
                            self.__snake_direction = 3
                            self.__list_snake.insert(0,(self.__x,self.__y))
                case 0:
                    self.__y -= self.__size_tile
                    if self.__y < 0:
                        self.live = False
                    self.__snake_direction = 0
                    self.__list_snake.insert(0,(self.__x,self.__y))
                case 1:
                    self.__x += self.__size_tile
                    if self.__x > self.__windows_size_x:
                        self.live = False
                    self.__snake_direction = 1
                    self.__list_snake.insert(0,(self.__x,self.__y))
                case 2:
                    self.__y += self.__size_tile
                    if self.__y > self.__windows_size_y:
                        self.live = False
                    self.__snake_direction = 2
                    self.__list_snake.insert(0,(self.__x,self.__y))
                case 3:
                    self.__x -= self.__size_tile
                    if self.__x < 0:
                        self.live = False
                    self.__snake_direction = 3
                    self.__list_snake.insert(0,(self.__x,self.__y))
    def Snake_update(self):
        while self.__list_snake > self.size_snake:
            x ,y = self.__list_snake.pop(-1)
            if self.__second_color_BG is None or ((x // self.__size_tile) % 2 == 0 and (y // self.__size_tile) % 2 == 0):
                self.Snake_Create_rectangle(x,y,self.__size_tile,self.__size_tile,self.__color_BG)
            else:
                self.Snake_Create_rectangle(x,y,self.__size_tile,self.__size_tile,self.__second_color_BG)
        x ,y = self.__x ,self.__y
        xx = x + self.__size_tile ; yy = y + self.__size_tile
        set_positions = {(x,y),(xx,y),(xx,yy),(x,yy)}
        for i in range(1,len(self.__list_snake)):
            x_check ,y_check = self.__list_snake[i]
            xx_check = x_check + self.__size_tile;yy_check = y_check + self.__size_tile
            set_positions_check = {(x_check,y_check),(xx_check,y_check),(xx_check,yy_check),(x_check,yy_check)}
            if any(pos in set_positions for pos in set_positions_check):
                self.live = False
                break
        for x,y in self.__list_snake:
            self.Snake_Create_rectangle(x,y,self.__size_tile,self.__size_tile,self.__color_snake)
            
        x ,y = self.__list_snake[0]
        match self.__snake_direction:
            case 0:
                self.Snake_Create_rectangle(x,y,self.__size_eyes,self.__size_eyes,self.__color_eyes)
                self.Snake_Create_rectangle((x + self.__size_eyes + self.__eyes_distance), y ,self.__size_eyes,self.__size_eyes,self.__color_eyes)
            case 1:
                self.Snake_Create_rectangle((x + self.__size_eyes + self.__eyes_distance), y ,self.__size_eyes,self.__size_eyes,self.__color_eyes)
                self.Snake_Create_rectangle((x + self.__size_eyes + self.__eyes_distance),(y + self.__size_eyes + self.__eyes_distance),self.__size_eyes,self.__size_eyes,self.__color_eyes)
            case 2:
                self.Snake_Create_rectangle((x + self.__size_eyes + self.__eyes_distance),(y + self.__size_eyes + self.__eyes_distance),self.__size_eyes,self.__size_eyes,self.__color_eyes)
                self.Snake_Create_rectangle(x,(y + self.__size_eyes + self.__eyes_distance),self.__size_eyes,self.__size_eyes,self.__color_eyes)
            case 3:
                self.Snake_Create_rectangle(x,y,self.__size_eyes,self.__size_eyes,self.__color_eyes)
                self.Snake_Create_rectangle(x,(y + self.__size_eyes + self.__eyes_distance),self.__size_eyes,self.__size_eyes,self.__color_eyes)
    def Snake_eat_apple(self,list_x_y_apple):
        x ,y = self.__x ,self.__y
        xx = x + self.__size_tile ; yy = y + self.__size_tile
        set_positions = {(x,y),(xx,y),(xx,yy),(x,yy)}
        for x_apple,y_apple in list_x_y_apple:
            xx_apple = x_apple + self.__size_tile;yy_apple = y_apple + self.__size_tile
            set_positions_apple = {(x_apple,y_apple),(xx_apple,y_apple),(xx_apple,yy_apple),(x_apple,yy_apple)}
            if any(pos in set_positions for pos in set_positions_apple):
                self.size_snake += 1