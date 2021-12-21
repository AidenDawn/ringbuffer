import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

requirements = ["numpy>=1.11.1"]

setup(
    name="ringbuffer",
    version="0.0.1",
    description="Python implementation of a ringbuffer",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["ringbuffer"],
    license="APACHE-2.0",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python :: 3",
    ],
    install_requires=requirements,
    url="https://github.com/AidenDawn/ringbuffer",
    author="Daniel Schmeer",
    author_email="d.a.schmeer@gmail.com",
    setup_requires=["pytest-runner"],
    tests_require=["pytest>=3.9"],
)
