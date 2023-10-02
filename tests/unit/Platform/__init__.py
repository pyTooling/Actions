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
"""Unit tests for TBD."""
from os       import getenv as os_getenv
from pytest   import mark
from unittest import TestCase

from pyTooling.Platform import Platform


if __name__ == "__main__":  # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class AnyPlatform(TestCase):
	expected = os_getenv("ENVIRONMENT_NAME", default="Windows (x86-64)")

	@mark.skipif(os_getenv("ENVIRONMENT_NAME", "skip") == "skip", reason="Skipped when environment variable 'ENVIRONMENT_NAME' isn't set.")
	def test_PlatformString(self) -> None:
		platform = Platform()

		print()
		print(platform)

	@mark.skipif("Linux (x86-64)" != os_getenv("ENVIRONMENT_NAME", "skip"), reason=f"Skipped 'test_NativeLinux' when environment variable 'ENVIRONMENT_NAME' doesn't match. {os_getenv('ENVIRONMENT_NAME', 'skip')}")
	def test_NativeLinux(self) -> None:
		platform = Platform()

		print()
		print(platform)

	@mark.skipif("MacOS (x86-64)" != os_getenv("ENVIRONMENT_NAME", "skip"), reason=f"Skipped 'test_NativeMacOS' when environment variable 'ENVIRONMENT_NAME' doesn't match. {os_getenv('ENVIRONMENT_NAME', 'skip')}")
	def test_NativeMacOS(self) -> None:
		platform = Platform()

		print()
		print(platform)

	@mark.skipif("Windows (x86-64)" != os_getenv("ENVIRONMENT_NAME", "skip"), reason=f"Skipped 'test_NativeWindows' when environment variable 'ENVIRONMENT_NAME' doesn't match. {os_getenv('ENVIRONMENT_NAME', 'skip')}")
	def test_NativeWindows(self) -> None:
		platform = Platform()

		print()
		print(platform)

	@mark.skipif("Windows+MSYS2 (x86-64) - MSYS" != os_getenv("ENVIRONMENT_NAME", "skip"), reason=f"Skipped 'test_MSYS' when environment variable 'ENVIRONMENT_NAME' doesn't match. {os_getenv('ENVIRONMENT_NAME', 'skip')}")
	def test_MSYS(self) -> None:
		platform = Platform()

		print()
		print(platform)

	@mark.skipif("Windows+MSYS2 (x86-64) - MinGW32" != os_getenv("ENVIRONMENT_NAME", "skip"), reason=f"Skipped 'test_MinGW32' when environment variable 'ENVIRONMENT_NAME' doesn't match. {os_getenv('ENVIRONMENT_NAME', 'skip')}")
	def test_MinGW32(self) -> None:
		platform = Platform()

		print()
		print(platform)

	@mark.skipif("Windows+MSYS2 (x86-64) - MinGW64" != os_getenv("ENVIRONMENT_NAME", "skip"), reason=f"Skipped 'test_MinGW64' when environment variable 'ENVIRONMENT_NAME' doesn't match. {os_getenv('ENVIRONMENT_NAME', 'skip')}")
	def test_MinGW64(self) -> None:
		platform = Platform()

		print()
		print(platform)

	@mark.skipif("Windows+MSYS2 (x86-64) - UCRT64" != os_getenv("ENVIRONMENT_NAME", "skip"), reason=f"Skipped 'test_UCRT64' when environment variable 'ENVIRONMENT_NAME' doesn't match. {os_getenv('ENVIRONMENT_NAME', 'skip')}")
	def test_UCRT64(self) -> None:
		platform = Platform()

		print()
		print(platform)

	@mark.skipif("Windows+MSYS2 (x86-64) - Clang32" != os_getenv("ENVIRONMENT_NAME", "skip"), reason=f"Skipped 'test_Clang32' when environment variable 'ENVIRONMENT_NAME' doesn't match. {os_getenv('ENVIRONMENT_NAME', 'skip')}")
	def test_Clang32(self) -> None:
		platform = Platform()

		print()
		print(platform)

	@mark.skipif("Windows+MSYS2 (x86-64) - Clang64" != os_getenv("ENVIRONMENT_NAME", "skip"), reason=f"Skipped 'test_Clang64' when environment variable 'ENVIRONMENT_NAME' doesn't match. {os_getenv('ENVIRONMENT_NAME', 'skip')}")
	def test_Clang64(self) -> None:
		platform = Platform()

		print()
		print(platform)
