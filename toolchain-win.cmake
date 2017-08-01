# Toolchain file for Windows x64 (MinGW)
set(CMAKE_SYSTEM_NAME Windows)

# Which compilers to use for C and C++
SET(CMAKE_C_COMPILER x86_x64-w64-mingw-gcc)
SET(CMAKE_CXX_COMPILER x86_x64-w64-mingw-g++)

# Location of the target environment (add directory for user-built libararies
# if necessary)
SET(CMAKE_FIND_ROOT_PATH  /usr/x86_x64-w64-mingw)

# Adjust the default behaviour of the FIND_XXX() commands:
# Search headers and libraries in the target environment, search
# Programs in the host environment
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
