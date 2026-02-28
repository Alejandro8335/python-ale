import pygame
from snake.pc.snake_for_pc import Snake_for_pc as Snake
from snake.pc.apple_for_pc import Apples_for_pc as Apples
import snake.pc.constants_snake_for_pc as constants

# python -m snake.pc.main_snake_for_pc


pygame.init()
window = pygame.display.set_mode((constants.WINDOW_SIZE,constants.WINDOW_SIZE))
snake_size_to_win = (constants.WINDOW_SIZE // constants.TILE_SIZE) ** 2 # if it gives float, The error will be thrown in the __init__ of snake
pygame.display.set_caption("Snake for pc")

font_score = pygame.font.Font(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\programacion\\python-ALE\\proyectos\\snake\\pc\\fuente.ttf", 22)
font_win = pygame.font.Font(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\programacion\\python-ALE\\proyectos\\snake\\pc\\fuente.ttf", 75)
text_win = font_win.render("you won", True, constants.YELLOW)

def Draw_background(window,color_0,color_1,num_tile,tile_size):
    for y in range(num_tile):
        for x in range(num_tile):
            if (x + y) % 2 == 0:
                pygame.draw.rect(window, color_0, ((x * tile_size), (y * tile_size), tile_size, tile_size))
            else:
                pygame.draw.rect(window, color_1, ((x * tile_size), (y * tile_size), tile_size, tile_size))
                
window.fill(constants.BLUE)
Draw_background(window,constants.LIGHT_GREEN,constants.DARK_GREEN,constants.NUM_TILE,constants.TILE_SIZE)
pygame.display.update()
clock = pygame.time.Clock()

def Update_game(window,snake,apples,direction_movement,font_score,snake_size_to_win,blue,light_green,dark_green,yellow,num_tile,tile_size):
    snake.Snake_movement(direction_movement)
    snake.Snake_check_Collision()
    if snake._live:
        window.fill(blue)
        Draw_background(window,light_green,dark_green,num_tile,tile_size)
                    
        snake.Snake_eat_apple(apples.list_x_y_apples)
        snake.Snake_update_body()
        snake.Snake_update_eyes()
                    
        apples.Apples_Create()            
        apples.Apples_update()

    text_score = font_score.render(f"snake size: {snake._size_snake} / {snake_size_to_win}", True, yellow)
    window.blit(text_score, (10, 5))
                
def Handle_start_events():
    running = True
    running_first_while = True
    while running and running_first_while:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

def game_run(window,snake_size_to_win,text_win,font_score):
    running = Handle_start_events()

    while running:
        game_reset = True
        direction_movement = None
        snake = Snake(320, 240, constants.TILE_SIZE, constants.INITIAL_SIZE_SNAKE, constants.BLUE, constants.BLACK, constants.WINDOW_SIZE, constants.WINDOW_SIZE, constants.MOVE_COOLDOWN, window, 3)
        apples = Apples(constants.TILE_SIZE, constants.RED, snake._list_snake, constants.NUM_TILE, constants.NUM_TILE, window, constants.APPLES_CREATE_COOLDOWN)
        while game_reset:
            clock.tick(constants.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_reset = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_reset = False
                    if event.key == pygame.K_w:
                        direction_movement = 0
                    elif event.key == pygame.K_d:
                        direction_movement = 1
                    elif event.key == pygame.K_s:
                        direction_movement = 2
                    elif event.key == pygame.K_a:
                        direction_movement = 3
            
            if snake_size_to_win <= snake._size_snake:
                window.blit(text_win, (((constants.WINDOW_SIZE - text_win.get_width()) // 2), ((constants.WINDOW_SIZE - text_win.get_height()) // 2)))
                
            elif snake._live:
                Update_game(window,snake,apples,direction_movement,font_score,snake_size_to_win,constants.BLUE,
                            constants.LIGHT_GREEN,constants.DARK_GREEN,constants.YELLOW,constants.NUM_TILE,constants.TILE_SIZE)
                
            pygame.display.update()
    pygame.quit()
    
if __name__ == "__main__":
    game_run(window,snake_size_to_win,text_win,font_score)