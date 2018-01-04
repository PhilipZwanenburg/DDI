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
#ifndef DDI__macros_hpp__INCLUDED
#define DDI__macros_hpp__INCLUDED
/** \file
 *  \brief Defines macros.
 */

/** \brief Macro to silence `unused variable` compile warning.
 *
 *  Taken from [this SO answer][SO_unused].
 *
 *  <!-- References: -->
 *  [SO_unused]: https://stackoverflow.com/questions/1486904/how-do-i-best-silence-a-warning-about-unused-variables
 */
#define UNUSED(expr) do { (void)(expr); } while (0)

#endif // DDI__macros_hpp__INCLUDED
