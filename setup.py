from setuptools import setup, find_packages

setup(
    name='add',
    version='0.0.1',
    author='Nikoleta Glynatsi, Naty Clementi',
    author_email=('glynatsine@cardiff.ac.uk'),
    packages=find_packages('src'),
    package_dir={"": "src"},
    description='A library for adding numbers.',
)
