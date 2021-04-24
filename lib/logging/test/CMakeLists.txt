add_executable(test_logging test_logging.cpp)
target_link_libraries(test_logging PRIVATE logging)

add_test(NAME test_logging COMMAND test_logging)


