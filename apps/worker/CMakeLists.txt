cmake_minimum_required(VERSION 3.10)

project(umbrella_abstract VERSION 0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

if(NOT TARGET umbrella::abstract)
    find_package(umbrella_abstract REQUIRED)
endif()

if(NOT TARGET umbrella::logging)
    find_package(umbrella_logging REQUIRED)
endif()

if(NOT TARGET umbrella::cnp)
    find_package(umbrella_cnp REQUIRED)
endif()

if(NOT TARGET umbrella::pb)
    find_package(umbrella_pb REQUIRED)
endif()

add_subdirectory(src)
