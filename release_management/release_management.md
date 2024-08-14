# Managing releases in a repository

## Creating a release

    gh release create TAG

    gh release create v1.0.0 --title "v1.0.0 (beta)" --notes "this is a beta release" --prerelease

## Editing a release

    gh release edit v1.0.0 -t "v1.0.0 (beta)"

## Deleting a release

    gh release delete TAG -y

    gh release delete v1.0.0
