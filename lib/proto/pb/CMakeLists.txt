cmake_minimum_required(VERSION 3.10)

project(umbrella_pb VERSION 0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(Protobuf REQUIRED)

protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS message.proto)

add_library(pb)
target_sources(pb
    PRIVATE
        ${PROTO_SRCS}
)
target_include_directories(pb
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_BINARY_DIR}/lib>
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_link_libraries(pb PUBLIC protobuf::libprotobuf)

# seems Protobuf have conversion errors
target_compile_options(pb
    PRIVATE
        -Wno-conversion
)

add_library(umbrella::pb ALIAS pb)

include(GNUInstallDirs)

install(
    TARGETS
        pb
    EXPORT
        umbrella_pbTargets
    RUNTIME DESTINATION
        ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION
        ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION
        ${CMAKE_INSTALL_LIBDIR}
)

install(
    EXPORT
        umbrella_pbTargets
    NAMESPACE
        umbrella::
    FILE
        umbrella_pbTargets.cmake
    DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_pb
)

install(
    FILES
        ${PROTO_HDRS}
    DESTINATION
        ${CMAKE_INSTALL_INCLUDEDIR}/umbrella/proto/pb
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/umbrella_pbConfig.cmake
    INSTALL_DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_pb
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/umbrella_pbConfigVersion.cmake
    VERSION
        "${umbrella_pb_VERSION_MAJOR}.${umbrella_pb_VERSION_MINOR}"
    COMPATIBILITY
        SameMajorVersion
)

# install the configuration file
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_pbConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_pbConfigVersion.cmake
    DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_pb
)
