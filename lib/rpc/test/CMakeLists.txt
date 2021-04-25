add_executable(test_rpc test_rpc.cpp)
target_link_libraries(test_rpc PRIVATE rpc)

add_test(NAME test_rpc COMMAND test_rpc)


