add_library(rpc rpc.cpp)
target_include_directories(rpc
    PUBLIC
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_link_libraries(rpc
    PUBLIC
        umbrella::logging
)
set_target_properties(rpc PROPERTIES
    SOVERSION "${umbrella_rpc_VERSION_MAJOR}"
    VERSION "${umbrella_rpc_VERSION}"
)

add_library(umbrella::rpc ALIAS rpc)

include(GNUInstallDirs)

install(
    TARGETS
        rpc
    EXPORT
        umbrella_rpcTargets
    RUNTIME DESTINATION
        ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION
        ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION
        ${CMAKE_INSTALL_LIBDIR}
)

install(
    EXPORT
        umbrella_rpcTargets
    NAMESPACE
        umbrella::
    FILE
        umbrella_rpcTargets.cmake
    DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_rpc
)

install(
    FILES
        ${PROJECT_SOURCE_DIR}/include/umbrella/rpc/rpc.h
    DESTINATION
        ${CMAKE_INSTALL_INCLUDEDIR}/umbrella/rpc
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/umbrella_rpcConfig.cmake
    INSTALL_DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_rpc
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/umbrella_rpcConfigVersion.cmake
    VERSION
        "${umbrella_rpc_VERSION_MAJOR}.${umbrella_rpc_VERSION_MINOR}"
    COMPATIBILITY
        SameMajorVersion
)

# install the configuration file
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_rpcConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_rpcConfigVersion.cmake
    DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_rpc
)
