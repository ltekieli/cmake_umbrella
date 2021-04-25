cmake_minimum_required(VERSION 3.10)

project(umbrella VERSION 0.1)

set(as_subproject
    umbrella_abstract umbrella_logging umbrella_rpc)

macro(find_package)
    if (NOT "${ARGV0}" IN_LIST as_subproject)
        _find_package(${ARGV})
    endif()
endmacro()

# Order matters
add_subdirectory(lib/logging)
add_subdirectory(lib/rpc)
add_subdirectory(lib/abstract)

add_subdirectory(apps/worker)

include(CTest)
