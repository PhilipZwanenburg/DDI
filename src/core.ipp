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

#include <vector>
#include <string>
#include <fstream>

#include "macros.hpp"

namespace ddi {

// Static function declarations ***************************************************************** //

/** \brief Return the next quote delimited entry in the input stream as a string.
 *  \return See brief. */
static std::string read_string
	(std::istream& is ///< Input stream.
	);

/** \brief Return the next quote delimited entry in the input stream as a scalar.
 *  \return See brief. */
template<typename scalar>
static scalar read_scalar
	(std::istream& is ///< Input stream.
	);

/// \brief Skip the input number of lines in the input stream.
static void skip_lines
	(std::istream& is, ///< Input stream.
	 const int n_skip  ///< Number of lines to skip.
	);

// Interface functions ************************************************************************** //

template<typename scalar_>
std::istream& operator>>(std::istream& is, Daily_Data<scalar_>& dd)
{
	dd.date   = read_string(is);
	dd.close  = read_scalar<scalar_>(is);
	dd.volume = read_scalar<int>(is);
	dd.open   = read_scalar<scalar_>(is);
	dd.high   = read_scalar<scalar_>(is);
	dd.low    = read_scalar<scalar_>(is);

	return is;
}

template<typename scalar_>
std::ostream& operator<<(std::ostream& os, const Daily_Data<scalar_>& dd)
{
	return os << "{" << '\n'
	          << "date:   " << "\"" << dd.date << "\"" << ",\n"
	          << "open:   " << dd.open                 << ",\n"
	          << "close:  " << dd.close                << ",\n"
	          << "low:    " << dd.low                  << ",\n"
	          << "high:   " << dd.high                 << ",\n"
	          << "volume: " << dd.volume               << ",\n"
	          << "}" << '\n';
}

template<typename scalar>
ETF_Data<scalar>::ETF_Data (std::ifstream& ifs)
{
	skip_lines(ifs,2);
	while (true) {
		ddi::Daily_Data<scalar> dd;
		if (!(ifs >> dd))
			break;

		data.push_back(dd);
	}
}

template<typename scalar>
void ETF_Data<scalar>::push_back_data (const Daily_Data<scalar>& dd)
{
	data.push_back(dd);
}

// Level 0 ************************************************************************************** //

/// \brief Advance the input stream to one beyond the next input character.
static void advance_past_char
	(std::istream& is,  ///< Input stream.
	 const char char_i  ///< The input character.
	);

static std::string read_string (std::istream& is)
{
	advance_past_char(is,'"');

	char ch;
	std::string str;
	while (is >> ch && ch != '"')
		str += ch;
	return str;
}

template<typename scalar>
static scalar read_scalar (std::istream& is)
{
	advance_past_char(is,'"');

	scalar val;
	is >> val;

	advance_past_char(is,'"');

	return val;
}

static void skip_lines (std::istream& is, const int n_skip)
{
    std::string str;
    for (int i = 0; i < n_skip; ++i)
        std::getline(is,str);
}

// Level 1 ************************************************************************************** //

static void advance_past_char (std::istream& is, const char char_i)
{
	char ch;
	while (is >> ch) {
		if (ch == char_i)
			break;
	}
}

} // end namespace ddi
