add_library(logging INTERFACE)
target_include_directories(logging
    INTERFACE
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)

add_library(logging_library logging.cpp)
target_include_directories(logging_library
    PRIVATE
        ${PROJECT_SOURCE_DIR}/include)

install(
    TARGETS
        logging
    DESTINATION
        lib
    EXPORT
        umbrella_loggingTargets
)

install(
    EXPORT
        umbrella_loggingTargets
    FILE
        umbrella_loggingTargets.cmake
    DESTINATION
        lib/cmake/umbrella_logging
)

install(
    FILES
        ${PROJECT_SOURCE_DIR}/include/umbrella/logging/logging.h
    DESTINATION
        include/umbrella/logging
)

