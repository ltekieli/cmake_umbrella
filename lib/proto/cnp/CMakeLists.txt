cmake_minimum_required(VERSION 3.10)

project(umbrella_cnp VERSION 0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(CapnProto REQUIRED)

capnp_generate_cpp(CAPNP_SRCS CAPNP_HDRS message.capnp)

add_library(cnp)
target_sources(cnp
    PRIVATE
        ${CAPNP_SRCS}
)
target_include_directories(cnp
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_BINARY_DIR}/lib>
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_link_libraries(cnp PUBLIC CapnProto::capnp)
set_target_properties(cnp PROPERTIES
    SOVERSION "${umbrella_cnp_VERSION_MAJOR}"
    VERSION "${umbrella_cnp_VERSION}"
)

add_library(umbrella::cnp ALIAS cnp)

include(GNUInstallDirs)

install(
    TARGETS
        cnp
    EXPORT
        umbrella_cnpTargets
    RUNTIME DESTINATION
        ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION
        ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION
        ${CMAKE_INSTALL_LIBDIR}
)

install(
    EXPORT
        umbrella_cnpTargets
    NAMESPACE
        umbrella::
    FILE
        umbrella_cnpTargets.cmake
    DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_cnp
)

install(
    FILES
        ${CAPNP_HDRS}
    DESTINATION
        ${CMAKE_INSTALL_INCLUDEDIR}/umbrella/proto/cnp
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/umbrella_cnpConfig.cmake
    INSTALL_DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_cnp
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/umbrella_cnpConfigVersion.cmake
    VERSION
        "${umbrella_cnp_VERSION_MAJOR}.${umbrella_cnp_VERSION_MINOR}"
    COMPATIBILITY
        SameMajorVersion
)

# install the configuration file
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_cnpConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_cnpConfigVersion.cmake
    DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_cnp
)
