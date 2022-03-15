cmake_minimum_required(VERSION 3.10)

project(umbrella VERSION 0.1)

# Order matters
add_subdirectory(lib/logging)
add_subdirectory(lib/rpc)
add_subdirectory(lib/abstract)

add_subdirectory(lib/proto/cnp)
add_subdirectory(lib/proto/pb)

add_subdirectory(lib/full)

add_subdirectory(apps/worker)

include(CTest)
