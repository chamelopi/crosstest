# Flags
add_compile_options(-Wall -Wextra -std=c++11 -pedantic)


add_library(mylib mylib.cpp)

add_executable(hello hello.cpp)
# statically link, since it breaks on windows otherwise
target_link_libraries(hello mylib -static)
