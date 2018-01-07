#!/usr/bin/env python3

import sys,os
import subprocess,shlex

from pathlib import Path

if __name__ == "__main__":
	"""
	Executes the cmake command for the initial code configuration in the terminal.

	At least two input arguments are required: build_type, toolchain_type (See assertions below
	for supported options). An optional 3rd argument may be input for the relative path of the
	build directory from the project ROOT directory; it is set to "build" by default otherwise.
	"""

	nargc = len(sys.argv)
	assert (nargc >= 3 and nargc <= 4),\
	       "Invalid number of input arguments: "+str(nargc)+". 3 or 4 required."

	build_type_in = sys.argv[1]
	assert (build_type_in in ["debug","release","coverage"]),\
	        "Unsupported build_type: "+build_type_in+" in argv[1]. Please select one of: debug, release, coverage."

	if (build_type_in == "release"):
		build_type = "Release"
	else:
		build_type = "Debug"

	toolchain_type = sys.argv[2]
	assert (toolchain_type in ["gcc"]),\
	        "Unsupported toolchain_type: "+toolchain_type+" in argv[2]. Please select one of: gcc."

	if (nargc == 3):
		build_rel_path = "build"
	else:
		build_rel_path = sys.argv[3]

	top_dir       = os.getcwd() + "/../.."
	toolchain_dir = top_dir+"/cmake/toolchains"
	build_dir     = Path(top_dir+"/"+build_rel_path)

	cmake_command  = "cmake"+" "\
	                 "-D CMAKE_BUILD_TYPE="+build_type+" "\
	                 "-D CMAKE_TOOLCHAIN_FILE="+toolchain_dir+"/"+toolchain_type+".cmake"+" "
	if (build_type_in == "coverage"):
		cmake_command += "-D CODE_COVERAGE_DDI=1"+" "
	cmake_command += top_dir

	build_dir.mkdir(exist_ok=True)
	subprocess.call(shlex.split(cmake_command),cwd=str(build_dir))
