add_library(logging)
target_sources(logging
    PRIVATE
        logging.cpp
)
target_include_directories(logging
    PUBLIC
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_link_libraries(logging
    PUBLIC
        spdlog::spdlog
)

add_library(umbrella::logging ALIAS logging)

include(GNUInstallDirs)

install(
    TARGETS
        logging
    EXPORT
        umbrella_loggingTargets
    RUNTIME DESTINATION
        ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION
        ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION
        ${CMAKE_INSTALL_LIBDIR}
)

install(
    EXPORT
        umbrella_loggingTargets
    NAMESPACE
        umbrella::
    FILE
        umbrella_loggingTargets.cmake
    DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_logging
)

install(
    FILES
        ${PROJECT_SOURCE_DIR}/include/umbrella/logging/logging.h
    DESTINATION
        ${CMAKE_INSTALL_INCLUDEDIR}/umbrella/logging
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/umbrella_loggingConfig.cmake
    INSTALL_DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_logging
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/umbrella_loggingConfigVersion.cmake
    VERSION
        "${umbrella_logging_VERSION_MAJOR}.${umbrella_logging_VERSION_MINOR}"
    COMPATIBILITY
        SameMajorVersion
)

# install the configuration file
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_loggingConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/umbrella_loggingConfigVersion.cmake
    DESTINATION
        ${CMAKE_INSTALL_LIBDIR}/cmake/umbrella_logging
)
