import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="formicary",
    version="0.1",
    author="Thales Gibbon",
    author_email="thales.gibbon@gmail.com",
    description="lib de etl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thalesgibbon/formicary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)