


from setuptools import setup, find_packages

with open("README.md",'r') as file:
    long_description = file.read()

setup(
    name = 'sixfab_cellulariot_5G',     # this should be unique = python package
    version = "0.0.1",
    author = "Ramy Amer",
    author_email = 'ramy.mohamed@ibm.com',
    description = 'This is the necessary package for Sixfab S56',
    long_description = long_description,
    long_description_content_type = 'text/markdown',        # md for markdown file
    packages = find_packages(),    # automatically find the folder of the package I will create
    classifiers = [
                'Programming Language :: Python :: 3',
                'License :: OSI approved :: MIT License',       # MIT or BSD
                'Operating System :: OS Independent'],
    python_requires = '>=3.5',
    )



#
