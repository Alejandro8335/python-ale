from snake.pc.apple_for_pc import Apples_for_pc as Apples
from unittest.mock import patch

def create_apples():
    return Apples(size_tile = 5,
                  color_apples = None,
                  list_snake = [],
                  num_tiles_x = 15,
                  num_tiles_y = 15,
                  window = "_window_",
                  apples_create_cooldown = 100)

@patch("snake.pc.apple_for_pc.pygame.time.get_ticks")
def test_apples_for_pc_timer_false_then_true(mock_ticks):
    apples = create_apples()

    mock_ticks.return_value = 50
    assert apples.Timer() is False

    mock_ticks.return_value = 100
    assert apples.Timer() is True

    mock_ticks.return_value = 150
    assert apples.Timer() is False

@patch("snake.pc.apple_for_pc.pygame.draw.rect")
def test_apples_for_pc_apples_draw_pixels(mock_rect):
    apples = create_apples()
    
    apples.Apples_draw_pixels(10,20,(255,0,0))

    mock_rect.assert_called_once_with(
        "_window_",
        (255,0,0),
        (10, 20, 1,1)
    )
    
@patch("snake.pc.apple_for_pc.random.randint")
def test_apples_for_pc_Random(mock_randint):
    apples = create_apples()
    
    apples.Random(50)
    
    mock_randint.assert_called_once_with(0,49)