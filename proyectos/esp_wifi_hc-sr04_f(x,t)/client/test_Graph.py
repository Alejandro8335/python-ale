import pytest
import asyncio
from D_object_graph import Graph

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

@pytest.mark.asyncio
@pytest.mark.parametrize("input_sleep,input_queue,output_sleep,output_queue,data_consumer_state",[
    (1,5,[1],[5],True),
    (2,40,[1,2],[5,40],True),
    (5,39.9,[1,2,5],[5,40,39.9],True),
    (0.5,1.1,[1,2,5,0.5],[5,40,39.9,1.1],True),
    (2,None,None,None,False)
])
async def test_Graph_Data_consumer(fixture_pass_obj_Graph,input_sleep,input_queue,output_sleep,output_queue,data_consumer_state):
    try:
        queue,graph = fixture_pass_obj_Graph
        data_consumer_loop = asyncio.create_task(graph.Data_consumer())
        await asyncio.sleep(input_sleep)
        await queue.put(input_queue)
        await asyncio.sleep(0.1)
        if data_consumer_state is True:
            assert graph.X_data[-1] >= output_sleep
            assert graph.Y_data == output_queue
            assert graph.data_consumer_state == True
        elif data_consumer_state is False:
            assert graph.data_consumer_state == False
        else:
            raise TypeError("The data_consumer_state is not true or false")
    except Exception as e:
        data_consumer_loop.cancel()
        try:
            await data_consumer_loop
        except asyncio.CancelledError:
            pass
        raise e
    finally:
        data_consumer_loop.cancel()
        try:
            await data_consumer_loop
        except asyncio.CancelledError:
            pass