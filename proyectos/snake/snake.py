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
        if not isinstance(self.__size_tile ,int) or self.__size_tile < 3:
            raise ValueError("Invalid size_tile: must be integer >= 3")
        
        self.__windows_size_x = windows_size_x
        if self.__windows_size_x % self.__size_tile != 0 or self.__windows_size_x // self.__size_tile < 2:
            raise ValueError("Invalid windows_size_x: must be divisible by size_tile and result in more than 2 tiles")
        
        self.__windows_size_y = windows_size_y
        if self.__windows_size_y % self.__size_tile != 0 or self.__windows_size_y // self.__size_tile < 2:
            raise ValueError("Invalid windows_size_y: must be divisible by size_tile and result in more than 2 tiles")
        
        self.__x = x
        if self.__x % self.__size_tile != 0 or self.__x > self.__windows_size_x:
            raise  ValueError("Invalid x: must be divisible by size_tile and <= windows_size_x")
        
        self.__y = y
        if self.__y % self.__size_tile != 0 or self.__y > self.__windows_size_y:
            raise  ValueError("Invalid y: must be divisible by size_tile and <= windows_size_y")
        
        self._list_snake = [(x,y)]
        self.__snake_direction = snake_direction # 0 = top / 1 = right / 2 = bottom / 3 = left
        if self.__snake_direction not in [0,1,2,3]:
            raise ValueError("Invalid direction: must be 0 (up), 1 (right), 2 (down), or 3 (left).")
        self._size_snake = size_snake
        if self._size_snake < 1 or not isinstance(self._size_snake,int):
            raise ValueError("Invalid snake size: must be >= 1 and must be int")
        
        if self._size_snake == 1:pass
        elif self.__snake_direction == 0:
            for i in range(1,self._size_snake):self._list_snake.append((x,y + (self.__size_tile * i)))
            if self._list_snake[-1][1] + self.__size_tile > self.__windows_size_y:raise ValueError("Snake body out of bounds: Y position is greater than window height.")
        elif self.__snake_direction == 1:
            for i in range(1,self._size_snake):self._list_snake.append((x - (self.__size_tile * i),y))
            if self._list_snake[-1][0] < 0:raise ValueError("Snake body out of bounds: X position is less than zero.")
        elif self.__snake_direction == 2:
            for i in range(1,self._size_snake):self._list_snake.append((x,y - (self.__size_tile * i)))
            if self._list_snake[-1][1] < 0:raise ValueError("Snake body out of bounds: Y position is less than zero.")
        elif self.__snake_direction == 3:
            for i in range(1,self._size_snake):self._list_snake.append((x + (self.__size_tile * i),y))
            if self._list_snake[-1][0] + self.__size_tile> self.__windows_size_x :raise ValueError("Snake body out of bounds: X position is greater than window width.")
        
    def Snake_Create_rectangle(self,x,y,w,h,color,window):raise NotImplementedError
    def Timer(self):raise NotImplementedError # the function must return true or false
    def Snake_movement(self,direction_of_movement):# 0 = top / 1 = right / 2 = bottom / 3 = left
        if self.Timer():
            if direction_of_movement not in [0, 1, 2, 3, None]:
                raise ValueError("Invalid direction: must be 0 (up), 1 (right), 2 (down), or 3 (left), or None.")

            if (self.__snake_direction + 2) % 4 == direction_of_movement:
                direction_of_movement = None

            if direction_of_movement is None:
                direction_of_movement = self.__snake_direction

            match direction_of_movement:
                case 0:
                    self.__y -= self.__size_tile
                case 1:
                    self.__x += self.__size_tile
                case 2:
                    self.__y += self.__size_tile
                case 3:
                    self.__x -= self.__size_tile

            if (self.__x < 0 or self.__x >= self.__windows_size_x or
                self.__y < 0 or self.__y >= self.__windows_size_y):
                self._live = False
            else:
                self.__snake_direction = direction_of_movement
                self._list_snake.insert(0, (self.__x, self.__y))

    def Snake_update(self):
        for tuple_positions in self._list_snake[1:]:
            if self._list_snake[0] == tuple_positions:
                self._live = False
                return
        
        while len(self._list_snake) > self._size_snake:
            x ,y = self._list_snake.pop(-1)
            if self.__second_color_BG is None or (((x // self.__size_tile) + (y // self.__size_tile)) % 2 == 0 ):
                self.Snake_Create_rectangle(x,y,self.__size_tile,self.__size_tile,self.__color_BG)
            else:
                self.Snake_Create_rectangle(x,y,self.__size_tile,self.__size_tile,self.__second_color_BG)
            
        for x,y in self._list_snake:
            self.Snake_Create_rectangle(x,y,self.__size_tile,self.__size_tile,self.__color_snake)
            
        x ,y = self._list_snake[0]
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
        for tuple_positions_apple in list_x_y_apple:
            if self._list_snake[0] == tuple_positions_apple:
                self._size_snake += 1
                list_x_y_apple.remove(tuple_positions_apple)
                return