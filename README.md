# Welcome to Data-Driven Investing!

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
		<!-- <th> -->
		<!-- 	<a href="https://codecov.io/gh/PhilipZwanenburg/DDI/branch/master"> -->
		<!-- 		<img src="https://codecov.io/gh/PhilipZwanenburg/DDI/branch/master/graph/badge.svg" -->
		<!-- 		     title="coverage"> -->
		<!-- 	</a> -->
		<!-- </th> -->
		<!-- <th> -->
		<!-- 	<a href="https://codedocs.xyz/PhilipZwanenburg/DDI/"> -->
		<!-- 		<img src="https://codedocs.xyz/PhilipZwanenburg/DDI.svg" -->
		<!-- 		     title="documentation"> -->
		<!-- 	</a> -->
		<!-- </th> -->
	</tr>
</table>


## Objectives

The objectives of the project are twofold.

### Learning Platform

First, the project serves as a learning platform for:
- Coding workflow practices relying on the following external projects:
    - Sphinx (Python documentation)
    - TravisCI (Continuous integration for build verification and code coverage analysis);
- Library usage:
	- TensorFlow (Machine Learning);

### Practical Contribution

Second, the project of course has the goal of doing something of practical value! In this case, this
relates to the development of models for profitable investment trading strategies.

The **primary** goal is to develop a model for trading behaviour of **low-risk** Exchange-Traded
Funds (ETFs) such that they make a comparable or greater profit than holding a market-indexed ETF
(such as an S&P 500-indexed ETF, e.g. XUS) during a bull market.  This will ideally result in
significantly reduced exposure to financial market volatily during periods of recession while still
making comparable profits. The model should be validated by correctly predicting appropriate trading
behaviour at a "future" time based on a subset of past ETF data. For example, given the past 10
years of trading data for an ETF, build a model for future trading based on the first 8 years of
data data and verify that a profitable trading strategy is adopted for the remaining time.


If the primary goal is accomplished, the following secondary goals may be pursued:
- Interaction between several low-risk ETFs with the same strategy;
- Expansion of the model to high-risk ETFs with comparison of model performance with training on
  ETFs having differing risk levels (e.g. training on all risk levels vs only low-risk and comparing
  profit performance when used for various risk categories).

The investment strategy developed in this project is designed for investors with the following characteristics:
- Small scale: The model assumes that the investor's trading decisions have a negligible effect on the market.
- Access to zero/low fee ETF trading: The model assumes that trading costs are negligible.

#### Example Result

/// \todo Add result when available.

---


## Running the Code

The code has been succesfully run in the following environment(s):
- linux (ubuntu 16.04);

### Running the Code

Please follow the format of the targets provided in the [Makefile](Makefile) in order to run the
scripts responsible for various functionality of this project.

### Testing

/// \todo Update after adding tests.

#### Understanding the Code

/// \todo Update after adding tests.
<!-- Unit and integration tests may be considered to be minimal working examples demonstrating code functionality. -->

---


## License

The code is licensed under the [GNU GPLv3](LICENSE.md).
