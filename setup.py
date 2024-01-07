from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ezpkl",
    version="0.1.1",
    description="lovely pickling🥒 for context manager hater👊",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="bailando",
    author_email="bailando.ys@gmail.com",
    url="https://github.com/yesinkim/ezpkl.git",
    packages=find_packages(exclude=[]),
    keywords=["pickle", "file", "easy", "easypickle"],
    python_requires=">=3",
)
