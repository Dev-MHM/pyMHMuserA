import re

import setuptools

requirements = [
    "redis",
    "python-decouple==3.3",
    "python-dotenv==0.15.0",
    "aiofiles",
    "aiohttp[speedups]",
    "hiredis",
    "psycopg2-binary",
]


with open("pyMHMuser/version.py", "rt", encoding="utf8") as x:
    version = re.search(r'__version__ = "(.*?)"', x.read()).group(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "py-MHMuser"
author = "MHMuser"
author_email = "mohammadihussein.m@gmail.com"
description = "A Secure and Powerful Python-Telethon Based Library For MHMuser Userbot."
license_ = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/Dev-MHM/pyMHMuser"
project_urls = {
    "Bug Tracker": "https://github.com/Dev-MHM/pyMHMuser/issues",
    "Documentation": "https://vip.alcybery.com",
    "Source Code": "https://github.com/Dev-MHM/pyMHMuser",
}
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    project_urls=project_urls,
    license=license_,
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=classifiers,
    python_requires=">3.6, <3.10",
)
