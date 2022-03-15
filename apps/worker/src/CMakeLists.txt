add_executable(worker main.cpp)
target_link_libraries(worker
    PRIVATE
        umbrella::full
)

install(
    TARGETS
        worker
    DESTINATION
        bin
)
