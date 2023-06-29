# -*- coding: utf-8 -*-

name = 'red_build_tools'

version = '0.0.0'

requires = [
    'python-3',
]

build_command = "python {root}/rezbuild.py install"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}")

