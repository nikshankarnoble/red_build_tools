import os
import shutil

from red_build_tools.rez_builder.base import BaseBuilder


DEFAULT_IGNORE_PATTERNS = (
    '.git',
    '.gitignore',
    'build',
    'rezbuild.py',
)


class GenericBuilder(BaseBuilder):
    def __init__(
            self,
            source_path,
            build_path,
            install_path,
            targets,
            ignore=DEFAULT_IGNORE_PATTERNS,
    ):
        super().__init__(source_path, build_path, install_path, targets)
        self.ignore_patterns = ignore


    def build(self):
        return

    def install(self):
        if os.path.exists(self.install_path):
            shutil.rmtree(self.install_path)

        if os.path.exists(self.source_path):
            shutil.copytree(
                self.source_path,
                self.install_path,
                ignore=shutil.ignore_patterns(
                    *self.ignore_patterns
                )
            )