"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""


from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xxxswf',
    version='2.0.1',
    description=('xxxswf.py is a Python script for carving, scanning,' +
                 ' compressing, decompressing and analyzing Flash SWF files.'),
    long_description=long_description,
    url='https://bitbucket.org/Alexander_Hanel/xxxswf',
    author='Alexander Hanel',
    author_email='alexander<dot>hanel<at>gmail<dot>com',
    license='GNU',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='flash swf',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    extras_require={
        'lzma': ['pylzma'],
        'yara': ['yara'],
    },
    entry_points={
        'console_scripts': [
            'xxxswf=xxxswf.xxxswf:main',
        ],
    },
)
