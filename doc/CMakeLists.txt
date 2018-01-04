find_package(Doxygen OPTIONAL_COMPONENTS dot)

if(DOXYGEN_FOUND)
	find_package(LATEX REQUIRED BIBTEX)
	add_custom_target(doc COMMAND ${DOXYGEN_EXECUTABLE} doxygen.cfg)

	# There was a problem with DOXYGEN_DOT_FOUND not being set even when dot was found. Try removing this after
	# updating CMake version. This addition was not tested on a machine where dot was not present.
	if (TARGET Doxygen::dot)
		set(DOXYGEN_DOT_FOUND YES)
	endif()

	configure_file(${PROJECT_SOURCE_DIR}/doc/doxygen.cfg.in
	               ${PROJECT_BINARY_DIR}/doc/doxygen.cfg @ONLY)

	file(GLOB_RECURSE FILES *.pdf)
	foreach(pdf_name_full ${FILES})
		string(REPLACE "${CMAKE_SOURCE_DIR}/doc" "/doc/html" pdf_name ${pdf_name_full})
		configure_file(${pdf_name_full} ${PROJECT_BINARY_DIR}${pdf_name} COPYONLY)
	endforeach()
endif()
