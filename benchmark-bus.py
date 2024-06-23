import pytest
from my_message_bus import MessageBus

@pytest.mark.benchmark
def test_message_bus_latency(benchmark):
    bus = MessageBus()
    bus.connect("tcp://localhost:5555")

    def send_and_receive_message():
        bus.send_message({"key": "value"})
        response = bus.receive_message()
        return response

    benchmark(send_and_receive_message)
