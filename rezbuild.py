#!/usr/bin/env python
import os
import sys
import shutil


def ignore_files(src, names):
    return [
        '.git',
        '.gitignore',
        'build',
        'rezbuild.py',
    ]


def build(source_path, build_path, install_path, targets):
    """
    Generic Rez Build script for python packages that use the standard
    python distribution tools (i.e. setuptools, setup.py).

    Supports local installs, console and gui scripts defined via entry_points,
    and "develop" mode for local installs.

    """
    install_mode = "install" in targets

    def _install():
        if os.path.exists(install_path):
            shutil.rmtree(install_path)

        if os.path.exists(source_path):
            shutil.copytree(
                source_path,
                install_path,
                ignore=shutil.ignore_patterns(
                    '.git',
                    '.gitignore',
                    'build',
                    'rezbuild.py',
                )
            )

    if install_mode:
        _install()


if __name__ == "__main__":
    build(
        source_path=os.environ["REZ_BUILD_SOURCE_PATH"],
        build_path=os.environ["REZ_BUILD_PATH"],
        install_path=os.environ["REZ_BUILD_INSTALL_PATH"],
        targets=sys.argv[1:],
    )
