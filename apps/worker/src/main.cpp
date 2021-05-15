#include <umbrella/abstract/abstract.h>
#include <umbrella/logging/logging.h>

#include <umbrella/proto/cnp/message.capnp.h>
#include <umbrella/proto/pb/message.pb.h>

#include <capnp/message.h>

int main() {
    example::Message m;
    m.add_id(10);
    m.add_id(11);
    m.add_id(12);
    umbrella::logging::info(m.DebugString());

    ::capnp::MallocMessageBuilder message;
    Message::Builder b = message.initRoot<Message>();
    b.setId(23);
    auto r = b.asReader();

    umbrella::logging::info(r.toString().flatten().cStr());

    umbrella::logging::info("starting worker");
    umbrella::abstract::do_something();
    umbrella::logging::error("something bad?");
    umbrella::logging::info("stopping worker");
    return 0;
}
