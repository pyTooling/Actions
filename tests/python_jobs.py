from json import dumps as json_dumps
from os import getenv
from pathlib import Path
from textwrap import dedent

name = "example".strip()
python_version = "3.12".strip()
systems = "ubuntu windows macos mingw64 ucrt64".strip()
versions = "3.8 3.9 3.10 3.11 3.12".strip()
include_list = "".strip()
exclude_list = "".strip()
disable_list = "".strip()

currentMSYS2Version = "3.11"
currentAlphaVersion = "3.13"
currentAlphaRelease = "3.13.0-alpha.1"

if systems == "":
	print("::error title=Parameter::system_list is empty.")
else:
	systems = [sys.strip() for sys in systems.split(" ")]

if versions == "":
	versions = [python_version]
else:
	versions = [ver.strip() for ver in versions.split(" ")]

if include_list == "":
	includes = []
else:
	includes = [tuple(include.strip().split(":")) for include in include_list.split(" ")]

if exclude_list == "":
	excludes = []
else:
	excludes = [exclude.strip() for exclude in exclude_list.split(" ")]

if disable_list == "":
	disabled = []
else:
	disabled = [disable.strip() for disable in disable_list.split(" ")]

if "3.7" in versions:
	print("::warning title=Deprecated::Support for Python 3.7 ended in 2023.06.27.")
if "msys2" in systems:
	print("::warning title=Deprecated::System 'msys2' will be replaced by 'mingw64'.")
if currentAlphaVersion in versions:
	print(f"::notice title=Experimental::Python {currentAlphaVersion} ({currentAlphaRelease}) is a pre-release.")
for disable in disabled:
	print(f"::warning title=Disabled Python Job::System '{disable}' temporarily disabled.")

# see https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json
data = {
	# Python and PyPy versions supported by "setup-python" action
	"python": {
		"3.7": {"icon": "⚫", "until": "2023.06.27"},
		"3.8": {"icon": "🔴", "until": "2024.10"},
		"3.9": {"icon": "🟠", "until": "2025.10"},
		"3.10": {"icon": "🟡", "until": "2026.10"},
		"3.11": {"icon": "🟢", "until": "2027.10"},
		"3.12": {"icon": "🟢", "until": "2028.10"},
		#  "3.13":      { "icon": "🟣",  "until": "2028.10" },
		"pypy-3.7": {"icon": "⟲⚫", "until": "????.??"},
		"pypy-3.8": {"icon": "⟲🔴", "until": "????.??"},
		"pypy-3.9": {"icon": "⟲🟠", "until": "????.??"},
		"pypy-3.10": {"icon": "⟲🟡", "until": "????.??"},
	},
	# Runner systems (runner images) supported by GitHub Actions
	"sys": {
		"ubuntu": {"icon": "🐧", "runs-on": "ubuntu-latest", "shell": "bash", "name": "Linux (x86-64)"},
		"windows": {"icon": "🪟", "runs-on": "windows-latest", "shell": "pwsh", "name": "Windows (x86-64)"},
		"macos": {"icon": "🍎", "runs-on": "macos-latest", "shell": "bash", "name": "MacOS (x86-64)"},
	},
	# Runtimes provided by MSYS2
	"runtime": {
		"msys": {"icon": "🪟🟪", "name": "Windows+MSYS2 (x86-64) - MSYS"},
		"mingw32": {"icon": "🪟⬛", "name": "Windows+MSYS2 (x86-64) - MinGW32"},
		"mingw64": {"icon": "🪟🟦", "name": "Windows+MSYS2 (x86-64) - MinGW64"},
		"clang32": {"icon": "🪟🟫", "name": "Windows+MSYS2 (x86-64) - Clang32"},
		"clang64": {"icon": "🪟🟧", "name": "Windows+MSYS2 (x86-64) - Clang64"},
		"ucrt64": {"icon": "🪟🟨", "name": "Windows+MSYS2 (x86-64) - UCRT64"},
	}
}

print(f"includes ({len(includes)}):")
for system, version in includes:
	print(f"- {system}:{version}")
print(f"excludes ({len(excludes)}):")
for exclude in excludes:
	print(f"- {exclude}")
print(f"disabled ({len(disabled)}):")
for disable in disabled:
	print(f"- {disable}")

combinations = [
								 (system, version)
								 for system in systems
								 if system in data["sys"]
								 for version in versions
								 if version in data["python"]
										and f"{system}:{version}" not in excludes
										and f"{system}:{version}" not in disabled
							 ] + [
								 (system, currentMSYS2Version)
								 for system in systems
								 if system in data["runtime"]
										and f"{system}:{currentMSYS2Version}" not in excludes
										and f"{system}:{currentMSYS2Version}" not in disabled
							 ] + [
								 (system, version)
								 for system, version in includes
								 if system in data["sys"]
										and version in data["python"]
										and f"{system}:{version}" not in disabled
							 ]
print(f"Combinations ({len(combinations)}):")
for system, version in combinations:
	print(f"- {system}:{version}")

jobs = [
				 {
					 "sysicon": data["sys"][system]["icon"],
					 "system": system,
					 "runs-on": data["sys"][system]["runs-on"],
					 "runtime": "native",
					 "shell": data["sys"][system]["shell"],
					 "pyicon": data["python"][version]["icon"],
					 "python": currentAlphaRelease if version == currentAlphaVersion else version,
					 "envname": data["sys"][system]["name"],
				 }
				 for system, version in combinations if system in data["sys"]
			 ] + [
				 {
					 "sysicon": data["runtime"][runtime]["icon"],
					 "system": "msys2",
					 "runs-on": "windows-latest",
					 "runtime": runtime.upper(),
					 "shell": "msys2 {0}",
					 "pyicon": data["python"][currentMSYS2Version]["icon"],
					 "python": version,
					 "envname": data["runtime"][runtime]["name"],
				 }
				 for runtime, version in combinations if runtime not in data["sys"]
			 ]

artifact_names = {
	"unittesting_xml": f"{name}-UnitTestReportSummary-XML",
	"unittesting_html": f"{name}-UnitTestReportSummary-HTML",
	"perftesting_xml": f"{name}-PerformanceTestReportSummary-XML",
	"benchtesting_xml": f"{name}-BenchmarkTestReportSummary-XML",
	"apptesting_xml": f"{name}-ApplicationTestReportSummary-XML",
	"codecoverage_sqlite": f"{name}-CodeCoverage-SQLite",
	"codecoverage_xml": f"{name}-CodeCoverage-XML",
	"codecoverage_json": f"{name}-CodeCoverage-JSON",
	"codecoverage_html": f"{name}-CodeCoverage-HTML",
	"statictyping_html": f"{name}-StaticTyping-HTML",
	"package_all": f"{name}-Packages",
	"documentation_html": f"{name}-Documentation-HTML",
	"documentation_latex": f"{name}-Documentation-LaTeX",
	"documentation_pdf": f"{name}-Documentation-PDF",
}

# Deprecated structure
params = {
	"python_version": python_version,
	"artifacts": {
		"unittesting": f"{artifact_names['unittesting_xml']}",
		"coverage": f"{artifact_names['codecoverage_html']}",
		"typing": f"{artifact_names['statictyping_html']}",
		"package": f"{artifact_names['package_all']}",
		"doc": f"{artifact_names['documentation_html']}",
	}
}

print("Parameters:")
print(f"  python_version: {python_version}")
print(f"  python_jobs ({len(jobs)}):\n" +
			"".join(
				[f"    {{ " + ", ".join([f"\"{key}\": \"{value}\"" for key, value in job.items()]) + f" }},\n" for job in jobs])
			)
print(f"  artifact_names ({len(artifact_names)}):")
for id, name in artifact_names.items():
	print(f"    {id:>20}: {name}")

# Write jobs to special file
github_output = Path(getenv("GITHUB_OUTPUT"))
print(f"GITHUB_OUTPUT: {github_output}")
with github_output.open("a+", encoding="utf-8") as f:
	f.write(dedent(f"""\
    python_version={python_version}
    python_jobs={json_dumps(jobs)}
    artifact_names={json_dumps(artifact_names)}
    params={json_dumps(params)}
"""))
