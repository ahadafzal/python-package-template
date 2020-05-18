"""Setup for the chocobo package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Ahad Afzal",
    author_email="ahadbutafzal@gmail.com",
    name='python_package_template',
    license="MIT",
    description='Whate ereve',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/ahadafzal/python-package-template',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=[], # module dependencies
    classifiers=[]
)