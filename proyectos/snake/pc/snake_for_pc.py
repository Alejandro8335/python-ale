from snake.snake import Snake
import pygame

class Snake_for_pc(Snake):
    def __init__(self, x, y, size_tile, size_snake, color_snake, color_eyes, windows_size_x, windows_size_y, move_cooldown, window, color_BG, snake_direction=0, second_color_BG=None):
        super().__init__(x, y, size_tile, size_snake, color_snake, color_eyes, windows_size_x, windows_size_y, color_BG, snake_direction, second_color_BG)
        self._move_cooldown = move_cooldown
        self._last_move_cooldown = 0
        self.window = window
    def Snake_Create_rectangle(self, x, y, w, h, color):
        pygame.draw.rect(self.window, color, (x, y, w, h))
        
    def Timer(self):
        if pygame.time.get_ticks() - self._last_move_cooldown >= self._move_cooldown:
            self._last_move_cooldown = pygame.time.get_ticks()
            return True
        return False
            