from snake.pc.main_snake_for_pc import Draw_background, Handle_start_events, game_run,Update_game
from unittest.mock import patch,Mock
from snake.pc.apple_for_pc import Apples_for_pc as Apples
from snake.pc.snake_for_pc import Snake_for_pc as Snake

@patch("snake.pc.main_snake_for_pc.pygame.draw.rect")
def test_Draw_background(mock_rect):
    # Arrange: set up constants
    num_tile = 2
    tile_size = 10

    window = "windows"
    color_0 = (255, 255, 255)
    color_1 = (0, 0, 0)

    # Act
    Draw_background(window, color_0, color_1,num_tile,tile_size)

    # Assert: rect should be called NUM_TILE * NUM_TILE times
    assert mock_rect.call_count == num_tile ** 2

    # Recorremos todas las llamadas y comprobamos ventana, color y rect
    for idx, call in enumerate(mock_rect.call_args_list):
        args, kwargs = call
        # args[0] -> window
        assert args[0] == window

        # calcular x,y según el orden del bucle: for y in ...: for x in ...:
        y = idx // num_tile
        x = idx % num_tile

        # color esperado según paridad de x+y
        expected_color = color_0 if (x + y) % 2 == 0 else color_1
        assert args[1] == expected_color

        # rect esperado: (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        expected_rect = (x * tile_size,
                         y * tile_size,
                         tile_size,
                         tile_size)
        assert args[2] == expected_rect

def test_Update_game_if__live_is_False():
    snake_size_to_win = 40
    
    mock_snake = Mock()
    mock_snake._live = False
    mock_snake._size_snake = 13
    
    mock_apples = Mock()
    
    mock_font_score = Mock()
    mock_font_score.render.return_value = "text_score"
    
    mock_window = Mock()
    
    Update_game(mock_window,mock_snake,mock_apples,3,mock_font_score,snake_size_to_win,None,None,None,(10,10,10),None,None)
    
    mock_snake.Snake_movement.assert_called_once_with(3)
    mock_snake.Snake_check_Collision.assert_called_once_with()
    
    mock_apples.assert_not_called() # it is a flag for know if the Update_game enter the if
    
    mock_font_score.render.assert_called_once_with(f"snake size: {13} / {snake_size_to_win}", True, (10,10,10))
    mock_window.blit("text_score", (10, 5))


@patch("snake.pc.main_snake_for_pc.Draw_background")
def test_Update_game_if__live_is_true(Draw_background):
    snake_size_to_win = 40
    
    BLUE        = (0, 0, 255)
    LIGHT_GREEN = (144, 238, 144)
    DARK_GREEN  = (0, 128, 0)
    YELLOW =   (200, 170, 0)
    
    TILE_SIZE = 40
    NUM_TILE = 12
    
    mock_snake = Mock()
    mock_snake._live = True
    mock_snake._size_snake = 13
    
    mock_apples = Mock()
    
    mock_font_score = Mock()
    mock_font_score.render.return_value = "text_score"
    
    mock_window = Mock()
    
    Update_game(mock_window,mock_snake,mock_apples,3,mock_font_score,snake_size_to_win,BLUE,LIGHT_GREEN,DARK_GREEN,YELLOW,NUM_TILE,TILE_SIZE)
    
    mock_snake.Snake_movement.assert_called_once_with(3)
    mock_snake.Snake_check_Collision.assert_called_once_with()
    
    mock_window.fill.assert_called_once_with((0, 0, 255))
    Draw_background.assert_called_once_with(mock_window, LIGHT_GREEN, DARK_GREEN, NUM_TILE, TILE_SIZE)
    
    mock_snake.Snake_eat_apple.assert_called_once_with(mock_apples.list_x_y_apples)
    mock_snake.Snake_update_body.assert_called_once_with()
    mock_snake.Snake_update_eyes.assert_called_once_with()
    
    mock_apples.Apples_Create.assert_called_once_with()            
    mock_apples.Apples_update.assert_called_once_with()
    
    mock_font_score.render.assert_called_once_with(f"snake size: {13} / {snake_size_to_win}", True, YELLOW)
    mock_window.blit("text_score", (10, 5))
      
@patch("snake.pc.main_snake_for_pc.pygame") 
def test_Handle_start_events(mock_pygame):
    mock_pygame.QUIT = 1
    mock_pygame.KEYDOWN = 2
    mock_pygame.K_ESCAPE = 3
    
    mock_event = Mock()
    mock_event.type = mock_pygame.QUIT
    
    mock_pygame.event.get.return_value = [mock_event]
    assert Handle_start_events() is False
    
    mock_event.type = mock_pygame.KEYDOWN
    mock_event.key = mock_pygame.K_ESCAPE
    
    mock_pygame.event.get.return_value = [mock_event]
    assert Handle_start_events() is True

@patch("snake.pc.main_snake_for_pc.Handle_start_events")
@patch("snake.pc.main_snake_for_pc.pygame")
def test_game_run_if_Handle_start_events_return_false(mock_pygame,mock_Handle_start_events):
    mock_Handle_start_events.return_value = False
    
    game_run(None,100,None,None)
    
    mock_pygame.quit.assert_called_once()

@patch("snake.pc.main_snake_for_pc.Apples")
@patch("snake.pc.main_snake_for_pc.Snake")
@patch("snake.pc.main_snake_for_pc.Update_game")
@patch("snake.pc.main_snake_for_pc.Handle_start_events")
@patch("snake.pc.main_snake_for_pc.pygame")
def test_game_run_event_type_QUIT(mock_pygame,mock_Handle_start_events,mock_Update_game,mock_Snake,mock_Apples):
    mock_Handle_start_events.return_value = True
    
    mock_event = Mock()
    
    mock_snake_instance = mock_Snake.return_value
    mock_snake_instance._size_snake = 1
    
    mock_pygame.QUIT = 1
    mock_event.type = mock_pygame.QUIT
    
    mock_pygame.event.get.return_value = [mock_event]
    
    game_run(None,100,None,None)
    
    mock_pygame.quit.assert_called_once()
    
    mock_Update_game.assert_called_once_with(
    None,
    mock_Snake.return_value,
    mock_Apples.return_value,
    None,
    None,
    100,
    (0, 0, 255), 
    (144, 238, 144), 
    (0, 128, 0), 
    (200, 170, 0), 
    12, 
    40
)

@patch("snake.pc.main_snake_for_pc.Snake")
@patch("snake.pc.main_snake_for_pc.constants.WINDOW_SIZE", 480)
@patch("snake.pc.main_snake_for_pc.Update_game")
@patch("snake.pc.main_snake_for_pc.Handle_start_events")
@patch("snake.pc.main_snake_for_pc.pygame")
def test_game_run_win(mock_pygame,mock_Handle_start_events,mock_Update_game,mock_Snake):
    mock_window = Mock()
    mock_text_win = Mock()
    mock_text_win.return_value = 10
    
    mock_text_win_get_width = 10
    mock_text_win.get_width.return_value = mock_text_win_get_width
    
    mock_text_win_get_height = 10
    mock_text_win.get_height.return_value = mock_text_win_get_height
    
    mock_Handle_start_events.return_value = True
    
    mock_event = Mock()
    
    mock_pygame.QUIT = 1
    mock_event.type = mock_pygame.QUIT
    
    mock_pygame.event.get.return_value = [mock_event]
    
    snake_size_to_win = 40
    mock_snake_instance = mock_Snake.return_value
    mock_snake_instance._size_snake = snake_size_to_win
    
    game_run(mock_window,snake_size_to_win,mock_text_win,None)
    
    mock_pygame.quit.assert_called_once()
    
    mock_window.blit.assert_called_once_with(mock_text_win, (((480 - mock_text_win_get_width) // 2), ((480 - mock_text_win_get_height) // 2)))
    
    mock_text_win.get_width.assert_called_once_with()
    mock_text_win.get_height.assert_called_once_with()