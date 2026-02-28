from snake.apple import Apples
import pygame
import random

class Apples_for_pc(Apples):
    def __init__(self, size_tile, color_apples, list_snake, num_tiles_x, num_tiles_y,window, apples_create_cooldown):
        super().__init__(size_tile, color_apples, list_snake, num_tiles_x, num_tiles_y)
        self.__window = window
        self.last_Apples_Create_cooldown = 0
        self.apples_create_cooldown = apples_create_cooldown
    def Apples_draw_pixels(self, x, y, color):
        pygame.draw.rect(self.__window, color, (x, y, 1, 1))
        
    def Random(self, max_random_value):
        return random.randint(0, max_random_value - 1)
    
    def Timer(self):
        if pygame.time.get_ticks() - self.last_Apples_Create_cooldown >= self.apples_create_cooldown:
            self.last_Apples_Create_cooldown = pygame.time.get_ticks()
            return True
        return False