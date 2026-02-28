from snake.snake import Snake
import pytest
import re 
from unittest.mock import Mock
from unittest.mock import call
# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\programacion\python-ale\proyectos\snake\test_snake.py"

def test__init__():
    # size_tile
    with pytest.raises(ValueError,match = "Invalid size_tile: must be integer >= 3"):
        snake = Snake(None,None,3.5,None,None,None,None,None)
    with pytest.raises(ValueError,match = "Invalid size_tile: must be integer >= 3"):
        snake = Snake(None,None,1,None,None,None,None,None)
        
    # windows_size_x
    with pytest.raises(ValueError,match = "Invalid windows_size_x: must be divisible by size_tile and result in more than 2 tiles"):
        snake = Snake(None,None,3,None,None,None,4,None)
    with pytest.raises(ValueError,match = "Invalid windows_size_x: must be divisible by size_tile and result in more than 2 tiles"):
        snake = Snake(None,None,3,None,None,None,3,None)
        
    # windows_size_y
    with pytest.raises(ValueError, match = "Invalid windows_size_y: must be divisible by size_tile and result in more than 2 tiles"):
        snake = Snake(None,None,3,None,None,None,6,4)
    with pytest.raises(ValueError, match = "Invalid windows_size_y: must be divisible by size_tile and result in more than 2 tiles"):
        snake = Snake(None,None,3,None,None,None,6,3)
        
    # x
    with pytest.raises(ValueError, match = "Invalid x: must be divisible by size_tile and <= windows_size_x"):
        snake = Snake(1,None,3,None,None,None,6,6)
    with pytest.raises(ValueError, match = "Invalid x: must be divisible by size_tile and <= windows_size_x"):
        snake = Snake(9,None,3,None,None,None,6,6)
    
    # y
    with pytest.raises(ValueError, match = "Invalid y: must be divisible by size_tile and <= windows_size_y"):
        snake = Snake(3,1,3,None,None,None,6,6)
    with pytest.raises(ValueError, match = "Invalid y: must be divisible by size_tile and <= windows_size_y"):
        snake = Snake(3,9,3,None,None,None,6,6)
    
    # snake_direction not in [1,2,3,4]
    with pytest.raises(ValueError, match = re.escape("Invalid direction: must be 0 (up), 1 (right), 2 (down), or 3 (left).")):
        snake = Snake(6,6,3,2,None,None,12,12,5)
    
    # size_snake
    with pytest.raises(ValueError, match = "Invalid snake size: must be >= 1 and must be int"):
        snake = Snake(3,3,3,0,None,None,12,12)
    with pytest.raises(ValueError, match = "Invalid snake size: must be >= 1 and must be int"):
        snake = Snake(3,3,3,1.5,None,None,12,12)
    
    ###################################################################################################################
    snake = Snake(6,6,3,1,None,None,12,12,3)
    assert snake._list_snake == [(6,6)]
    
    # snake_direction 0
    snake = Snake(6,6,3,3,None,None,15,15)
    assert snake._list_snake == [(6,6),(6,9),(6,12)]
    
    with pytest.raises(ValueError, match = "Snake body out of bounds: Y position is greater than window height."):
        snake = Snake(6,6,3,3,None,None,12,12)
        
    # snake_direction 1
    snake = Snake(6,6,3,3,None,None,15,15,1)
    assert snake._list_snake == [(6,6),(3,6),(0,6)]
    
    with pytest.raises(ValueError, match = "Snake body out of bounds: X position is less than zero."):
        snake = Snake(3,3,3,3,None,None,15,15,1)
    
    # snake_direction 2
    snake = Snake(6,6,3,3,None,None,15,15,2)
    assert snake._list_snake == [(6,6),(6,3),(6,0)]
    
    with pytest.raises(ValueError, match = "Snake body out of bounds: Y position is less than zero."):
        snake = Snake(3,3,3,3,None,None,15,15,2)
    
    # snake_direction 3
    snake = Snake(6,6,3,3,None,None,15,15,3)
    assert snake._list_snake == [(6,6),(9,6),(12,6)]
    
    with pytest.raises(ValueError, match = "Snake body out of bounds: X position is greater than window width."):
        snake = Snake(6,6,3,3,None,None,12,12,3)
        
    snake = Snake(6,6,3,2,None,None,12,12,3)

def test_direction_0_creates_segments_downwards():
    size_tile = 20
    x, y = 40, 40
    size_snake = 3
    win_x = win_y = 200
    s = Snake(x, y, size_tile, size_snake, None, None, win_x, win_y, 0)
    expected = [
        (x, y),
        (x, y + size_tile * 1),
        (x, y + size_tile * 2),
    ]
    assert s._list_snake == expected

def test_direction_1_creates_segments_leftwards():
    size_tile = 20
    x, y = 80, 40
    size_snake = 3
    win_x = win_y = 200
    s = Snake(x, y, size_tile, size_snake, None, None, win_x, win_y, 1)
    expected = [
        (x, y),
        (x - size_tile * 1, y),
        (x - size_tile * 2, y),
    ]
    assert s._list_snake == expected

def test_direction_2_creates_segments_upwards():
    size_tile = 20
    x, y = 80, 80
    size_snake = 3
    win_x = win_y = 200
    s = Snake(x, y, size_tile, size_snake, None, None, win_x, win_y, 2)
    expected = [
        (x, y),
        (x, y - size_tile * 1),
        (x, y - size_tile * 2),
    ]
    assert s._list_snake == expected

def test_direction_3_creates_segments_rightwards():
    size_tile = 20
    x, y = 40, 40
    size_snake = 3
    win_x = win_y = 200
    s = Snake(x, y, size_tile, size_snake, None, None, win_x, win_y, 3)
    expected = [
        (x, y),
        (x + size_tile * 1, y),
        (x + size_tile * 2, y),
    ]
    assert s._list_snake == expected

def test_size_one_keeps_single_segment():
    size_tile = 20
    x, y = 40, 40
    size_snake = 1
    win_x = win_y = 200
    s = Snake(x, y, size_tile, size_snake, None, None, win_x, win_y, 0)
    assert s._list_snake == [(x, y)]

# Tests para los errores de límites provocados por los for
def test_direction_0_out_of_bounds_raises():
    size_tile = 20
    x, y = 40, 60
    size_snake = 5
    win_x = 200
    win_y = 100  # suficientemente pequeño para provocar overflow
    with pytest.raises(ValueError):
        Snake(x, y, size_tile, size_snake, None, None, win_x, win_y, 0)

def test_direction_1_out_of_bounds_raises_negative_x():
    size_tile = 20
    x, y = 0, 40
    size_snake = 2
    win_x = win_y = 200
    with pytest.raises(ValueError):
        Snake(x, y, size_tile, size_snake, None, None, win_x, win_y, 1)

def test_direction_2_out_of_bounds_raises_negative_y():
    size_tile = 20
    x, y = 40, 0
    size_snake = 2
    win_x = win_y = 200
    with pytest.raises(ValueError):
        Snake(x, y, size_tile, size_snake, None, None, win_x, win_y, 2)

def test_direction_3_out_of_bounds_raises_overflow_x():
    size_tile = 20
    x, y = 80, 40
    size_snake = 2
    win_x = 100  # provocará que el último segmento + size_tile > win_x
    win_y = 200
    with pytest.raises(ValueError):
        Snake(x, y, size_tile, size_snake, None, None, win_x, win_y, 3)

def test_Snake_movement():
    snake = Snake(0,0,3,2,None,None,12,12,0)
    snake.Timer = lambda: True
    
    # direction_of_movement = None
    
    # 0
    snake._Snake__snake_direction = 0
    snake._Snake__x = 6 ;snake._Snake__y = 6
    snake.Snake_movement(2)
    assert snake._Snake__snake_direction == 0
    assert snake._list_snake[0] == (6,3)
    
    # 1
    snake._Snake__snake_direction = 1
    snake._Snake__x = 0 ;snake._Snake__y = 0
    snake.Snake_movement(3)
    assert snake._Snake__snake_direction == 1
    assert snake._list_snake[0] == (3,0)
    
    # 2
    snake._Snake__snake_direction = 2
    snake._Snake__x = 0 ;snake._Snake__y = 0
    snake.Snake_movement(0)
    assert snake._Snake__snake_direction == 2
    assert snake._list_snake[0] == (0,3)
    
    # 3
    snake._Snake__snake_direction = 3
    snake._Snake__x = 6 ;snake._Snake__y = 6
    snake.Snake_movement(1)
    assert snake._Snake__snake_direction == 3
    assert snake._list_snake[0] == (3,6)
    
    ############################################################################
    
    # direction_of_movement
    
    # 0
    snake._Snake__snake_direction = 1
    snake._Snake__x = 6 ;snake._Snake__y = 6
    snake.Snake_movement(0)
    assert snake._Snake__snake_direction == 0
    assert snake._list_snake[0] == (6,3)
    
    # 1
    snake._Snake__snake_direction = 2
    snake._Snake__x = 0 ;snake._Snake__y = 0
    snake.Snake_movement(1)
    assert snake._Snake__snake_direction == 1
    assert snake._list_snake[0] == (3,0)
    
    # 2
    snake._Snake__snake_direction = 3
    snake._Snake__x = 0 ;snake._Snake__y = 0
    snake.Snake_movement(2)
    assert snake._Snake__snake_direction == 2
    assert snake._list_snake[0] == (0,3)

    # 3
    snake._Snake__snake_direction = 0
    snake._Snake__x = 6 ;snake._Snake__y = 6
    snake.Snake_movement(3)
    assert snake._Snake__snake_direction == 3
    assert snake._list_snake[0] == (3,6)

def test_Snake_check_Collision():
    snake = Snake(0,0,3,4,0,1,15,15,0)
    snake._list_snake = [(3,3),(3,3)]
    
    snake.Snake_check_Collision()
    assert snake._live is False
    ###########################
    snake._live = True
    snake._list_snake = [(3,0),(3,3)]

    snake.Snake_check_Collision()
    assert snake._live is True
    ###########################
    snake._live = True
    snake._list_snake = [(3,3),(0,3)]
    
    snake.Snake_check_Collision()
    assert snake._live is True
    
def test_Snake_update_body_draw_while_pop_plus_size():
    snake = Snake(0,0,3,4,0,1,15,15,0)
    snake.Snake_Create_rectangle = Mock()
    
    snake._size_snake = 3
    snake._list_snake = [(3,3),(6,6),(9,9),(12,12),(15,15)]
    
    snake.Snake_update_body()
    assert len(snake._list_snake) == 3
    
    snake._size_snake = 2
    snake._list_snake = [(4,4),(8,8),(12,12),(16,16)]
    
    snake.Snake_update_body()
    assert len(snake._list_snake) == 2
    
def test_Snake_update_draw_Snake_Create_rectangle_snake():
    snake = Snake(0,0,3,4,0,1,15,15,0)
    snake.Snake_Create_rectangle = Mock()
    
    snake._list_snake = [(0,0),(3,0),(3,3),(6,3)]
    
    snake.Snake_update_body()
    
    snake.Snake_Create_rectangle.assert_has_calls([call(0,0,3,3,0),call(3,0,3,3,0),call(3,3,3,3,0),call(6,3,3,3,0)])
    
def test_Snake_update_draw_eyes():
    # 0 color_snake / 1 color_eyes / 2 color_BG / 3 second_color_BG
    snake = Snake(3,3,3,1,0,1,12,12,0)
    snake.Snake_Create_rectangle = Mock()
    
    # direction_of_movement
    
    # 0
    snake._Snake__snake_direction = 0
    snake.Snake_Create_rectangle.reset_mock()
    
    snake.Snake_update_eyes()
    
    snake.Snake_Create_rectangle.assert_has_calls([call(3,3,1,1,1),call(5,3,1,1,1)])
    
    # 1
    snake._Snake__snake_direction = 1
    snake.Snake_Create_rectangle.reset_mock()
    
    snake.Snake_update_eyes()
    
    snake.Snake_Create_rectangle.assert_has_calls([call(5,3,1,1,1),call(5,5,1,1,1)])
    
    # 2
    snake._Snake__snake_direction = 2
    snake.Snake_Create_rectangle.reset_mock()

    snake.Snake_update_eyes()
    
    snake.Snake_Create_rectangle.assert_has_calls([call(5,5,1,1,1),call(3,5,1,1,1)])
    
    # 3
    snake._Snake__snake_direction = 3
    snake.Snake_Create_rectangle.reset_mock()
    
    snake.Snake_update_eyes()
    
    snake.Snake_Create_rectangle.assert_has_calls([call(3,3,1,1,1),call(3,5,1,1,1)])
    
def test_Snake_eat_apple():
    snake = Snake(0,0,3,1,0,1,12,12,0)
    snake._list_snake = [(0,0),(3,0),(6,0)]
    list_apple = [(0,0)]
    
    snake.Snake_eat_apple(list_apple)
    
    assert list_apple == [] 
    assert snake._size_snake == 2