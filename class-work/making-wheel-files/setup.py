
from setuptools import setup,find_packages

setup(
    name='my_package',
    version='1.0.0',
    description="This is My Package",
    author='Awnish Kumar',
    requires=[], #install the package you provide
    packages_dir=find_packages() #search the package
)


