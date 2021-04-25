add_library(abstract abstract.cpp)
target_include_directories(abstract
    PUBLIC
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_link_libraries(abstract
    PRIVATE
        umbrella::logging
        umbrella::rpc
)

add_library(umbrella::abstract ALIAS abstract)

install(
    TARGETS
        abstract
    DESTINATION
        lib
    EXPORT
        umbrella_abstractTargets
)

install(
    EXPORT
        umbrella_abstractTargets
    NAMESPACE
        umbrella::
    FILE
        umbrella_abstractTargets.cmake
    DESTINATION
        lib/cmake/umbrella_abstract
)

install(
    FILES
        ${PROJECT_SOURCE_DIR}/include/umbrella/abstract/abstract.h
    DESTINATION
        include/umbrella/abstract
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    "${CMAKE_CURRENT_BINARY_DIR}/umbrella_abstractConfig.cmake"
    INSTALL_DESTINATION
        "lib/cmake/umbrella_abstract"
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)

write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/umbrella_abstractConfigVersion.cmake"
    VERSION
        "${umbrella_abstract_VERSION_MAJOR}.${umbrella_abstract_VERSION_MINOR}"
    COMPATIBILITY
        AnyNewerVersion
)

# install the configuration file
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_abstractConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_abstractConfigVersion.cmake
    DESTINATION
        lib/cmake/umbrella_abstract
)
