from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in estateapp/__init__.py
from estateapp import __version__ as version

setup(
	name="estateapp",
	version=version,
	description="Estate App manager",
	author="test",
	author_email="test@test.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
