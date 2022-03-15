cmake_minimum_required(VERSION 3.10)

project(umbrella_full VERSION 0.1)

if(NOT TARGET umbrella::abstract)
    find_package(umbrella_abstract REQUIRED)
endif()

if(NOT TARGET umbrella::logging)
    find_package(umbrella_logging REQUIRED)
endif()

if(NOT TARGET umbrella::rpc)
    find_package(umbrella_rpc REQUIRED)
endif()

if(NOT TARGET umbrella::cnp)
    find_package(umbrella_cnp REQUIRED)
endif()

if(NOT TARGET umbrella::pb)
    find_package(umbrella_pb REQUIRED)
endif()


add_library(full SHARED)
target_sources(full
    PRIVATE
        dummy.cpp
)
target_include_directories(full
    PUBLIC
        $<INSTALL_INTERFACE:include>
)
target_link_libraries(full
    PUBLIC
        -Wl,--whole-archive
        umbrella::abstract
        umbrella::logging
        umbrella::rpc
        umbrella::cnp
        umbrella::pb
        -Wl,--no-whole-archive
)
set_target_properties(full PROPERTIES
    SOVERSION "${umbrella_full_VERSION_MAJOR}"
    VERSION "${umbrella_full_VERSION}"
)

add_library(umbrella::full ALIAS full)

include(GNUInstallDirs)

install(
    TARGETS
        full
    EXPORT
        umbrella_fullTargets
    RUNTIME DESTINATION
        ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION
        ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION
        ${CMAKE_INSTALL_LIBDIR}
)

install(
    EXPORT
        umbrella_fullTargets
    NAMESPACE
        umbrella::
    FILE
        umbrella_fullTargets.cmake
    DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_full
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/umbrella_fullConfig.cmake
    INSTALL_DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_full
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/umbrella_fullConfigVersion.cmake
    VERSION
        "${umbrella_full_VERSION_MAJOR}.${umbrella_full_VERSION_MINOR}"
    COMPATIBILITY
        SameMajorVersion
)

# install the configuration file
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_fullConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_fullConfigVersion.cmake
    DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_full
)

