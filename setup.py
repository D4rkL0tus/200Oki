"""
================================================================
COPYRIGHT OF INFORMATION SYSTEMS SERVICES 2025
MIT LICNSE

SETUP FILE

ANY DAMAGES THAT ARE CAUSED BY THIS SOFTWARE ARE NOT RESPONSIBLE BY
ANY PARTY BUT BESIDES THE PARTY RUNNING THE SOFTWARE
HEREBY STATING THAT THERE IS NO WARRENTY!

YOU HAVE BEEN WARNED!
================================================================

"""

from setuptools import setup, find_packages

setup(
    name="200Oki",             # Application name
    version="0.1.0",           # Version
    author="Information Systems Services",
    author_email="trent_schake2005@outlook.com",
    description="Software for testing multiple website status",
    packages=find_packages(),
    install_requires=[
        "requests",
        "threading",
        "time",
        "argparse"
    ],
    classifiers=[
        "programming language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independant",
    ],
    python_requires='>=3.6',



)