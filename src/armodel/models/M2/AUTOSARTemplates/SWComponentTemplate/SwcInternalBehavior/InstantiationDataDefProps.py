from typing import Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef


class InstantiationDataDefProps(ARObject, VariationPointCapable):
    """
    This is a general class allowing to apply additional SwDataDefProps to
    particular instantiations of a Data Prototype. Typically the accessibility
    and further information like alias names for a particular data is modeled
    on the level of DataPrototypes (especially VariableDataPrototypes,
    ParameterDataPrototypes). But due to the recursive structure of the
    meta-model concerning data types (a composite (data) type consists out of
    data prototypes) a part of the MCD information is described in the data
    type (in case of Application CompositeDataType). This is a strong
    restriction in the reuse of data typed because the data type should be
    re-used for different VariableDataPrototypes and ParameterDataPrototypes
    to guarantee type compatibility on C-implementation level (e.g. data of a
    Port is stored in PIM or a ParameterDataPrototype used as ROM Block and
    shall be typed by the same data type as NVRAM Block). This class overcomes
    such a restriction if applied properly.
    """

    # InstantiationDataDefProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.41, p.588
    # Spec verified: R23-11
    # [x] __init__                    [x] impl  [x] docstring  [x] test
    # [x] getParameterInstance        [x] impl  [x] docstring  [x] test
    # [x] setParameterInstance        [x] impl  [x] docstring  [x] test
    # [x] getSwDataDefProps           [x] impl  [x] docstring  [x] test
    # [x] setSwDataDefProps           [x] impl  [x] docstring  [x] test
    # [x] getVariableInstance         [x] impl  [x] docstring  [x] test
    # [x] setVariableInstance         [x] impl  [x] docstring  [x] test

    def __init__(self):
        super().__init__()

        # This reference identifies the particular DataPrototype (defined in
        # the context of a composite ParameterDataPrototype) on which the
        # swDataDefProps shall be applied.
        self.parameterInstance: Optional[AutosarParameterRef] = None

        # These are the particular data definition properties which shall be
        # applied.
        self.swDataDefProps: Optional[SwDataDefProps] = None

        # This reference identifies the particular DataPrototype (defined in
        # the context of a composite VariableDataPrototype) on which the
        # swDataDefProps shall be applied.
        self.variableInstance: Optional[AutosarVariableRef] = None

    def getParameterInstance(self) -> Optional[AutosarParameterRef]:
        """Gets the particular ParameterDataPrototype on which the swDataDefProps shall be applied."""
        return self.parameterInstance

    def setParameterInstance(self, value: Optional[AutosarParameterRef]) -> "InstantiationDataDefProps":
        """
        Sets the particular ParameterDataPrototype on which the swDataDefProps
        shall be applied. A None value is a no-op and does not overwrite an
        existing parameterInstance.
        """
        if value is not None:
            self.parameterInstance = value
        return self

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """Gets the particular data definition properties which shall be applied."""
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> "InstantiationDataDefProps":
        """
        Sets the particular data definition properties which shall be applied.
        A None value is a no-op and does not overwrite an existing
        swDataDefProps.
        """
        if value is not None:
            self.swDataDefProps = value
        return self

    def getVariableInstance(self) -> Optional[AutosarVariableRef]:
        """Gets the particular VariableDataPrototype on which the swDataDefProps shall be applied."""
        return self.variableInstance

    def setVariableInstance(self, value: Optional[AutosarVariableRef]) -> "InstantiationDataDefProps":
        """
        Sets the particular VariableDataPrototype on which the swDataDefProps
        shall be applied. A None value is a no-op and does not overwrite an
        existing variableInstance.
        """
        if value is not None:
            self.variableInstance = value
        return self
