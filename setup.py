import setuptools
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="argeye",
    version="0.0.3",
    author="llzmgjzhy", 
    author_email="bmnjklipo@qq.com",
    description="A small optimization of Python library argparse.All original usage are retained,but adding a yml file so the user can set the arguments by editing the yml file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/llzmgjzhy/argeye.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)