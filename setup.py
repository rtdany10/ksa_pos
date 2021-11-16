from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ksa_pos/__init__.py
from ksa_pos import __version__ as version

setup(
	name="ksa_pos",
	version=version,
	description="KSA POS",
	author="Wahni Green Technologies",
	author_email="danyrt@wahni.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
