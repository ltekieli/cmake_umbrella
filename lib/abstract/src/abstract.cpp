#include "umbrella/abstract/abstract.h"

#include <umbrella/logging/logging.h>
#include <umbrella/rpc/rpc.h>

namespace umbrella {
namespace abstract {

void do_something() {
    logging::info("doing something");

    rpc::Proxy p;
    p.call();

    logging::info("done something");
}

}  // namespace abstract
}  // namespace umbrella
