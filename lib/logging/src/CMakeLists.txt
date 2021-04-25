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

add_library(umbrella::logging ALIAS logging)

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
    NAMESPACE
        umbrella::
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

include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    "${CMAKE_CURRENT_BINARY_DIR}/umbrella_loggingConfig.cmake"
    INSTALL_DESTINATION
        "lib/cmake/umbrella_logging"
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)

write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/umbrella_loggingConfigVersion.cmake"
    VERSION
        "${umbrella_logging_VERSION_MAJOR}.${umbrella_logging_VERSION_MINOR}"
    COMPATIBILITY
        AnyNewerVersion
)

# install the configuration file
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_loggingConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_loggingConfigVersion.cmake
    DESTINATION
        lib/cmake/umbrella_logging
)
