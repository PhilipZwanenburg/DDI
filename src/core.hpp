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
#ifndef DDI__core_hpp__INCLUDED
#define DDI__core_hpp__INCLUDED
/** \file
 *  \brief Defines core functions.
 */

#include <vector>
#include <string>
#include <iostream>

namespace ddi {

/** \brief Return a `vector<string>` to be used instead of the `char**` format for argv.
 *  \return See brief.
 *
 *  This function was copied from (p. 254, \cite Stroustrup2013).
 */
std::vector<std::string> arguments
	(int argc,   ///< Number of arguments.
	 char** argv ///< Array of `char*` arguments.
	);


/// \brief Container for daily trading data.
template<typename scalar>
class Daily_Data {
public:
	/// \brief Standard (operator).
	template<typename scalar_>
	friend std::istream& operator>>
		(std::istream& is,       ///< Input stream.
		 Daily_Data<scalar_>& dd ///< Standard.
		);

	/// \brief Standard (operator).
	template<typename scalar_>
	friend std::ostream& operator<<
		(std::ostream& os,             ///< Output stream.
		 const Daily_Data<scalar_>& dd ///< Standard.
		);
private:
	std::string date; ///< Date.
	scalar open,      ///< Price (open).
	       close,     ///< Price (close).
	       low,       ///< Price (low).
	       high;      ///< Price (high).
	int volume;       ///< Trading volume.
};

/// \brief Container for all data for a given ETF.
template<typename scalar>
class ETF_Data {
public:
	/// \brief Constructor.
	ETF_Data
		(std::ifstream& ifs ///< Input file stream.
		);

	/// \brief Push the input \ref Daily_Data to the back of the data vector.
	void push_back_data
		(const Daily_Data<scalar>& dd ///< \ref Daily_Data.
		);

	/** \brief Standard (operator).
	 *  \return See brief. */
	Daily_Data<scalar>& operator[]
		(int i ///< Index.
		) { return data[i]; }
private:
	std::vector<Daily_Data<scalar>> data; ///< The data.
};

} // end namespace ddi

#include "core.ipp"

#endif // DDI__core_hpp__INCLUDED
