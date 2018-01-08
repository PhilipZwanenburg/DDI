set	(SOURCE
	 test_integration_generate_ideal.cpp
	)

set	(LIBS_DEPEND
	 Core
	)

set(LIB Test_Integration)
add_library(${LIB} STATIC ${SOURCE})
target_link_libraries(${LIB} PRIVATE ${LIBS_DEPEND})


set (EXEC test_integration_generate_ideal)
set (LIBS_DEPEND Core)
add_executable(${EXEC} ${EXEC}.cpp)
target_link_libraries(${EXEC} PRIVATE ${LIBS_DEPEND})
add_test_DDI(${EXEC} "atvi_10y")
