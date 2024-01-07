from setuptools import find_packages, setup

setup(
    name="ezpkl",
    version="0.1.0",
    description="lovely pickling🥒 for context manager hater👊",
    author="bailando",
    author_email="bailando.ys@gmail.com",
    url="https://github.com/yesinkim/ezpkl.git",
    packages=find_packages(exclude = []),
    keywords=["pickle", "file", "easy", "easypickle"],
    python_requires=">=3",
    
)
