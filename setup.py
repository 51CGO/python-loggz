import os.path
import setuptools

if os.path.exists("README.md"):
    with open("README.md", "r") as fh:
        long_description = fh.read()
    long_description_content_type="text/markdown",
else:
    long_description=""
    long_description_content_type="text/plain",

setuptools.setup(
    name="loggz",
    version="1.0",
    author="Christophe Godart",
    author_email="dev@armaghast.eu",
    description="A small example package",
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url="https://github.com/crist0phe/python-loggz",
    packages=["loggz"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
