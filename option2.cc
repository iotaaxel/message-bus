#include <zmq.hpp>
#include <capnp/serialize.h>

class MessageBus {
public:
    MessageBus() : context_(1), socket_(context_, ZMQ_REQ) {}

    void connect(const std::string& address) {
        socket_.connect(address);
    }

    void sendMessage(const capnp::MessageBuilder& message) {
        auto serializedMessage = message.toFlatArray();
        zmq::message_t zmqMessage(serializedMessage.size());
        memcpy(zmqMessage.data(), serializedMessage.data(), serializedMessage.size());
        socket_.send(zmqMessage);
    }

    capnp::FlatArray<capnp::word> receiveMessage() {
        zmq::message_t zmqMessage;
        socket_.recv(&zmqMessage);
        return capnp::FlatArray<capnp::word>(reinterpret_cast<capnp::word*>(zmqMessage.data()), zmqMessage.size() / sizeof(capnp::word));
    }

private:
    zmq::context_t context_;
    zmq::socket_t socket_;
};

// Example usage
int main() {
    MessageBus bus;
    bus.connect("tcp://localhost:5555");

    capnp::MessageBuilder message;
    // ... build the message ...
    bus.sendMessage(message);

    auto response = bus.receiveMessage();
    // ... process the response ...
    return 0;
}
