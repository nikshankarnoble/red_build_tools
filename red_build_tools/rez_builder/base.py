class BaseBuilder:
    def __init__(self, source_path, build_path, install_path, targets):
        self.source_path = source_path
        self.build_path = build_path
        self.install_path = install_path
        self.targets = targets

    def build(self):
        raise NotImplementedError()

    def install(self):
        raise NotImplementedError()


# # def ignore_files(src, names):
# #     return [
# #         '.git',
# #         '.gitignore',
# #         'build',
# #         'rezbuild.py',
# #     ]
# #
# #
# # def build(source_path, build_path, install_path, targets):
# #     """
# #     Generic Rez Build script for python packages that use the standard
# #     python distribution tools (i.e. setuptools, setup.py).
# #
# #     Supports local installs, console and gui scripts defined via entry_points,
# #     and "develop" mode for local installs.
# #
# #     """
# #     install_mode = "install" in targets
# #
# #     def _install():
# #         if os.path.exists(install_path):
# #             shutil.rmtree(install_path)
# #
# #         if os.path.exists(source_path):
# #             shutil.copytree(
# #                 source_path,
# #                 install_path,
# #                 ignore=shutil.ignore_patterns(
# #                     '.git',
# #                     '.gitignore',
# #                     'build',
# #                     'rezbuild.py',
# #                 )
# #             )
# #
# #     if install_mode:
# #         _install()