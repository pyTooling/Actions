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
# Copyright 2017-2026 Patrick Lehmann - Bötzingen, Germany                                                             #
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
from importlib.metadata import version as get_version
from json               import loads as json_loads, JSONDecodeError
from re                 import IGNORECASE, MULTILINE
from shutil             import which
from subprocess import CompletedProcess, run as subprocess_run, TimeoutExpired
from sys                import executable as PYTHON_EXECUTABLE
from tempfile           import TemporaryDirectory
from typing             import ClassVar
from unittest           import TestCase


class Testcase(TestCase):
	"""
	Shared base class: resolves the installed console_scripts executable
	once per test class and provides a subprocess-invocation helper.
	"""

	ENTRY_POINT_NAME: ClassVar[str] = "myPackage"
	executable: str

	@classmethod
	def setUpClass(cls) -> None:
		if (resolved := which(cls.ENTRY_POINT_NAME)) is None:
			raise RuntimeError(
				f"'{cls.ENTRY_POINT_NAME}' not found on PATH. Verify the wheel "
				f"was installed in this environment and that setup.py's "
				f"entry_points {{'console_scripts': "
				f"['{cls.ENTRY_POINT_NAME}=myPackage.CLI:main']}} was picked "
				f"up correctly."
			)
		cls.executable = resolved

	def RunEntrypoint(
		self,
		*args: str,
		timeout: float = 10.0,
		input_text: str | None = None,
		env: dict | None = None,
		cwd: str | None = None,
	) -> CompletedProcess:
		return subprocess_run(
			[self.executable, *args],
			capture_output=True,
			text=True,
			timeout=timeout,
			input=input_text,
			env=env,
			cwd=cwd,
		)

	def RunModule(self, *args: str, timeout: float = 10.0) -> CompletedProcess:
		"""
		Invokes `python -m myPackage.CLI` directly, bypassing the
		console_scripts shim. Use to isolate whether a failure originates
		in the entry-point wiring vs. the CLI logic itself.
		"""
		return subprocess_run(
			[PYTHON_EXECUTABLE, "-m", "myPackage.CLI", *args],
			capture_output=True,
			text=True,
			timeout=timeout,
		)

	def assertExitCode(self, result: CompletedProcess, expected: int) -> None:
		self.assertEqual(
			expected,
			result.returncode,
			msg=(
				f"args={result.args!r}\n"
				f"--- stdout ---\n{result.stdout}\n"
				f"--- stderr ---\n{result.stderr}"
			),
		)


class Basic(Testcase):
	def test_NoArguments(self) -> None:
		result = self.RunEntrypoint()
		self.assertExitCode(result, 0)
