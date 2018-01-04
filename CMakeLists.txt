# Execute cmake using specific build parameters from '$ROOT/cmake/run' using, for example:
# $ ./gcc_debug.sh
#
# CMake Warnings which may be safely ignored when the conditions in braces () are satisfied:
# - "Manually-specified variables were not used by the project: CMAKE_TOOLCHAIN_FILE"
#   (after the initial build)

cmake_minimum_required(VERSION 3.9)

message("Running cmake (version ${CMAKE_VERSION}) with build type: ${CMAKE_BUILD_TYPE}.\n")

project(DDI)


set(DDI_VERSION_MAJOR 1)
set(DDI_VERSION_MINOR 0)
set(DDI_VERSION "${DDI_VERSION_MAJOR}.${DDI_VERSION_MINOR}")

set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Global includes
list	(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake/modules"
	)
include(functions)
include(ctest_testing)

option(BUILD_SHARED_LIBS "Build the shared library" OFF)

include_directories(src)

add_subdirectory(src)
add_subdirectory(doc)
