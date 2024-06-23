import queue
import time
import threading

class MessageBus:
    def __init__(self):
        self.queue = queue.Queue()

    def send(self, message):
        self.queue.put(message)

    def receive(self):
        return self.queue.get()

def producer(bus):
    for i in range(100000):
        bus.send(f"Message {i}")

def consumer(bus):
    for _ in range(100000):
        message = bus.receive()
        # Process the message

bus = MessageBus()

producer_thread = threading.Thread(target=producer, args=(bus,))
consumer_thread = threading.Thread(target=consumer, args=(bus,))

start_time = time.time()

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

end_time = time.time()

print(f"Total time: {end_time - start_time:.2f} seconds")
print(f"Average latency: {(end_time - start_time) / 100000 * 1000:.2f} ms")
