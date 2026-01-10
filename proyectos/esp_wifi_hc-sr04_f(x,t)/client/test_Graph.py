import pytest
import pytest_asyncio
import asyncio
from D_object_graph import Graph
from unittest.mock import Mock
# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos\esp_wifi_hc-sr04_f(x,t)\client\test_Graph.py"

@pytest.fixture(scope="module")
def fixture_pass_obj_Graph():
    queue = asyncio.Queue()
    graph = Graph(queue)
    yield queue,graph
    
def test_Graph_open(fixture_pass_obj_Graph):
    queue,graph = fixture_pass_obj_Graph
    if graph.open_state:
        raise ValueError("The window is open; the test cannot open another window.")
    graph.Graph_open()
    assert graph.open_state

def test_Graph_close(fixture_pass_obj_Graph):
    queue,graph = fixture_pass_obj_Graph
    if not graph.open_state:
        raise ValueError("The window is closed; the test cannot closed a window that does not exist.")
    graph.Graph_close()
    assert not graph.open_state

@pytest_asyncio.fixture(scope="function")
async def async_fixture_pass_obj_Graph():
    queue = asyncio.Queue()
    graph = Graph(queue)
    yield queue,graph

@pytest.mark.asyncio
async def test_2_put_in_Graph_Data_consumer(async_fixture_pass_obj_Graph):
    try:
        queue , graph = async_fixture_pass_obj_Graph
        Data_consumer = asyncio.create_task(graph.Data_consumer())
        await asyncio.sleep(1)
        await queue.put(1)
        await queue.join()
        await asyncio.sleep(2)
        await queue.put(2)
        await queue.join()
        assert graph.X_data[0] >= float(1)
        assert graph.Y_data[0] == float(1)
        assert graph.X_data[1] >= float(2)
        assert graph.Y_data[1] == float(2)
        assert len(graph.X_data) == 2
        for X_data,num in zip(graph.X_data,[1,2]):
            assert X_data >=  num
        assert graph.Y_data == [1,2]
    except Exception as e:
        graph.data_consumer_state = False
        Data_consumer.cancel()
        try:
            await Data_consumer
        except asyncio.CancelledError:
            pass
        raise e
    finally:
        graph.data_consumer_state = False
        Data_consumer.cancel()
        try:
            await Data_consumer
        except asyncio.CancelledError:
            pass
@pytest.mark.asyncio
@pytest.mark.parametrize("tuple_of_datas",[
    ((1,"5",[1],[5.0],True),
    (2,"40",[1,2],[5.0,40.0],True),
    (5,"39.9",[1,2,5],[5.0,40.0,39.9],True),
    (0.5,"1.1",[1,2,5,0.5],[5.0,40.0,39.9,1.1],True),
    (2,None,None,None,False))
])
async def test_Graph_Data_consumer(async_fixture_pass_obj_Graph,tuple_of_datas):
    try:
        queue , graph = async_fixture_pass_obj_Graph
        Data_consumer = asyncio.create_task(graph.Data_consumer())
        for input_sleep,input_queue,list_output_sleep,list_output_queue,data_consumer_state in tuple_of_datas:
                await asyncio.sleep(input_sleep)
                await queue.put(input_queue)
                await queue.join()
                if data_consumer_state is True:
                    assert graph.X_data[-1] >= input_sleep
                    assert len(graph.X_data) == len(list_output_sleep)
                    for X_data , output_sleep in zip(graph.X_data,list_output_sleep):
                        assert X_data >= output_sleep
                    assert graph.Y_data[-1] == float(input_queue)
                    assert graph.Y_data == list_output_queue
                    assert graph.data_consumer_state is True
                elif data_consumer_state is False:
                    assert graph.data_consumer_state is False
                else:
                    raise TypeError("The data_consumer_state is not true or false")
    except Exception as e:
        raise e
    finally:
        graph.data_consumer_state = False
        Data_consumer.cancel()
        try:
            await Data_consumer
        except asyncio.CancelledError:
            pass

@pytest.fixture(scope="function")
def fixture_open_close_windows():
    queue = asyncio.Queue()
    graph = Graph(queue)
    graph.Graph_open()
    yield queue , graph
    graph.Graph_close()


def test_update_frame_with_mocks(fixture_open_close_windows):
    # Crea un objeto de tu clase real
    _ ,obj =  fixture_open_close_windows

    # Sustituye line y ax por mocks
    obj.line = Mock()
    obj.ax = Mock()

    # Prepara datos conocidos
    obj.X_data = [1, 2]
    obj.Y_data = [3, 4]

    # Llama al método
    result = obj.Update_frame(frame=None)

    # Verifica que set_data se llamó con los datos correctos
    obj.line.set_data.assert_called_once_with([1, 2], [3, 4])

    # Verifica que relim y autoscale_view se llamaron
    obj.ax.relim.assert_called_once()
    obj.ax.autoscale_view.assert_called_once()

    # Verifica el retorno
    assert isinstance(result, tuple)
    assert result[0] is obj.line
