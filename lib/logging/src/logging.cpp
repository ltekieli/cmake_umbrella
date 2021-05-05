#include "umbrella/logging/logging.h"

#include <spdlog/spdlog.h>

namespace umbrella {
namespace logging {

void info(const std::string& msg) {
    spdlog::info(msg);
}

void warning(const std::string& msg) {
    spdlog::warn(msg);
}

void error(const std::string& msg) {
    spdlog::critical(msg);
}

}  // namespace logging
}  // namespace umbrella
