#!/usr/bin/env python3

import re
import sys
from sys import argv, stdout
from os import environ, getenv
from subprocess import check_call
from glob import glob
from pathlib import Path
from github import Github

print("· Get list of artifacts to be uploaded")

args = []
files = []

if 'INPUT_FILES' in environ:
    args = environ['INPUT_FILES'].split()

if len(argv) > 1:
    args = args + argv[1:]

if len(args) == 0:
    stdout.flush()
    raise(Exception("Glob patterns need to be provided as positional arguments or through envvar 'INPUT_FILES'!"))

for item in args:
    items = glob(item)
    print("glob(%s)" % item, "->", items)
    files = files + items

if len(files) < 1:
    stdout.flush()
    raise(Exception('Empty list of files to upload/update!'))

print("· Get GitHub API handler (authenticate)")

if 'GITHUB_TOKEN' in environ:
    gh = Github(environ["GITHUB_TOKEN"])
elif 'INPUT_TOKEN' in environ:
    gh = Github(environ["INPUT_TOKEN"])
else:
    if 'GITHUB_USER' not in environ or 'GITHUB_PASS' not in environ:
        stdout.flush()
        raise(Exception("Need credentials to authenticate! Please, provide 'GITHUB_TOKEN', 'INPUT_TOKEN', or 'GITHUB_USER' and 'GITHUB_PASS'"))
    gh = Github(environ["GITHUB_USER"], environ["GITHUB_PASS"])

print("· Get Repository handler")

if 'GITHUB_REPOSITORY' not in environ:
    stdout.flush()
    raise(Exception("Repository name not defined! Please set 'GITHUB_REPOSITORY"))

gh_repo = gh.get_repo(environ['GITHUB_REPOSITORY'])

print("· Get Release handler")

tag = getenv('INPUT_TAG', 'tip')

env_tag = None
gh_ref = environ['GITHUB_REF']
is_prerelease = True
is_draft = False

if gh_ref[0:10] == 'refs/tags/':
    env_tag = gh_ref[10:]
    if env_tag != tag:
        semver = re.search(r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$", env_tag)
        if semver.group('prerelease') is None:
            # is a regular semver compilant tag
            is_prerelease = False
            tag = env_tag
        elif getenv('INPUT_SNAPSHOTS', 'true') == 'true':
            # is semver compilant prerelease tag, thus a snapshot (we skip it)
            sys.exit()

gh_tag = None
try:
    gh_tag = gh_repo.get_git_ref('tags/%s' % tag)
except Exception as e:
    stdout.flush()
    pass
if gh_tag:
    try:
        gh_release = gh_repo.get_release(tag)
    except Exception as e:
        gh_release = gh_repo.create_git_release(tag, tag, "", draft=True, prerelease=is_prerelease)
        is_draft = True
        pass
else:
    err_msg = "Tag/release '%s' does not exist and could not create it!" % tag
    if 'GITHUB_SHA' not in environ:
        raise(Exception(err_msg))
    try:
        gh_release = gh_repo.create_git_tag_and_release(tag,  "", tag, "", environ['GITHUB_SHA'], 'commit', draft=True, prerelease=is_prerelease)
        is_draft = True
    except Exception as e:
        raise(Exception(err_msg))

print("· Upload artifacts")

artifacts = files

assets = gh_release.get_assets()

if getenv('INPUT_RM', 'false') == 'true':
    print("· RM set. All previous assets are being cleared...")
    for asset in assets:
        print(" ", asset.name)
        asset.delete_asset()
else:
    for asset in assets:
        print(" >", asset)
        print("   %s:" % asset.name)
        for artifact in artifacts:
            aname = str(Path(artifact).name)
            if asset.name == aname:
                print("   - uploading tmp...")
                new_asset = gh_release.upload_asset(artifact, name='tmp.%s' % aname)
                print("   - removing...")
                asset.delete_asset()
                print("   - renaming tmp...")
                new_asset.update_asset(aname, label=aname)
                artifacts.remove(artifact)
                break

for artifact in artifacts:
    print(" >", artifact)
    print("   - uploading...")
    gh_release.upload_asset(artifact)

stdout.flush()
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
        target_commitish=gh_release.target_commitish
    )

if ('GITHUB_SHA' in environ) and (env_tag is None):
    sha = environ['GITHUB_SHA']
    print(" > Force-push '%s' to %s" % (tag, sha))
    gh_repo.get_git_ref('tags/%s' % tag).edit(sha)
