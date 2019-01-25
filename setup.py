import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cnngeometric',  
    version='0.1',
    scripts=['cnngeometric'] ,
    author="Felix Brechtmann, Ignacio Rocco",
    author_email="",
    description="cnngeometric",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brechtmann/cnngeometric_pytorch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: ??",
        "Operating System :: OS Independent",
    ],

)