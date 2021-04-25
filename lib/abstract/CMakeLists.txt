cmake_minimum_required(VERSION 3.10)

project(umbrella_abstract VERSION 0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(umbrella_logging REQUIRED)
find_package(umbrella_rpc REQUIRED)

set(CMAKE_INSTALL_RPATH "$ORIGIN/../lib")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

add_subdirectory(src)

include(CTest)
if (BUILD_TESTING)
    add_subdirectory(test)
endif()
