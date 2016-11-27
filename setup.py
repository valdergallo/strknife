# encoding: utf-8
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import strknifepy


def readme():
    try:
        os.system('pandoc --from=markdown --to=rst README.md -o README.rst')
        with open('README.rst') as f:
            return f.read()
    except Exception:
        return '''**Django Data Importer** is a tool which allow you to transform easily a CSV, XML, XLS and XLSX file into a python object or a django model instance. It is based on the django-style declarative model.'''


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['strknifepy', 'tests', '--cov=strknifepy', '-vrsx']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='strknifepy',
    url='https://github.com/valdergallo/data-importer',
    download_url='https://github.com/valdergallo/strknifepy/tarball/{0!s}/'.format(strknifepy.get_version()),
    author="valdergallo",
    author_email='valdergallo@gmail.com',
    keywords='Django Data Importer XLS XLSX CSV XML',
    description='Simple library to easily import data with Django',
    license='BSD',
    long_description=readme(),
    classifiers=[
      'Framework :: Django',
      'Operating System :: OS Independent',
      'Topic :: Utilities'
    ],
    version=strknifepy.get_version(),
    tests_require=[
        'pytest>=3.0.0',
        'pytest-cov==2.3.1',
        'django>=1.4',
    ],
    cmdclass={'test': PyTest},
    packages=['strknifepy'],
    zip_safe=False,
    platforms='any',
)
