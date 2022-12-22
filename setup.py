#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().splitlines()

test_requirements = []

setup(
    author="Synthesis AI",
    author_email="anish@synthesis.ai",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Python library for loading synthetic data for ML use cases",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="synthesisai",
    name="synthesisai",
    packages=find_packages(include=["synthesisai", "synthesisai.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Synthesis-AI-Dev/synthesisai",
    version='0.2.0',
    zip_safe=False,
)
