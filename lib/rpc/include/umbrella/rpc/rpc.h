#ifndef UMBRELLA_RPC_H_
#define UMBRELLA_RPC_H_

namespace umbrella {
namespace rpc {

class Proxy {
public:
    void call();
};

class Skeleton {
public:
    void listen();
};

}  // namespace rpc
}  // namespace umbrella

#endif  // UMBRELLA_RPC_H_
