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
# Copyright 2017-2023 Patrick Lehmann - Bötzingen, Germany                                                             #
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
__author__ =        "Patrick Lehmann"
__email__ =         "Paebbels@gmail.com"
__copyright__ =     "2017-2023, Patrick Lehmann"
__license__ =       "Apache License, Version 2.0"
__version__ =       "0.1.0"
__keywords__ =      ["dummy"]
__issue_tracker__ = "https://GitHub.com/pyTooling/Actions/issues"

from pyTooling.Decorators import export


@export
class Application:
	_value: int

	def __init__(self) -> None:
		self._value = 1

	@property
	def Value(self) -> int:
		return self._value
