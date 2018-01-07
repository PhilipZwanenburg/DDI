# Welcome to (D)ata-(D)riven (I)nvesting!

<table>
	<tr>
		<th>Branch</th>
		<th>Version</th>
		<th>Linux</th>
		<th>Coverage</th>
		<th>Documentation</th>
	</tr>
	<tr>
		<th>
			<a href="https://github.com/PhilipZwanenburg/DDI/tree/master">
				master
			</a>
		</th>
		<th>
			<a href="https://badge.fury.io/">
				<img src="https://badge.fury.io/gh/PhilipZwanenburg%2FDDI.svg"
				     title="version">
			</a>
		</th>
		<th>
			<a href="https://travis-ci.org/PhilipZwanenburg/DDI">
				<img src="https://travis-ci.org/PhilipZwanenburg/DDI.svg?branch=master"
				     title="build status">
			</a>
		</th>
		<th>
			<a href="https://codecov.io/gh/PhilipZwanenburg/DDI/branch/master">
				<img src="https://codecov.io/gh/PhilipZwanenburg/DDI/branch/master/graph/badge.svg"
				     title="coverage">
			</a>
		</th>
		<th>
			<a href="https://codedocs.xyz/PhilipZwanenburg/DDI/">
				<img src="https://codedocs.xyz/PhilipZwanenburg/DDI.svg"
				     title="documentation">
			</a>
		</th>
	</tr>
</table>


## Objectives

The objectives of the project are twofold.

### Learning Platform

First, the project serves as a learning platform for:
- Modern coding practices focusing on the exploration of modern c++ features;
- Coding workflow practices relying on the following external projects:
	- CMake/CTest (Facilitating project building and test generation);
	- Doxygen (Documentation);
	- TravisCI (Continuous integration for build verification and code coverage analysis);
- Library usage:
	- TensorFlow (Machine Learning);

Please consult the Doxygen documentation mainpage for the list of supporting software incorporated
in accordance with the fulfillment of these objectives.

### Practical Contribution

Second, the project of course has the goal of doing something of practical value! In this case, this
relates to the development of models for profitable investment trading strategies.

The **primary** goal is to develop a model for trading behaviour of **low-risk** Exchange-Traded
Funds (ETFs) such that they make a comparable or greater profit than holding a market-indexed ETF
(such as an S&P 500-indexed ETF, e.g. XUS) during a bull market.  This will ideally result in
significantly reduced exposure to financial market volatily during periods of recession while still
making comparable profits. The model should be validated by correctly predicting appropriate trading
behaviour at a "future" time based on a subset of past ETF data. For example, given the past 10
years of trading data for an ETF, build a model for future trading based on the first 5-8 years of
data and verify that a profitable trading strategy is adopted for the remaining time.

If the primary goal is accomplished, the following secondary goals may be pursued:
- Interaction between several low-risk ETFs with the same strategy;
- Expansion of the model to high-risk ETFs with comparison of model performance with training on
  ETFs having differing risk levels (e.g. training on all risk levels vs only low-risk and comparing
  profit performance when used for various risk categories).

The investment strategy developed in this project is designed for investors with the following
characteristics:
- Small scale: The model assumes that the investor's trading decisions have a negligible effect on
  the market.
- Access to zero/low fee ETF trading: The model assumes that trading costs are negligible.

Financial data has been obtained from [nasdaq.com](http://www.nasdaq.com/symbol).

#### Example Result

/** \todo Add result when available. */

---


## Building/Running the Code

The code has been succesfully built in the following environment(s):
- linux (ubuntu 16.04);

### Build using CMake

An out-of-source build **must** be performed using the appropriate [python script](cmake/run). For
example, to configure for the debug/gcc build for ubuntu:
```sh
$ ROOT/cmake/run$ python3 ubuntu16-04.py debug gcc
```

**Additional cmake command line inputs may be required** if CMake is unable to locate required
software which you are sure is installed; CMake will exit with an error if required software is not
found. It is recommended to use a standard package manager for installing missing software whenever
possible (e.g. `apt` on ubuntu) to limit package conflicts and place installed software in
directories in the default search path.

### Compile using Make

Once the code has been successfully built, the available `make` targets can be seen using
```sh
BUILD$ make help
```

Of primary interest are the following:
```sh
BUILD$ make     // Compile the code.
BUILD$ make doc // Generate the Doxygen documentation.
```

The html documentation can be accessed by pointing a browser at `BUILD/doc/html/index.html`. For
example:
```sh
BUILD/doc/html$ firefox index.html
```

### Running the Code

/** \todo Modify after implementing. Use python script files. */

### Testing

Testing can be performed using CMake's `ctest` functionality. After successfully compiling the
project, all tests can be run by executing:
```sh
BUILD$ ctest // This is equivalent to BUILD$ make test
```

Additional useful commands are:
```sh
BUILD$ ctest -N (List the tests that would be run but not actually run them)
BUILD$ ctest -R <regex> (Run tests matching regular expression)
BUILD$ ctest -V (Enable verbose output from tests)
```

#### Understanding the Code

Unit and integration tests may be considered to be minimal working examples demonstrating code
functionality.

---


## License

The code is licensed under the [GNU GPLv3](LICENSE.md).
