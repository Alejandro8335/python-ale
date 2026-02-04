from apple import Apples
import pytest
from unittest.mock import patch
from unittest.mock import Mock

# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos\snake\test_apple.py"

def test_Apples__init__():
    with pytest.raises(ValueError):
        apples = Apples(2.5,None,[],10,10)
    with pytest.raises(ValueError):
        apples = Apples(2,None,[],10,10)
    with pytest.raises(ValueError):
        apples = Apples(3,None,[],1.5,1)
    with pytest.raises(ValueError):
        apples = Apples(3,None,[],1,1.5)
    apples = Apples(3,None,[],10,10)

def test_Apples_Create_pair_size_tile():
    size_tile = 41
    apples = Apples(size_tile,None,[],10,10)
    
    list_added_positions_apples = []
    
    with patch.object(Apples, "Apples_draw_pixels") as def_mock:    
        x = 0;y = 0
        apples.Apples_Create((x,y))
        
        list_added_positions_apples = [tuple(call.args[-3:]) for call in def_mock.call_args_list]

        assert len(apples.list_x_y_apples) == 1
        assert apples.list_x_y_apples[0][0] == x and apples.list_x_y_apples[0][1] == y
    
    number_of_pixels = 41

    x = 0
    y = 0
    x_center_circle = x + (number_of_pixels / 2) -1
    y_center_circle = y + (number_of_pixels / 2) -1
    radio = (number_of_pixels) / 2 -1
    
    list_added_positions_expected = []
    for y_for in range(y,y + number_of_pixels):
        for x_for in range(x,x + number_of_pixels):
            if (x_for - x_center_circle)**2 + (y_for - y_center_circle)**2 < (radio)**2:
                list_added_positions_expected.append((x_for,y_for))
    
    assert len(list_added_positions_apples) == len(list_added_positions_expected)
    for list_apples , list_expected in zip(list_added_positions_apples,list_added_positions_expected):
        assert list_apples[0] == list_expected[0]
        assert list_apples[1] == list_expected[1]
        
def test_Apples_Create_odd_size_tile():
    size_tile = 40
    apples = Apples(size_tile,None,None,10,10)
    
    list_added_positions_apples = []
    
    with patch.object(Apples, "Apples_draw_pixels") as def_mock:    
        x = 0;y = 0
        apples.Apples_Create((x,y))
        
        list_added_positions_apples = [tuple(call.args[-3:]) for call in def_mock.call_args_list]

        assert len(apples.list_x_y_apples) == 1
        assert apples.list_x_y_apples[0][0] == x and apples.list_x_y_apples[0][1] == y
    
    number_of_pixels = 40

    x = 0
    y = 0
    x_center_circle = x + (number_of_pixels / 2) -1
    y_center_circle = y + (number_of_pixels / 2) -1
    radio = (number_of_pixels) / 2 -1
    
    list_added_positions_expected = []
    for y_for in range(y,y + number_of_pixels):
        for x_for in range(x,x + number_of_pixels):
            if (x_for - x_center_circle)**2 + (y_for - y_center_circle)**2 < (radio)**2:
                list_added_positions_expected.append((x_for,y_for))
    
    assert len(list_added_positions_apples) == len(list_added_positions_expected)
    for list_apples , list_expected in zip(list_added_positions_apples,list_added_positions_expected):
        assert list_apples[0] == list_expected[0]
        assert list_apples[1] == list_expected[1]
        
def test_Apples_random():
    apples = Apples(3,None,None,10,10)
    
    apples.Random = Mock()
    apples._Apples__Remove_tiles_that_are_in_use = Mock()
    
    apples._Apples__Remove_tiles_that_are_in_use.return_value = [(0,0),(1,0),(0,1),(1,1)]
    
    apples.Random.return_value = 2
    
    assert apples.Apples_random() == (0,1)
    
    apples._Apples__Remove_tiles_that_are_in_use.assert_called_once_with()
    
    apples.Random.assert_called_once_with(4)
    
def test__Remove_tiles_that_are_in_use():
    size_tile = 10 
    num_tiles_x = 3 
    num_tiles_y = 3 
    list_apples = [(0, 0), (10, 20)] 
    list_snake = [(20, 0), (20, 10)] 
    apples = Apples(size_tile, None, list_snake, num_tiles_x, num_tiles_y)
    
    apples.list_x_y_apples = list_apples
    result = apples._Apples__Remove_tiles_that_are_in_use()
    
    all_tiles = [(size_tile * x, size_tile * y) for y in range(num_tiles_y) for x in range(num_tiles_x)]
    
    expected = [tile for tile in all_tiles if tile not in list_apples and tile not in list_snake]
    
    assert result == expected