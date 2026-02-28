from snake.pc.snake_for_pc import Snake_for_pc as Snake
from unittest.mock import patch

# cd C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos\snake
#  pytest

def create_snake():
    return Snake(
        x=0, y=0,
        size_tile=10,
        size_snake=1,
        color_snake=(0,255,0),
        color_eyes=(0,0,0),
        windows_size_x=100,
        windows_size_y=100,
        move_cooldown=100,
        window="fake_window",
    )

@patch("snake.pc.snake_for_pc.pygame.time.get_ticks")
def test_snake_for_pc_timer_false_then_true(mock_ticks):
    snake = create_snake()

    mock_ticks.return_value = 50
    assert snake.Timer() is False

    mock_ticks.return_value = 100
    assert snake.Timer() is True

    mock_ticks.return_value = 150
    assert snake.Timer() is False
    
@patch("snake.pc.snake_for_pc.pygame.draw.rect")
def test_snake_for_pc_snake_create_rectangle(mock_rect):
    snake = create_snake()
    
    snake.Snake_Create_rectangle(10, 20, 30, 40, (255,0,0))

    mock_rect.assert_called_once_with(
        "fake_window",
        (255,0,0),
        (10, 20, 30, 40)
    )