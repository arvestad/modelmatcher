# Changes to modelmatcher

## 1.2

* Last version should have increased the minor version number (because of new feature), so bumping
  that number now instead.
* It is no longer an error to request more samples than there sequence pairs. It is just limited to
  the number of available pairs.
* Sampling information is now added to JSON output.


## 1.1.4

* Added --version
* Corrected MrBayes model names
* Implemented the --sample-size option, to offer a limit to the number of sequence pairs that are
  consider, and avoid a O(n^2L) trap in favor of O(L) behaviour.
* Started using SonarCloud.com
* Improved setup.py
* Changed identifiers to follow PEP-8
* A first unit test has been implemented.

## 1.1.3

* Getting the package to work as useful module as well.
* Tried to make important functions and classes available after "import modelmatcher",
  without knowing the actual files". So, avoiding
    "from modelmatcher.models import RateMatrix"
  and instead allowing "from modelmatcher import RateMatrix".
* First tiny attempt of getting unit tests running.
* Ensured that, when outputting for IQTREE, only models known to IQTREE are considered.

## 1.1.2

Version got messed up.

## 1.1.1

* Added more models:
    - mtDeu
    - mtInv
    - mtMet
    - mtPro
    - mtVer
    - PMB


## 1.1.0

* Added support for testing MSA amino-acid frequencies on top of the
  model-specified probabilities, as suggested by Ingo Ebersberger.
* More output formats.

## 1.0.1

* First version added to PyPi.
