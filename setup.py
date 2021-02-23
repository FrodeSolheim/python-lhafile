# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 Hidekazu Ohnishi
# Copyright (C) 2014-2021 Frode Solheim
#
# This software is released under the terms of the BSD license.
# For more information see the COPYING.txt file in this directory.

from setuptools import setup, Extension
import sys
import platform

extra_compile_args = []
extra_link_args = []
if sys.platform == "darwin" and platform.machine() == "i386":
    extra_compile_args.append("-m32")
    extra_link_args.append("-m32")

lzhlib = Extension(
    "lzhlib",
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
    define_macros=[("MAJOR_VERSION", "0"), ("MINOR_VERSION", "2")],
    sources=["lzhlib.c"],
)

setup(
    name="lhafile",
    packages=["lhafile"],
    version="0.2.5",
    description="LHA archive support for Python",
    long_description="""\
A python package that handles .lha archives, with an interface similar to the
zipfile module found in the standard library.""",
    author="Hidekazu Ohnishi",
    author_email="the-o@neotitans.net",
    maintainer="Frode Solheim",
    maintainer_email="frode@solheim.dev",
    url="https://github.com/FrodeSolheim/python-lhafile/",
    download_url="https://pypi.org/project/lhafile/",
    license="BSD",
    keywords=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Archiving",
    ],
    ext_modules=[lzhlib],
)
