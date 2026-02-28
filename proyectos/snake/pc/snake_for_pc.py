from snake.snake import Snake
import pygame

class Snake_for_pc(Snake):
    def __init__(self, x, y, size_tile, size_snake, color_snake, color_eyes, windows_size_x, windows_size_y, move_cooldown, window, snake_direction=0):
        super().__init__(x, y, size_tile, size_snake, color_snake, color_eyes, windows_size_x, windows_size_y, snake_direction)
        self.move_cooldown = move_cooldown
        self.last_move_cooldown = 0
        self.__window = window
    def Snake_Create_rectangle(self, x, y, w, h, color):
        pygame.draw.rect(self.__window, color, (x, y, w, h))
        
    def Timer(self):
        if pygame.time.get_ticks() - self.last_move_cooldown >= self.move_cooldown:
            self.last_move_cooldown = pygame.time.get_ticks()
            return True
        return False