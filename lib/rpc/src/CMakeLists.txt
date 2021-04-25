add_library(rpc rpc.cpp)
target_include_directories(rpc
    PUBLIC
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_link_libraries(rpc
    PRIVATE
        umbrella::logging
)

add_library(umbrella::rpc ALIAS rpc)

install(
    TARGETS
        rpc
    DESTINATION
        lib
    EXPORT
        umbrella_rpcTargets
)

install(
    EXPORT
        umbrella_rpcTargets
    NAMESPACE
        umbrella::
    FILE
        umbrella_rpcTargets.cmake
    DESTINATION
        lib/cmake/umbrella_rpc
)

install(
    FILES
        ${PROJECT_SOURCE_DIR}/include/umbrella/rpc/rpc.h
    DESTINATION
        include/umbrella/rpc
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    "${CMAKE_CURRENT_BINARY_DIR}/umbrella_rpcConfig.cmake"
    INSTALL_DESTINATION
        "lib/cmake/umbrella_rpc"
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)

write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/umbrella_rpcConfigVersion.cmake"
    VERSION
        "${umbrella_rpc_VERSION_MAJOR}.${umbrella_rpc_VERSION_MINOR}"
    COMPATIBILITY
        AnyNewerVersion
)

# install the configuration file
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_rpcConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_rpcConfigVersion.cmake
    DESTINATION
        lib/cmake/umbrella_rpc
)
