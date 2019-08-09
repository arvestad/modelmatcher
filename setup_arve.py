import setuptools
import sys

with open("README.md", "r") as fh:
    at_top = True
    long_description = ''
    for line in fh:
        if at_top and line[:3] == '[![':
            pass                # Skipping the badge-lines in the github README.md
        else:
            at_top = False      # Now starts the "real" README.md
        long_description += line


with open('modelmatcher/version.py') as fh:
    exec(fh.read())

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
    scripts = ['bin/modelmatcher', 'bin/gen_q', 'bin/gen_freq', 'bin/modelprojector', 'bin/combine_q'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arvestad/modelmatcher",
#    test_suite = "tests",
    packages=setuptools.find_packages(),
    python_requires='>=3.2',
    install_requires=[
        'biopython>=1.70',
        'numpy',
        'console_progressbar'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ),
)
