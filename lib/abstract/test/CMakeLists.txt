add_executable(test_abstract test_abstract.cpp)
target_link_libraries(test_abstract PRIVATE abstract)

add_test(NAME test_abstract COMMAND test_abstract)


