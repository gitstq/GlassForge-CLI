"""
Setup configuration for GlassForge CLI.

Zero-dependency package that installs the 'glassforge' console command.
"""

from setuptools import setup, find_packages

# Read version from package __init__
about = {}
with open("glassforge/__init__.py", "r", encoding="utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="glassforge-cli",
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    license="MIT",
    python_requires=">=3.8",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "glassforge=glassforge.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Utilities",
    ],
)
