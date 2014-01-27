# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 Hidekazu Ohnishi
# 
# This software is released under the terms of the BSD license.
# For more information see the COPYING.txt file in this directory.

from distutils.core import setup, Extension

lzhlib = Extension('lzhlib',
                   define_macros=[('MAJOR_VERSION', '0'),
                                  ('MINOR_VERSION', '1')],
                   sources=['lhafile/lzhlib.c'])

setup(name="lhafile",
      packages=['lhafile'],
      version='0.1',
      description="LHA(.lzh) file extract interface",
      long_description="""Extract LHA(.lzh) file extension.  
Its interface is likely zipfile extension is included in regular
python distribution.""",
      author='Hidekazu Ohnishi',
      author_email='the-o@neotitans.net',
      url='http://trac.neotitans.net/wiki/lhafile',
      download_url='http://trac.neotitans.net/wiki/lhafile',
      license='BSD',
      keywords = [],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Envrionment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent'
        'Programming Language :: Python',
        'Topic :: Software Development'],
      ext_modules=[lzhlib])
