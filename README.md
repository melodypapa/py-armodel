# py-armodel

## Purpose

To support AUTOSAR model with python 

## Reference Documents
1. AUTOSAR_TPS_XMLSchemaProductionRules.pdf
2. AUTOSAR_TPS_ARXMLSerializationRules.pdf

|Version|Documentation|Travis CI|Coverage Status|Pypi|
|--|--|--|--|--|
|[![GitHub version](https://badge.fury.io/gh/melodypapa%2Fpy-armodel.svg)](https://badge.fury.io/gh/melodypapa%2Fpy-armodel)|[![Documentation Status](https://readthedocs.org/projects/py-armodel/badge/?version=latest)](https://py-armodel.readthedocs.io/en/latest)|[![](https://www.travis-ci.com/melodypapa/py-armodel.svg?branch=main)](https://www.travis-ci.com/melodypapa/py-armodel)|[![Coverage Status](https://coveralls.io/repos/github/melodypapa/py-armodel/badge.svg?branch=main)](https://coveralls.io/github/melodypapa/py-armodel?branch=main)|[![PyPI version](https://badge.fury.io/py/armodel.svg)](https://badge.fury.io/py/armodel)|

## How to create the distribution and upload to pypi
1. Run `python setup.py bdist_wheel` to generate distribution
2. Run `twine check dist/*` to check the validation of distribution
3. Run `twine upload dist/*` to upload to pypi repository
4. Check the website https://pypi.org/project/armodel/ to find out it works or not

And more details can be found at https://packaging.python.org/  

## How to perform Unit test

* Run `pip install pytest pytest-cov` to install pytest.
* Run `pytest --cov=armodel --cov-report term-missing` to verify all the functionality.

## How to create a distribution and wheel

* Run `python setup.py sdist bdist_wheel --universal`

## How to create the document

1. Run `pip install sphinx` to install the necessary document

## Heritage 

```
- ARObject
  - Referrable
    - MultilanguageReferrable
      - Identifiable
        - PackageableElement
          - ARElement
            - AtpType
              - AutosarDataType
              - PortInterface
                - DataInterface
                  - NvDataInterface
                  - ParameterInterface
                  - SenderReceiverInterface
        - AtpFeature
          - AtpPrototype
            - DataPrototype
              - AutosarDataPrototype
                - VariableDataPrototype
              - ApplicationCompositeElementDataPrototype
                - ApplicationArrayElement
                - ApplicationRecordElement
  - ValueSpecification
    - ConstantReference
```

## CLI usages

### arxml-dump

**Dump all the arxml data to screen**

`arxml-dump --arxml arg -h`

--arxml arg     The file name of arxml data
-h              show the help information

### Example for arxml-dump

**Dump the arxml data from test1.arxml and test2.arxml**

`arxml-dump --arxml test1.arxml --arxml test2.arxml`


