cmake_minimum_required(VERSION 3.10)

project(umbrella_abstract VERSION 0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

if(NOT TARGET umbrella::logging)
    find_package(umbrella_logging REQUIRED)
endif()

if(NOT TARGET umbrella::rpc)
    find_package(umbrella_rpc REQUIRED)
endif()

add_subdirectory(src)

include(CTest)
if(BUILD_TESTING)
    add_subdirectory(test)
endif()
