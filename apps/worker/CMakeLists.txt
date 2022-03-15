cmake_minimum_required(VERSION 3.10)

project(umbrella_abstract VERSION 0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

if(NOT TARGET umbrella::full)
    find_package(umbrella_full REQUIRED)
endif()

add_subdirectory(src)
