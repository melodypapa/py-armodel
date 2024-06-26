# 1. py-armodel

## 1.1. Purpose

To support AUTOSAR model with python 

## 1.2. Reference Documents
1. AUTOSAR_TPS_XMLSchemaProductionRules.pdf
2. AUTOSAR_TPS_ARXMLSerializationRules.pdf

|Version|Documentation|Travis CI|Coverage Status|Pypi|
|--|--|--|--|--|
|[![GitHub version](https://badge.fury.io/gh/melodypapa%2Fpy-armodel.svg)](https://badge.fury.io/gh/melodypapa%2Fpy-armodel)|[![Documentation Status](https://readthedocs.org/projects/py-armodel/badge/?version=latest)](https://py-armodel.readthedocs.io/en/latest)|[![](https://www.travis-ci.com/melodypapa/py-armodel.svg?branch=main)](https://www.travis-ci.com/melodypapa/py-armodel)|[![Coverage Status](https://coveralls.io/repos/github/melodypapa/py-armodel/badge.svg?branch=main)](https://coveralls.io/github/melodypapa/py-armodel?branch=main)|[![PyPI version](https://badge.fury.io/py/armodel.svg)](https://badge.fury.io/py/armodel)|

## 1.3. How to create the distribution and upload to pypi
1. Run `python setup.py bdist_wheel` to generate distribution
2. Run `twine check dist/*` to check the validation of distribution
3. Run `twine upload dist/*` to upload to pypi repository
4. Check the website https://pypi.org/project/armodel/ to find out it works or not

And more details can be found at https://packaging.python.org/  

## 1.4. How to perform Unit test

* Run `pip install pytest pytest-cov` to install pytest.
* Run `pytest --cov=armodel --cov-report term-missing` to verify all the functionality.

## 1.5. How to create a distribution and wheel

* Run `python setup.py sdist bdist_wheel --universal`

## 1.6. How to create the document

1. Run `pip install sphinx` to install the necessary document

## 1.7. Heritage 

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
            - BswModuleEntry
          - Implementation
            - BswImplementation
        - AtpFeature
          - AtpPrototype
            - AtpPrototype
              - DataPrototype
                - AutosarDataPrototype
                  - VariableDataPrototype
                - ApplicationCompositeElementDataPrototype
                  - ApplicationArrayElement
                  - ApplicationRecordElement
          - AtpStructureElement
            - BswModuleDescription
        - ExecutableEntity
        - SwcBswMapping
  - ValueSpecification
    - ConstantReference
```

## 1.8. CLI usages

### 1.8.1. arxml-dump

**Dump all the arxml data to screen**


`arxml-dump --arxml arg -h`

--arxml arg     The file name of arxml data
-h              show the help information

#### 1.8.1.1. arxml-dump usage

**Dump the arxml data from test1.arxml and test2.arxml**

```
$arxml-dump --arxml test1.arxml --arxml test2.arxml
```

### 1.8.2. swc-list

**List all the SwComponentType in the autosar model**

usage: swc-list [-h] [-v] [-f FORMAT] [--filter FILTER] Input [Input ...]

-h, --help          show the help message and exit
-v, --verbose       Print debug information
-f FORMAT, --format FORMAT
                    Specify the short or long name of Sw-C. 
                      *short* : only print the short name of SWComponentType
                      *long*  : print the SWComponentType with ARPackage names
--filter FILTER     Set the filter condition. 
                      *CompositionSwComponent* : Print the CompositionSwComponent only.


#### 1.8.2.1. List all the SW-Components in the specific path

```
$swc-list <arxml_folder>
```

#### 1.8.2.2. List all the CompositionSwComponent with the long name

```
$swc-list --format long --filter CompositionSwComponent <arxml_folder> 
```

## 1.9. API

### 1.9.1. Constructor

```
  ARXMLParser(options={"warning": True})
```

## 1.10. Change notes:

**Version 0.1.1**

Add the ARRAY category support for ImplementationDataType

**Version 0.1.2**

Add the AsynchronousServerCallPoint support for ARXML

**Version 0.1.3**

Fix the attribute intervalType of **Limit** is empty issue.

**Version 1.0.0**

1. Add the logging support
2. Add the <warning> option to disable exception raised.
3. Add the BswMD support

**Version 1.1.0**

1. Add the InitEvent support. (Issue #5)
2. Add the DataReceiveEvent support. (Issue #5)
3. Add the SwcModeSwitchEvent support. (Issue #5)

**Version 1.2.0**

1. Add the SwcImplementation support (Issue #9)
2. Add the integer value for memory section alignment (Issue #9)
3. Remove the required attributes for the Implementation according to the AUTOSAR standard 23R-11. (Issue #9)
4. Change the START-ON-EVENT-REF to optional according to the AUTOSAR standard 23R-11. (Issue #9)
5. Change the HANDLE-OUT-OF-RANGE to optional according to the AUTOSAR standard 23R-11. (Issue #9)
6. Add the SensorActuatorSwComponentType support (Issue #9)
7. Change the CATEGORY of COMPU-METHOD to optional.
8. Change the CAN-BE-INVOKED-CONCURRENTLY to optional.

**Version 1.3.0**

1. List all the SwComponentType (Issue #11)
