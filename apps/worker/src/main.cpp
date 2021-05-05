#include <umbrella/abstract/abstract.h>
#include <umbrella/logging/logging.h>

int main() {
    umbrella::logging::info("starting worker");
    umbrella::abstract::do_something();
    umbrella::logging::error("something bad?");
    umbrella::logging::info("stopping worker");
    return 0;
}
