set	(SOURCE
	 main.cpp
	)

set	(LIBS_DEPEND
	)

set(LIB Test)
add_library(${LIB} STATIC ${SOURCE})
target_link_libraries(${LIB} PRIVATE ${LIBS_DEPEND})


set (EXEC main)
set (LIBS_DEPEND Test)
add_executable(${EXEC} ${EXEC}.cpp)
target_link_libraries(${EXEC} PRIVATE ${LIBS_DEPEND})
add_test_DDI(${EXEC} "to_be_determined")
