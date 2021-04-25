add_executable(worker main.cpp)
target_link_libraries(worker
    PRIVATE
        umbrella::abstract
        umbrella::logging
)

install(
    TARGETS
        worker
    DESTINATION
        bin
)
