# Provide commands required for ctest.

# Required to avoid errors along the lines of "Cannot find file:
# /path/to/DDI/build/DartConfiguration.tcl"
include(CTest)

# Following the discussion in [this SO answer][https://stackoverflow.com/a/16163137/5983549], the
# `check` make target is added below to force ctest to run with additional default parameters.
if (CMAKE_CONFIGURATION_TYPES)
    add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND}
        --force-new-ctest-process --output-on-failure
        --build-config "$<CONFIGURATION>")
else()
    add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND}
        --force-new-ctest-process --output-on-failure)
endif()

# Add a test with input test name and an arbitrary number of trailing command line arguments.
function(add_test_DDI test_exec)
	# The optional command line arguments should be passed as a string and are stored in ${ARGV1} if present.

	set(extra_args ${ARGN})
	list(LENGTH extra_args n_extra_args)

	if (n_extra_args EQUAL 0)
		add_test(NAME ${test_exec} COMMAND ${test_exec} WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
	elseif (n_extra_args EQUAL 1)
		add_test(NAME ${test_exec}___${ARGV1} COMMAND ${test_exec} ${ARGV1} WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
	elseif (n_extra_args EQUAL 2)
		add_test(NAME ${test_exec}___${ARGV1} COMMAND ${test_exec} ${ARGV1} ${ARGV2} WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
	else ()
		message(FATAL_ERROR "Invalid number of command line arguments." )
	endif()
endfunction()

# Add a test with input path and executable and an arbitrary number of trailing command line arguments.
function(add_test_DDI_w_path exec_path test_exec)
	# The optional command line arguments should be passed as a string and are stored in ${ARGV1} if present.

	set(extra_args ${ARGN})
	list(LENGTH extra_args n_extra_args)

	if (n_extra_args EQUAL 0)
		add_test(NAME ${test_exec} COMMAND ${exec_path}${test_exec} WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
	elseif (n_extra_args EQUAL 1)
		add_test(NAME ${test_exec}___${ARGV2} COMMAND ${exec_path}${test_exec} ${ARGV2} WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
	elseif (n_extra_args EQUAL 2)
		add_test(NAME ${test_exec}___${ARGV2} COMMAND ${exec_path}${test_exec} ${ARGV2} ${ARGV3} WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
	else ()
		message(FATAL_ERROR "Invalid number of command line arguments." )
	endif()
endfunction()
