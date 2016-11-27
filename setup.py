# encoding: utf-8
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import strknife


def readme():
    try:
        os.system('pandoc --from=markdown --to=rst README.md -o README.rst')
        with open('README.rst') as f:
            return f.read()
    except Exception:
        return ''''''


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['strknife', 'tests', '--cov=strknife', '-vrsx']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='strknife',
    url='https://github.com/valdergallo/strknife',
    download_url='https://github.com/valdergallo/strknife/tarball/{0!s}/'.format(strknife.get_version()),
    author="valdergallo",
    author_email='valdergallo@gmail.com',
    keywords='',
    description='Simple library to easily import data with Django',
    license='BSD',
    long_description=readme(),
    classifiers=[
      'Framework :: Django',
      'Operating System :: OS Independent',
      'Topic :: Utilities'
    ],
    version=strknife.get_version(),
    tests_require=[
        'pytest>=3.0.0',
        'pytest-cov==2.3.1',
        'django>=1.4',
    ],
    cmdclass={'test': PyTest},
    packages=['strknife'],
    zip_safe=False,
    platforms='any',
)
