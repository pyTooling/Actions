# ==================================================================================================================== #
#             _____           _ _                  _        _   _                                                      #
#  _ __  _   |_   _|__   ___ | (_)_ __   __ _     / \   ___| |_(_) ___  _ __  ___                                      #
# | '_ \| | | || |/ _ \ / _ \| | | '_ \ / _` |   / _ \ / __| __| |/ _ \| '_ \/ __|                                     #
# | |_) | |_| || | (_) | (_) | | | | | | (_| |_ / ___ \ (__| |_| | (_) | | | \__ \                                     #
# | .__/ \__, ||_|\___/ \___/|_|_|_| |_|\__, (_)_/   \_\___|\__|_|\___/|_| |_|___/                                     #
# |_|    |___/                          |___/                                                                          #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2017-2025 Patrick Lehmann - Bötzingen, Germany                                                             #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
"""
A module for a set of dummy classes.
"""

__author__ =        "Patrick Lehmann"
__email__ =         "Paebbels@gmail.com"
__copyright__ =     "2017-2025, Patrick Lehmann"
__license__ =       "Apache License, Version 2.0"
__version__ =       "7.2.0"
__keywords__ =      ["GitHub Actions"]
__issue_tracker__ = "https://GitHub.com/pyTooling/Actions/issues"

from pickle               import dumps
from subprocess           import check_call

from pyTooling.Decorators import export, readonly
from pyTooling.Platform   import Platform


@export
class Base:
	"""
	A base-class for dummy applications.
	"""

	_value: int    #: An internal value.

	def __init__(self) -> None:
		# """
		# Initializes the base-class.
		# """
		self._value = 0

	@readonly
	def Value(self) -> int:
		"""
		Read-only property to return the internal value.

		:return: Internal value.
		"""
		return self._value

	def Add(self, value) -> None:
		"""
		Accumulate value to internal value.

		:param value: Value to accumulate.
		"""
		self._value += value


@export
class Application(Base):
	"""
	A dummy application for demonstration purposes.
	"""

	def __init__(self) -> None:
		# """
		# Initializes the dummy application.
		# """
		super().__init__()

		platform = Platform()
		# pylint: disable=using-constant-test
		if platform.IsNativeLinux:
			self._value += 1
		elif platform.IsNativeMacOS:
			self._value += 2
		elif platform.IsNativeWindows:
			self._value += 3
		elif platform.IsMSYSOnWindows:
			self._value += 11
		elif platform.IsMinGW32OnWindows:
			self._value += 12
		elif platform.IsMinGW64OnWindows:
			self._value += 13
		elif platform.IsUCRT64OnWindows:
			self._value += 14
		elif platform.IsClang32OnWindows:
			self._value += 15
		elif platform.IsClang64OnWindows:
			self._value += 16
