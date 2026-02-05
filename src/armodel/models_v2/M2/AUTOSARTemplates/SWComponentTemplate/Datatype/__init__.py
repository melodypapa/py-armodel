"""
Datatypes module for AUTOSAR SWComponentTemplate.
"""

from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (  # noqa: F401, F403
    ApplicationArrayElement,
    ApplicationCompositeElementDataPrototype,
    ApplicationRecordElement,
    AutosarDataPrototype,
    DataPrototype,
    ParameterDataPrototype,
    VariableDataPrototype,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (  # noqa: F401, F403
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
