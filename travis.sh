#!/bin/bash
set -eux

TOP_DIR=${PWD}
CMAKE_RUN=${TOP_DIR}/cmake/run/

# Run `cmake`
cd $CMAKE_RUN
python3.5 ${ENVIRONMENT}.py ${CMAKE_PARAMETERS}

# Compile and execute various make targets
cd ${TOP_DIR}/build
make
CTEST_OUTPUT_ON_FAILURE=1 ctest
make coverage
