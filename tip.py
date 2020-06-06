#!/usr/bin/env python3

from os import environ, getenv
from sys import argv, stdout
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

try:
    gh_tag = gh_repo.get_git_ref('tags/%s' % tag)
except Exception as e:
    stdout.flush()
    # TODO: create the tag/release, instead of raising an exception
    raise(Exception("Tag '%s' does not exist!" % tag))

gh_release = gh_repo.get_release(tag)

print("· Upload artifacts")

artifacts = files

if getenv('INPUT_RM', 'false') == 'true':
    print("· RM set. All previous assets are being cleared...")
    for asset in gh_release.get_assets():
        print(" ", asset.name)
        asset.delete_asset()
else:
    for asset in gh_release.get_assets():
        print(">", asset)
        print(" ", asset.name)
        for artifact in artifacts:
            aname = str(Path(artifact).name)
            if asset.name == aname:
                print(" removing '%s'..." % asset.name)
                asset.delete_asset()
                print(" uploading '%s'..." % artifact)
                gh_release.upload_asset(artifact, name=aname)
                artifacts.remove(artifact)
                break

for artifact in artifacts:
    print(" uploading '%s'..." % artifact)
    gh_release.upload_asset(artifact)

stdout.flush()
print("· Update Release reference (force-push tag)")

if ('GITHUB_SHA' in environ) and ('GITHUB_REF' in environ) and environ['GITHUB_REF'] != 'refs/tags/%s' % tag:
    sha = environ['GITHUB_SHA']
    print("force-push '%s' to %s" % (tag, sha))
    gh_repo.get_git_ref('tags/%s' % tag).edit(sha)

    # TODO: alternatively, update the title/body of the release (while keeping the tag or not)
    # gh_release.update_release(
    #     gh_release.title,
    #     gh_release.body,
    #     draft=False,
    #     prerelease=True,
    #     tag_name=gh_release.tag_name,
    #     target_commitish=gh_release.target_commitish
    # )
