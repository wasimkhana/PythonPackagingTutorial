from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PackagingTutorial", # Replace with your own username
    version="0.0.1",
    author="Artaghal",
    author_email="wasimkhanak5@gmail.com",
    description="A small packaging tutorial",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Artaghal/pythonPackagingTutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
