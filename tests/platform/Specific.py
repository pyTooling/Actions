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
from unittest           import TestCase

from pytest             import mark
from pyTooling.Platform import CurrentPlatform

from myPackage          import Application


if __name__ == "__main__":  # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unittest <testcase module>'")
	exit(1)


class PlatformTesting(TestCase):
	@mark.skipif(not CurrentPlatform.IsNativeLinux, reason="Skipped, if current platform isn't native Linux.")
	def test_ApplicationOnNativeLinux(self):
		app = Application()

		self.assertEqual(1, app.Value)

	@mark.skipif(not CurrentPlatform.IsNativeMacOS, reason="Skipped, if current platform isn't native macOS.")
	def test_ApplicationOnNativeMacOS(self):
		app = Application()

		self.assertEqual(2, app.Value)

	@mark.skipif(not CurrentPlatform.IsNativeWindows, reason="Skipped, if current platform isn't native Windows.")
	def test_ApplicationOnNativeWindows(self):
		app = Application()

		self.assertEqual(3, app.Value)

	@mark.skipif(not CurrentPlatform.IsMSYSOnWindows, reason="Skipped, if current platform isn't MSYS on Windows.")
	def test_ApplicationOnMSYS2OnWindows(self):
		app = Application()

		self.assertEqual(11, app.Value)

	@mark.skipif(not CurrentPlatform.IsMinGW32OnWindows, reason="Skipped, if current platform isn't MinGW32 on Windows.")
	def test_ApplicationOnMinGW32OnWindows(self):
		app = Application()

		self.assertEqual(12, app.Value)

	@mark.skipif(not CurrentPlatform.IsMinGW64OnWindows, reason="Skipped, if current platform isn't MinGW64 on Windows.")
	def test_ApplicationOnMinGW64OnWindows(self):
		app = Application()

		self.assertEqual(13, app.Value)

	@mark.skipif(not CurrentPlatform.IsUCRT64OnWindows, reason="Skipped, if current platform isn't UCRT64 on Windows.")
	def test_ApplicationOnURTC64OnWindows(self):
		app = Application()

		self.assertEqual(14, app.Value)

	@mark.skipif(not CurrentPlatform.IsClang32OnWindows, reason="Skipped, if current platform isn't Clang32 on Windows.")
	def test_ApplicationOnClang32OnWindows(self):
		app = Application()

		self.assertEqual(15, app.Value)

	@mark.skipif(not CurrentPlatform.IsClang64OnWindows, reason="Skipped, if current platform isn't Clang64 on Windows.")
	def test_ApplicationOnClang64OnWindows(self):
		app = Application()

		self.assertEqual(16, app.Value)
