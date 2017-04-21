

from aodb import __version__
from setuptools import setup, find_packages


setup(
    name="aodb",
    version=__version__,
    author="Regner Blok-Andersen",
    author_email="regnerba@gmail.com",
    description="CLI tool and library for converting the Albion Online exports to other formats.",
    license="MIT",
    keywords="albion online database assets data",
    url="https://github.com/Regner/aodb",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'aodb = aodb.cli:cli',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
