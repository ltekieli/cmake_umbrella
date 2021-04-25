#include <umbrella/rpc/rpc.h>

int main() {
    umbrella::rpc::Skeleton s;
    s.listen();
    return 0;
}
