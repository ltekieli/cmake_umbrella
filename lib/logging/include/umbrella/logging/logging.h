#ifndef UMBRELLA_LOGGING_H_
#define UMBRELLA_LOGGING_H_

#include <string>

namespace umbrella {
namespace logging {

void info(const std::string& msg);

void warning(const std::string& msg);

void error(const std::string& msg);

}  // namespace logging
}  // namespace umbrella

#endif  // UMBRELLA_LOGGING_H_
