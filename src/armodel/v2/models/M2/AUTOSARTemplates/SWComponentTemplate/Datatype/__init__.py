"""
Datatypes module for AUTOSAR SWComponentTemplate.
"""

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    ApplicationArrayElement,
    ApplicationCompositeElementDataPrototype,
    ApplicationRecordElement,
    AutosarDataPrototype,
    DataPrototype,
    ParameterDataPrototype,
    VariableDataPrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ApplicationArrayDataType,
    ApplicationCompositeDataType,
    ApplicationDataType,
    ApplicationPrimitiveDataType,
    ApplicationRecordDataType,
    AutosarDataType,
    DataTypeMap,
    DataTypeMappingSet,
)

__all__ = [
    # From DataPrototypes
    'ApplicationArrayElement',
    'ApplicationCompositeElementDataPrototype',
    'ApplicationRecordElement',
    'AutosarDataPrototype',
    'DataPrototype',
    'ParameterDataPrototype',
    'VariableDataPrototype',
    # From Datatypes
    'ApplicationArrayDataType',
    'ApplicationCompositeDataType',
    'ApplicationDataType',
    'ApplicationPrimitiveDataType',
    'ApplicationRecordDataType',
    'AutosarDataType',
    'DataTypeMap',
    'DataTypeMappingSet',
]
