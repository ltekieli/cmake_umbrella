#include "umbrella/rpc/rpc.h"

#include <umbrella/logging/logging.h>

namespace umbrella {
namespace rpc {

void Proxy::call() {
    logging::info("Proxy::call called");
}

void Skeleton::listen() {
    logging::info("Skeleton::listen called");
}

}  // namespace rpc
}  // namespace umbrella
