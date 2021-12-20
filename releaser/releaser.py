#!/usr/bin/env python3
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#   Unai Martinez-Corral                                                                                               #
#                                                                                                                      #
# ==================================================================================================================== #
# Copyright 2020-2021 The pyTooling Authors                                                                            #
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
import re
from sys import argv as sys_argv, stdout, exit as sys_exit
from os import environ, getenv
from glob import glob
from pathlib import Path
from github import Github, GithubException
from subprocess import check_call


paramTag = getenv("INPUT_TAG", "tip")
paramFiles = getenv("INPUT_FILES", None).split()
paramRM = getenv("INPUT_RM", "false") == "true"
paramSnapshots = getenv("INPUT_SNAPSHOTS", "true").lower() == "true"
paramToken = (
    environ["GITHUB_TOKEN"]
    if "GITHUB_TOKEN" in environ
    else environ["INPUT_TOKEN"]
    if "INPUT_TOKEN" in environ
    else None
)
paramRepo = getenv("GITHUB_REPOSITORY", None)
paramRef = getenv("GITHUB_REF", None)
paramSHA = getenv("GITHUB_SHA", None)


def GetListOfArtifacts(argv, files):
    print("· Get list of artifacts to be uploaded")
    args = files if files is not None else []
    if len(argv) > 1:
        args += argv[1:]
    if len(args) == 1 and args[0].lower() == "none":
        print("! Skipping 'files' because it's set to 'none")
        return []
    elif len(args) == 0:
        stdout.flush()
        raise (Exception("Glob patterns need to be provided as positional arguments or through envvar 'INPUT_FILES'!"))
    else:
        flist = []
        for item in args:
            print(f"  glob({item!s}):")
            for fname in [fname for fname in glob(item, recursive=True) if not Path(fname).is_dir()]:
                if Path(fname).stat().st_size == 0:
                    print(f"  - ! Skipping empty file {fname!s}")
                    continue
                print(f"  - {fname!s}")
                flist.append(fname)
        if len(flist) < 1:
            stdout.flush()
            raise (Exception("Empty list of files to upload/update!"))
        return flist


def GetGitHubAPIHandler(token):
    print("· Get GitHub API handler (authenticate)")
    if token is not None:
        return Github(token)
    raise (Exception("Need credentials to authenticate! Please, provide 'GITHUB_TOKEN' or 'INPUT_TOKEN'"))


def CheckRefSemVer(gh_ref, tag, snapshots):
    print("· Check SemVer compliance of the reference/tag")
    env_tag = None
    if gh_ref[0:10] == "refs/tags/":
        env_tag = gh_ref[10:]
        if env_tag != tag:
            rexp = r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
            semver = re.search(rexp, env_tag)
            if semver == None and env_tag[0] == "v":
                semver = re.search(rexp, env_tag[1:])
            tag = env_tag
            if semver == None:
                print(f"! Could not get semver from {gh_ref!s}")
                print(f"! Treat tag '{tag!s}' as a release")
                return (tag, env_tag, False)
            else:
                if semver.group("prerelease") is None:
                    # is a regular semver compilant tag
                    return (tag, env_tag, False)
                elif snapshots:
                    # is semver compilant prerelease tag, thus a snapshot (we skip it)
                    print("! Skipping snapshot prerelease")
                    sys_exit()

    return (tag, env_tag, True)


def GetRepositoryHandler(gh, repo):
    print("· Get Repository handler")
    if repo is None:
        stdout.flush()
        raise (Exception("Repository name not defined! Please set 'GITHUB_REPOSITORY"))
    return gh.get_repo(repo)


def GetOrCreateRelease(gh_repo, tag, sha, is_prerelease):
    print("· Get Release handler")
    gh_tag = None
    try:
        gh_tag = gh_repo.get_git_ref(f"tags/{tag!s}")
    except Exception:
        stdout.flush()

    if gh_tag:
        try:
            return (gh_repo.get_release(tag), False)
        except Exception:
            return (gh_repo.create_git_release(tag, tag, "", draft=True, prerelease=is_prerelease), True)
    else:
        err_msg = f"Tag/release '{tag!s}' does not exist and could not create it!"
        if sha is None:
            raise (Exception(err_msg))
        try:
            return (
                gh_repo.create_git_tag_and_release(
                    tag, "", tag, "", sha, "commit", draft=True, prerelease=is_prerelease
                ),
                True,
            )
        except Exception:
            raise (Exception(err_msg))


def UpdateReference(gh_release, tag, sha, is_prerelease, is_draft):
    print("· Update Release reference (force-push tag)")

    if is_draft:
        # Unfortunately, it seems not possible to update fields 'created_at' or 'published_at'.
        print(" > Update (pre-)release")
        gh_release.update_release(
            gh_release.title,
            "" if gh_release.body is None else gh_release.body,
            draft=False,
            prerelease=is_prerelease,
            tag_name=gh_release.tag_name,
            target_commitish=gh_release.target_commitish,
        )

    if sha is not None:
        print(f" > Force-push '{tag!s}' to {sha!s}")
        gh_repo.get_git_ref(f"tags/{tag!s}").edit(sha)


files = GetListOfArtifacts(sys_argv, paramFiles)
stdout.flush()
[tag, env_tag, is_prerelease] = CheckRefSemVer(paramRef, paramTag, paramSnapshots)
stdout.flush()
gh_repo = GetRepositoryHandler(GetGitHubAPIHandler(paramToken), paramRepo)
stdout.flush()
[gh_release, is_draft] = GetOrCreateRelease(gh_repo, tag, paramSHA, is_prerelease)
stdout.flush()

if paramRM:
    print("· RM set. All previous assets are being cleared...")
    for asset in gh_release.get_assets():
        print(f" - {asset.name}")
        asset.delete_asset()
stdout.flush()

print("· Cleanup and/or upload artifacts")
env = environ.copy()
env["GITHUB_TOKEN"] = paramToken
cmd = ["gh", "release", "upload", "--repo", paramRepo, "--clobber", tag] + files
print(f" > {' '.join(cmd)}")
check_call(cmd, env=env)
stdout.flush()

UpdateReference(gh_release, tag, paramSHA if env_tag is None else None, is_prerelease, is_draft)
