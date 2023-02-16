"""Setup Module"""

import os
from setuptools import find_packages, setup

f = open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8")
readme = f.read()
f.close()

setup(
    name="DekuVerify",
    packages=find_packages(),
    version="0.1.0",
    description="Deku Verify Plugin",
    long_description=readme,
    author="Afkanerd",
    author_email="info@afkanerd.com",
    license="The GNU General Public License v3.0",
    install_requires=[
        "mysql-connector-python==8.0.32",
        "mysqlclient==2.1.1",
        "peewee==3.15.4",
    ],
    test_suite="tests",
)
