/* {{{
This file is part of DDI.

DDI is free software: you can redistribute it and/or modify it under the terms of the GNU General
Public License as published by the Free Software Foundation, either version 3 of the License, or any
later version.

DDI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
License for more details.

You should have received a copy of the GNU General Public License along with DDI.  If not, see
<http://www.gnu.org/licenses/>.
}}} */
/** \file
 */

#include <iostream>
#include <fstream>
#include <stdexcept>

#include "macros.hpp"
#include "cmake.hpp"

#include "core.hpp"

using namespace std;

/** \test Integration test which generates optimal trading behaviour for maximized profit by always
 *        buying/selling before a value increase/decrease (\ref
 *        test_integration_generate_ideal.cpp).
 *  \return 0 on success.
 */
int main
	(int argc,     ///< Standard.
	 char** argv_i ///< Standard.
	)
try {
	auto argv = ddi::arguments(argc,argv_i);

	cout << "Hello c++!\n";
	cout << ddi::PROJECT_SOURCE_DIR << "\n";

	for (auto x : argv)
		cout << "name: " << x << "\n";

	string iname {ddi::PROJECT_SOURCE_DIR+"/input/data/"+argv[1]+".csv"};
	ifstream ifs {iname};
/// \todo Derive a checked ifstream which throws on open failure.
	if (!ifs) throw invalid_argument("Failed to open file: "+iname);

	ddi::ETF_Data<float> etf_data(ifs);

	for (int i = 0; i < 2; ++i)
		cout << etf_data[i];


	throw logic_error("Test not yet implemented.");

	cout << "Successful termination!\n\n";
} catch (exception& e) {
	cerr << "Error, caught exception: " << e.what() << '\n';
	return 1;
} catch (...) {
	cerr << "Error: unhandled exception.\n";
	return 1;
}
