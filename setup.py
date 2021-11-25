#!/usr/bin/python3

from setuptools import setup

import subprocess, glob, os.path
import os, sys

# Make the nvidia-installer hooks executable
#for x in glob.glob("nvidia-installer-hooks/*"):
#    os.chmod(x, 0o755)

setup(
    name="ubuntu-drivers-common",
    author="Alberto Milone",
    author_email="albertomilone@alice.it",
    maintainer="Alberto Milone",
    maintainer_email="albertomilone@alice.it",
    url="http://www.albertomilone.com",
    license="gpl",
    description="Detect and install additional Ubuntu driver packages",
    packages=["NvidiaDetector", "Quirks", "UbuntuDrivers"],
    data_files=[("/usr/share/ubuntu-drivers-common/", ["share/obsolete", "share/fake-devices-wrapper"]),
                ("/var/lib/ubuntu-drivers-common/", []),
                ("/usr/share/ubuntu-drivers-common/quirks", glob.glob("quirks/*")),
                ("/usr/share/ubuntu-drivers-common/detect", glob.glob("detect-plugins/*")),
                ("/usr/share/doc/ubuntu-drivers-common", ['README']),
                ("/usr/lib/nvidia/", glob.glob("nvidia-installer-hooks/*")),
                ("/usr/lib/ubiquity/target-config", glob.glob("ubiquity/target-config/*")),
    ],
    scripts=["nvidia-detector", "quirks-handler", "ubuntu-drivers"],
)
