# Changes to modelmatcher

## 1.1.4


## 1.1.3

* Getting the package to work as useful module as well.
* There is now basic support in the module (not the modelmatcher tool)
  for estimating evolutionary distance.
* Tried to make important functions and classes available after "import modelmatcher",
  without knowing the actual files". So, avoiding
    "from modelmatcher.models import RateMatrix"
  and instead allowing "from modelmatcher import RateMatrix".
* First tiny attempt of getting unit tests running.


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
