from os import getenv
from pathlib import Path
from re import compile
from sys import version

print(f"Python: {version}")


def loadRequirementsFile(requirementsFile: Path):
	requirements = []
	with requirementsFile.open("r") as file:
		for line in file.readlines():
			line = line.strip()
			if line.startswith("#") or line.startswith("https") or line == "":
				continue
			elif line.startswith("-r"):
				# Remove the first word/argument (-r)
				requirements += loadRequirementsFile(requirementsFile.parent / line[2:].lstrip())
			else:
				requirements.append(line)

	return requirements


requirements = "-r ../tests/requirements.txt"
if requirements.startswith("-r"):
	requirementsFile = Path(requirements[2:].lstrip())
	dependencies = loadRequirementsFile(requirementsFile)
else:
	dependencies = [req.strip() for req in requirements.split(" ")]

packages = {
	"coverage": "python-coverage:p",
	"igraph": "igraph:p",
	"jinja2": "python-markupsafe:p",
	"lxml": "python-lxml:p",
	"numpy": "python-numpy:p",
	"markupsafe": "python-markupsafe:p",
	"pip": "python-pip:p",
	"ruamel.yaml": "python-ruamel-yaml:p python-ruamel.yaml.clib:p",
	"sphinx": "python-markupsafe:p",
	"tomli": "python-tomli:p",
	"wheel": "python-wheel:p",
	"pyEDAA.ProjectModel": "python-ruamel-yaml:p python-ruamel.yaml.clib:p python-lxml:p",
	"pyEDAA.Reports": "python-ruamel-yaml:p python-ruamel.yaml.clib:p python-lxml:p",
}
subPackages = {
	"pytooling": {
		"yaml": "python-ruamel-yaml:p python-ruamel.yaml.clib:p",
	},
}

regExp = compile(
	r"(?P<PackageName>[\w_\-\.]+)(?:\[(?P<SubPackages>(?:\w+)(?:\s*,\s*\w+)*)\])?(?:\s*(?P<Comperator>[<>~=]+)\s*)(?P<Version>\d+(?:\.\d+)*)(?:-(?P<VersionExtension>\w+))?")

pacboyPackages = set(("python-pip:p", "python-wheel:p", "python-tomli:p"))
print(f"Processing dependencies ({len(dependencies)}):")
for dependency in dependencies:
	print(f"  {dependency}")

	match = regExp.match(dependency.lower())
	if not match:
		print(f"    Wrong format: {dependency}")
		print(f"::error title=Identifying Pacboy Packages::Unrecognized dependency format '{dependency}'")
		continue

	package = match["PackageName"]
	if package in packages:
		rewrite = packages[package]
		print(f"    Found rewrite rule for '{package}': {rewrite}")
		pacboyPackages.add(rewrite)

	if match["SubPackages"] and package in subPackages:
		for subPackage in match["SubPackages"].split(","):
			if subPackage in subPackages[package]:
				rewrite = subPackages[package][subPackage]
				print(f"    Found rewrite rule for '{package}[..., {subPackage}, ...]': {rewrite}")
				pacboyPackages.add(rewrite)

# Write jobs to special file
# github_output = Path(getenv("GITHUB_OUTPUT"))
# print(f"GITHUB_OUTPUT: {github_output}")
# with github_output.open("a+") as f:
# 	f.write(f"pacboy_packages={' '.join(pacboyPackages)}\n")

print(f"GITHUB_OUTPUT:")
print(f"pacboy_packages={' '.join(pacboyPackages)}\n")
