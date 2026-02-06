import pygame
from snake.pc.snake_for_pc import Snake_for_pc as Snake
from snake.pc.apple_for_pc import Apples_for_pc as Apples
import snake.pc.constants_snake_for_pc as constants

# cd C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos
# python -m snake.pc.main_snake_for_pc


pygame.init()
window = pygame.display.set_mode((constants.WINDOW_SIZE,constants.WINDOW_SIZE))
pygame.display.set_caption("Snake for pc")

window.fill(constants.COLOR_BG)

def Draw_background(window,color_0,color_1):
    for y in range(constants.NUM_TILE):
        for x in range(constants.NUM_TILE):
            if (x + y) % 2 == 0:
                pygame.draw.rect(window, color_0, ((x * constants.TILE_SIZE), (y * constants.TILE_SIZE), constants.TILE_SIZE, constants.TILE_SIZE))
            else:
                pygame.draw.rect(window, color_1, ((x * constants.TILE_SIZE), (y * constants.TILE_SIZE), constants.TILE_SIZE, constants.TILE_SIZE))
running = True
direction_movement = None
btn_reset = False
Draw_background(window,constants.LIGHT_GREEN,constants.DARK_GREEN)

snake = None

clock = pygame.time.Clock()
while running:
    clock.tick(constants.FPS)
    if btn_reset and snake._live:
        for event in pygame.event.get():
            event_type = event.type
            if event_type == pygame.QUIT:
                running = False
            elif event_type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction_movement = 0
                if event.key == pygame.K_d:
                    direction_movement = 1
                if event.key == pygame.K_s:
                    direction_movement = 2
                if event.key == pygame.K_a:
                    direction_movement = 3

        snake.Snake_movement(direction_movement)
        snake.Snake_update()
        snake.Snake_eat_apple(apples.list_x_y_apples)
        
        if pygame.time.get_ticks() - last_Apples_Create_cooldown >= constants.APPLES_CREATE_COOLDOWN:
            last_Apples_Create_cooldown = pygame.time.get_ticks()
            apples.Apples_Create(apples.Apples_random())
    else:
        if snake is None or not snake._live:
            direction_movement = None
            btn_reset = False
            snake = Snake(320,240,constants.TILE_SIZE,3,constants.BLUE,constants.BLACK,constants.WINDOW_SIZE,constants.WINDOW_SIZE,constants.MOVE_COOLDOWN,window,constants.LIGHT_GREEN,3,constants.DARK_GREEN)
            apples = Apples(constants.TILE_SIZE,constants.RED,snake._list_snake,constants.NUM_TILE,constants.NUM_TILE,window)
            last_Apples_Create_cooldown = 0
            
        for event in pygame.event.get():
            event_type = event.type
            if event_type == pygame.QUIT:
                running = False
            elif event_type == pygame.KEYDOWN:
                if event.key ==  pygame.K_ESCAPE:
                    Draw_background(window,constants.LIGHT_GREEN,constants.DARK_GREEN)
                    btn_reset = True
    pygame.display.update()
pygame.quit()