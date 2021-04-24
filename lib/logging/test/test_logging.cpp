#include <umbrella/logging/logging.h>

int main() {
    umbrella::logging::info("info");
    umbrella::logging::warning("warning");
    umbrella::logging::error("error");
    return 0;
}
