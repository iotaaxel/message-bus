#include <benchmark/benchmark.h>
#include "my_message_bus.h"

void sendAndReceiveMessage(MessageBus& bus) {
    capnp::MessageBuilder message;
    // ... build the message ...
    bus.sendMessage(message);

    auto response = bus.receiveMessage();
    // ... process the response ...
}

BENCHMARK(sendAndReceiveMessage);
