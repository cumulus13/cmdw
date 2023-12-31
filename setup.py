import io
#import re
from setuptools import setup

import os
import shutil
try:
    os.remove(os.path.join('cmdw', '__version__.py'))
except:
    pass
shutil.copy2('__version__.py', 'cmdw')


with io.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()

# with io.open("__version__.py", "rt", encoding="utf8") as f:
    # version = re.search(r"version = \'(.*?)\'", f.read()).group(1)
from cmdw import __version__
version = __version__

setup(
    name="cmdw",
    version=version,
    url="https://github.com/licface/cmdw",
    project_urls={
        "Documentation": "https://github.com/licface/cmdw",
        "Code": "https://github.com/licface/cmdw",
        "Issue tracker": "https://github.com/licface/cmdw/issues",
    },
    license="BSD",
    author="Hadi Cahyadi LD",
    author_email="cumulus13@gmail.com",
    maintainer="cumulus13 Team",
    maintainer_email="cumulus13@gmail.com",
    description="just get info of length and width of terminal/console/cmd",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=["cmdw"],
    data_files=['__version__.py', 'README.rst', 'LICENSE.rst'],
    include_package_data=True,
    package_data = {
       '': ['*.txt', '*.ini', '*.rst'] 
    }, 
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
