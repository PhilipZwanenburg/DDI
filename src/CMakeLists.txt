# add coverage
option(CODE_COVERAGE_DDI "Check code coverage of DDI." OFF)
if (CODE_COVERAGE_DDI)
	include(CodeCoverage)
	SET(CMAKE_CXX_FLAGS "-g -O0 -fprofile-arcs -ftest-coverage")

	# A `space` separated list may be specified for file patterns to be removed.
	setup_target_for_coverage(coverage bin/main coverage "placehold*")
endif()


configure_file_hpp_in(${PROJECT_SOURCE_DIR}/src/ cmake.hpp.in)
add_include_directories()


set	(SOURCE
	 core.cpp
	)

set	(LIBS_DEPEND
	)

set(LIB Core)
add_library(${LIB} STATIC ${SOURCE})
target_link_libraries(${LIB} PRIVATE ${LIBS_DEPEND})


add_subdirectory(testing)

include_directories(
	testing
	)
