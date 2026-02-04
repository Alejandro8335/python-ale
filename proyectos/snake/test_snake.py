from snake import Snake
import pytest
import re 
from unittest.mock import Mock
from unittest.mock import call
# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos\snake\test_snake.py"

def test__init__():
    # size_tile
    with pytest.raises(ValueError,match = "Invalid size_tile: must be integer >= 3"):
        snake = Snake(None,None,3.5,None,None,None,None,None,None)
    with pytest.raises(ValueError,match = "Invalid size_tile: must be integer >= 3"):
        snake = Snake(None,None,1,None,None,None,None,None,None)
        
    # windows_size_x
    with pytest.raises(ValueError,match = "Invalid windows_size_x: must be divisible by size_tile and result in more than 2 tiles"):
        snake = Snake(None,None,3,None,None,None,4,None,None)
    with pytest.raises(ValueError,match = "Invalid windows_size_x: must be divisible by size_tile and result in more than 2 tiles"):
        snake = Snake(None,None,3,None,None,None,3,None,None)
        
    # windows_size_y
    with pytest.raises(ValueError, match = "Invalid windows_size_y: must be divisible by size_tile and result in more than 2 tiles"):
        snake = Snake(None,None,3,None,None,None,6,4,None)
    with pytest.raises(ValueError, match = "Invalid windows_size_y: must be divisible by size_tile and result in more than 2 tiles"):
        snake = Snake(None,None,3,None,None,None,6,3,None)
        
    # x
    with pytest.raises(ValueError, match = "Invalid x: must be divisible by size_tile and <= windows_size_x"):
        snake = Snake(1,None,3,None,None,None,6,6,None)
    with pytest.raises(ValueError, match = "Invalid x: must be divisible by size_tile and <= windows_size_x"):
        snake = Snake(9,None,3,None,None,None,6,6,None)
    
    # y
    with pytest.raises(ValueError, match = "Invalid y: must be divisible by size_tile and <= windows_size_y"):
        snake = Snake(3,1,3,None,None,None,6,6,None)
    with pytest.raises(ValueError, match = "Invalid y: must be divisible by size_tile and <= windows_size_y"):
        snake = Snake(3,9,3,None,None,None,6,6,None)
    
    # snake_direction not in [1,2,3,4]
    with pytest.raises(ValueError, match = re.escape("Invalid direction: must be 0 (up), 1 (right), 2 (down), or 3 (left).")):
        snake = Snake(6,6,3,2,None,None,12,12,None,5,None)
    
    # size_snake
    with pytest.raises(ValueError, match = "Invalid snake size: must be >= 1 and must be int"):
        snake = Snake(3,3,3,0,None,None,12,12,None)
    with pytest.raises(ValueError, match = "Invalid snake size: must be >= 1 and must be int"):
        snake = Snake(3,3,3,1.5,None,None,12,12,None)
    
    ###################################################################################################################
    snake = Snake(6,6,3,1,None,None,12,12,None,3,None)
    assert snake._list_snake == [(6,6)]
    
    # snake_direction 0
    snake = Snake(6,6,3,3,None,None,15,15,None)
    assert snake._list_snake == [(6,6),(6,9),(6,12)]
    
    with pytest.raises(ValueError, match = "Snake body out of bounds: Y position is greater than window height."):
        snake = Snake(6,6,3,3,None,None,12,12,None)
        
    # snake_direction 1
    snake = Snake(6,6,3,3,None,None,15,15,None,1)
    assert snake._list_snake == [(6,6),(3,6),(0,6)]
    
    with pytest.raises(ValueError, match = "Snake body out of bounds: X position is less than zero."):
        snake = Snake(3,3,3,3,None,None,15,15,None,1)
    
    # snake_direction 2
    snake = Snake(6,6,3,3,None,None,15,15,None,2)
    assert snake._list_snake == [(6,6),(6,3),(6,0)]
    
    with pytest.raises(ValueError, match = "Snake body out of bounds: Y position is less than zero."):
        snake = Snake(3,3,3,3,None,None,15,15,None,2)
    
    # snake_direction 3
    snake = Snake(6,6,3,3,None,None,15,15,None,3)
    assert snake._list_snake == [(6,6),(9,6),(12,6)]
    
    with pytest.raises(ValueError, match = "Snake body out of bounds: X position is greater than window width."):
        snake = Snake(6,6,3,3,None,None,12,12,None,3)
        
    snake = Snake(6,6,3,2,None,None,12,12,None,3,None)
    
def test_Snake_movement():
    snake = Snake(0,0,3,2,None,None,12,12,None,0)
    snake.Timer = lambda: True
    
    # direction_of_movement = None
    
    # 0
    snake._Snake__snake_direction = 0
    snake._Snake__x = 0 ;snake._Snake__y = 0
    snake.Snake_movement(2)
    assert snake._Snake__snake_direction == 0
    assert snake._list_snake[0] == (0,-3)
    
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
    snake._Snake__x = 0 ;snake._Snake__y = 0
    snake.Snake_movement(1)
    assert snake._Snake__snake_direction == 3
    assert snake._list_snake[0] == (-3,0)
    
    ############################################################################
    
    # direction_of_movement
    
    # 0
    snake._Snake__snake_direction = 1
    snake._Snake__x = 0 ;snake._Snake__y = 0
    snake.Snake_movement(0)
    assert snake._Snake__snake_direction == 0
    assert snake._list_snake[0] == (0,-3)
    
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
    snake._Snake__x = 0 ;snake._Snake__y = 0
    snake.Snake_movement(3)
    assert snake._Snake__snake_direction == 3
    assert snake._list_snake[0] == (-3,0)

def test_Snake_update_collisions():
    snake = Snake(0,0,3,1,0,1,12,12,2,0,3)
    snake._list_snake = [(0,0),(0,0)]
    snake.Snake_Create_rectangle = Mock()

    snake.Snake_update()
    
    snake.Snake_Create_rectangle.assert_not_called()
    #######################################################
    snake._list_snake = [(3,6),(0,0),(6,3),(3,6)]
    
    
    snake.Snake_update()
    
    snake.Snake_Create_rectangle.assert_not_called()
    
def test_Snake_update_while_Snake_Create_rectangle_color_BG_and_second_color_BG():
    # 0 color_snake / 1 color_eyes / 2 color_BG / 3 second_color_BG
    snake = Snake(0,0,3,1,0,1,12,12,2,0,3)
    snake.Snake_Create_rectangle = Mock()
    
    # color_BG
    snake._size_snake = 1
    snake._list_snake = [(0,0),(6,6)]
    snake.Snake_update()
    
    assert len(snake._list_snake) == 1
    snake.Snake_Create_rectangle.assert_has_calls([call(6,6,3,3,2)])
    
    # second_color_BG
    snake._size_snake = 1
    snake.Snake_Create_rectangle.reset_mock()
    snake._list_snake = [(0,0),(3,3)]
    snake.Snake_update()
    
    assert len(snake._list_snake) == 1
    snake.Snake_Create_rectangle.assert_has_calls([call(3,3,3,3,3)])
    
    # color_BG and size_snake = 2
    snake._size_snake = 2
    snake._list_snake = [(0,0),(3,3),(6,6)]
    snake.Snake_update()
    
    assert len(snake._list_snake) == 2
    snake.Snake_Create_rectangle.assert_has_calls([call(6,6,3,3,2)])
    # second_color_BG and size_snake = 2
    snake._size_snake = 2
    snake.Snake_Create_rectangle.reset_mock()
    snake._list_snake = [(0,0),(6,6),(3,3)]
    snake.Snake_update()
    
    assert len(snake._list_snake) == 2
    snake.Snake_Create_rectangle.assert_has_calls([call(3,3,3,3,3)])
    
    # color_BG and second_color_BG
    snake._size_snake = 1
    snake.Snake_Create_rectangle.reset_mock()
    snake._list_snake = [(0,0),(3,3),(6,6)]
    snake.Snake_update()
    
    assert len(snake._list_snake) == 1
    snake.Snake_Create_rectangle.assert_has_calls([call(6,6,3,3,2),call(3,3,3,3,3)])
    
def test_Snake_update_Snake_Create_rectangle_snake():
    snake = Snake(0,0,3,4,0,1,15,15,2,0,3)
    snake.Snake_Create_rectangle = Mock()
    
    snake._list_snake = [(0,0),(3,0),(3,3),(6,3)]
    
    snake.Snake_update()
    
    snake.Snake_Create_rectangle.assert_has_calls([call(0,0,3,3,0),call(3,0,3,3,0),call(3,3,3,3,0),call(6,3,3,3,0)])
    
def test_Snake_update_eyes():
    # 0 color_snake / 1 color_eyes / 2 color_BG / 3 second_color_BG
    snake = Snake(3,3,3,1,0,1,12,12,2,0,3)
    snake.Snake_Create_rectangle = Mock()
    
    # direction_of_movement
    
    # 0
    snake._Snake__snake_direction = 0
    snake.Snake_Create_rectangle.reset_mock()
    
    snake.Snake_update()
    
    snake.Snake_Create_rectangle.assert_has_calls([call(3,3,3,3,0),call(3,3,1,1,1),call(5,3,1,1,1)])
    
    # 1
    snake._Snake__snake_direction = 1
    snake.Snake_Create_rectangle.reset_mock()
    
    snake.Snake_update()
    
    snake.Snake_Create_rectangle.assert_has_calls([call(3,3,3,3,0),call(5,3,1,1,1),call(5,5,1,1,1)])
    
    # 2
    snake._Snake__snake_direction = 2
    snake.Snake_Create_rectangle.reset_mock()

    snake.Snake_update()
    
    snake.Snake_Create_rectangle.assert_has_calls([call(3,3,3,3,0),call(5,5,1,1,1),call(3,5,1,1,1)])
    
    # 3
    snake._Snake__snake_direction = 3
    snake.Snake_Create_rectangle.reset_mock()
    
    snake.Snake_update()
    
    snake.Snake_Create_rectangle.assert_has_calls([call(3,3,3,3,0),call(3,3,1,1,1),call(3,5,1,1,1)])
    
def test_Snake_eat_apple():
    snake = Snake(0,0,3,1,0,1,12,12,2,0,3)
    snake._list_snake = [(0,0),(3,0),(6,0)]
    list_apple = [(0,0)]
    
    snake.Snake_eat_apple(list_apple)
    
    assert list_apple == [] 
    assert snake._size_snake == 2