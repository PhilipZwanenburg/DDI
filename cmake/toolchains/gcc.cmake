# Toolchain file for the GCC (default)
#
# Set `CMAKE_TOOLCHAIN_FILE` while running `cmake` to use this file.


# Compilers
set(CMAKE_CXX_COMPILER "g++")

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED on)


# Compile flags
set(CMAKE_CXX_FLAGS_DEBUG          "-fPIC -g -Wall -Wextra -Wconversion -Werror"     CACHE STRING "Debug flags")
set(CMAKE_CXX_FLAGS_RELEASE        "-fPIC -O3 -DNDEBUG"                              CACHE STRING "Release flags")
set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "-fPIC -O2 -g -Wall -Wextra -Wconversion -Werror" CACHE STRING "Release with debug info flags")
