from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in doublem/__init__.py
from doublem import __version__ as version

setup(
	name="doublem",
	version=version,
	description="Doublem Customizations",
	author="Geoffrey Karani",
	author_email="geoffrey.kamundi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
