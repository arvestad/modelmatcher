import setuptools
import sys

def read_version_string(filename):
    versionstring = None
    with open(filename) as h:
        for line in h:
            try:
                identifier, equalsign, versionstring = line.split()
                if identifier == '__version__' and equalsign == '=':
                    return versionstring.strip("'")
            except:
                continue        # Just read past lines to fitting the pattern
    if versionstring is None:
        return 'unknown_version'

__version__ = read_version_string('modelmatcher/version.py')


with open("README.md", "r") as fh:
    at_top = True
    long_description = ''
    for line in fh:
        if at_top and line[:3] == '[![':
            pass                # Skipping the badge-lines in the github README.md
        else:
            at_top = False      # Now starts the "real" README.md
        long_description += line


if sys.version_info.major < 3:
    sys.exit('\n'
             'Sorry, Python 2 is not supported\n'
             'Did you run pip install modelmatcher?\n'
             'Try "pip3 install modelmatcher"')

elif sys.version_info.minor < 2:
    sys.exit('\nSorry, Python < 3.2 is not supported\n')

setuptools.setup(
    name="modelmatcher",
    version=__version__,
    author="Lars Arvestad",
    author_email="arve@math.su.se",
    description="Rapid identification of sequence evolution models",
    scripts = ['bin/modelmatcher'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arvestad/modelmatcher",
    packages=setuptools.find_packages(),
    python_requires='>=3.2',
    install_requires=[
        'biopython>=1.70',
        'numpy',
        'console_progressbar>=1.1.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
