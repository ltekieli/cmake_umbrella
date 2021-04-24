#ifndef UMBRELLA_LOGGING_H_
#define UMBRELLA_LOGGING_H_

#include <iostream>
#include <string>

namespace umbrella {
namespace logging {

inline void info(const std::string& msg) {
    std::cout << msg << '\n';
}

inline void warning(const std::string& msg) {
    std::cout << msg << '\n';
}

inline void error(const std::string& msg) {
    std::cout << msg << '\n';
}

}  // namespace logging
}  // namespace umbrella

#endif  // UMBRELLA_LOGGING_H_
