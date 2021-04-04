# py-armodel

## Purpose

To support AUTOSAR model with python 

## Reference Documents
1. AUTOSAR_TPS_XMLSchemaProductionRules.pdf
2. AUTOSAR_TPS_ARXMLSerializationRules.pdf

|Documentation|Travis CI|Coverage Status|
|--|--|--|
|[![Documentation Status](https://readthedocs.org/projects/py-armodel/badge/?version=latest)](https://pyarmodel.readthedocs.io/en/latest)|[![](https://www.travis-ci.com/melodypapa/py-armodel.svg?branch=main)](https://www.travis-ci.com/melodypapa/py-armodel)|[![Coverage Status](https://coveralls.io/repos/github/melodypapa/py-armodel/badge.svg?branch=main)](https://coveralls.io/github/melodypapa/py-armodel?branch=main)|

## How to create the distribution and upload to pypi
1. `python setup.py bdist_wheel`
2. `twine check dist/*`
3. `twine upload dist/*`

And more details can be found at https://packaging.python.org/  

## How to perform Unit test

* Run `pip install pytest pytest-cov` to install pytest.
* Run `pytest --cov=ar_model --cov-report term-missing` to verify all the functionality.

## How to create a distribution and wheel

* Run `python setup.py sdist bdist_wheel --universal`

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

### arxmldump

**Dump all the arxml data to screen**

`arxmldump --arxml arg -h`

--arxml arg     The file name of arxml data
-h              show the help information

### Example for arxmldump

**Dump the arxml data from test1.arxml and test2.arxml**

`arxmldump --arxml test1.arxml --arxml test2.arxml`


