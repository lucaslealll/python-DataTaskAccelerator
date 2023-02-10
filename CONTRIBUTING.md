# Contributing

1. **Please sign one of the contributor license agreements below.**
1. Fork the repo, develop and test your code changes, add docs.
1. Make sure that your commit messages clearly describe the changes.
1. Send a pull request.

Here are some guidelines for hacking on `data-tastk-accelerator`.

## Making changes

A few notes on making changes to `data-tastk-accelerator`.

-   If you've added a new feature or modified an existing feature, be sure to add or update any applicable documentation in docstrings and in the documentation (in `docs/`). You can re-generate the reference documentation using `nox -s docgen`.

-   The change must work fully on the following CPython versions: 3.6, 3.7, 3.8, 3.9, 3.10 across macOS, Linux, and Windows.

-   The codebase _must_ have 100% test statement coverage after each commit.
