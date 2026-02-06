from snake.apple import Apples
import pygame
import random

class Apples_for_pc(Apples):
    def __init__(self, size_tile, color_apples, list_snake, num_tiles_x, num_tiles_y,window):
        super().__init__(size_tile, color_apples, list_snake, num_tiles_x, num_tiles_y)
        self.window = window
        
    def Apples_draw_pixels(self, x, y, color):
        pygame.draw.rect(self.window, color, (x, y, 1, 1))
        
    def Random(self, max_random_value):
        return random.randint(0, max_random_value - 1)