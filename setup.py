from setuptools import setup, Extension
import os


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
  name='Boost Example',
  version='0.0.1',
  description='An boost.python project example implementing boost',
  long_description=readme(),
  author_email='simon.dirmeier@web.de',
  license='GPLv3',
  keywords=['boost'],
  packages=['boost'],
  ext_modules=[
      Extension('boost.modules',
                ['src/modules.cpp'],
                include_dirs=['src'],
                library_dirs=['/'],
                libraries=['boost_python'],
                extra_compile_args=['-g', '-O3', '-Wall'])
  ],
  classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.1',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6'
  ]
)
