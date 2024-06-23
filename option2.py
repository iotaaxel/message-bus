#include <queue>
#include <thread>
#include <chrono>
#include <atomic>
#include <iostream>

class MessageBus {
public:
    void send(const std::string& message) {
        queue_.push(message);
    }

    std::string receive() {
        std::string message;
        if (!queue_.empty()) {
            message = queue_.front();
            queue_.pop();
        }
        return message;
    }

private:
    std::queue<std::string> queue_;
};

void producer(MessageBus& bus) {
    for (int i = 0; i < 100000; ++i) {
        bus.send("Message " + std::to_string(i));
    }
}

void consumer(MessageBus& bus) {
    for (int i = 0; i < 100000; ++i) {
        std::string message = bus.receive();
        // Process the message
    }
}

int main() {
    MessageBus bus;

    std::thread producer_thread(producer, std::ref(bus));
    std::thread consumer_thread(consumer, std::ref(bus));

    auto start_time = std::chrono::high_resolution_clock::now();

    producer_thread.join();
    consumer_thread.join();

    auto end_time = std::chrono::high_resolution_clock::now();

    std::cout << "Total time: " << std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count() << " ms" << std::endl;
    std::cout << "Average latency: " << std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count() / 100000.0 << " ms" << std::endl;

    return 0;
}
