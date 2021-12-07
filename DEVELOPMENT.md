# Development

## Tagging/versioning

See context in [#5](https://github.com/pyTooling/Actions/issues/5).

Tag new releases in the `main` branch using a semver compatible value, starting with `v`:

```sh
git checkout main
git tag v0.0.0
git push upstream v0.0.0
```

Move the corresponding release branch (starting with `r`) forward by creating a merge commit, and using the merged tag
as the commit message:

```sh
git checkout r0
git merge --no-ff -m 'v0.0.0' v0.0.0
git push upstream r0
```
