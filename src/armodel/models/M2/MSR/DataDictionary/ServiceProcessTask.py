from typing import Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ArgumentDirectionEnum
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps, ValueList


class SwServiceArg(Identifiable, VariationPointCapable):
    """
    Specifies the properties of a data object exchanged during the call of an SwService, e.g. an argument or a return value. The SwServiceArg can also be used in the argument list of a C-macro. For this purpose the category shall be set to "MACRO". A reference to implementationDataType can optional be added if the actual argument has an implementationDataType.
    """

    # SwServiceArg method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.6, p.38
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDirection            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDirection            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwArraysize          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwArraysize          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwDataDefProps       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwDataDefProps       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the direction of the data transfer. The direction shall indicate the direction of the actual information that is being consumed by the caller and/or the callee, not the direction of formal arguments in C. The attribute is optional for backwards compatibility reasons. For example, if a pointer is used to pass a memory address for the expected result, the direction shall be "out". If a pointer is used to pass a memory address with content to be read by the callee, its direction shall be "in". Tags: xml.sequenceOffset=10
        self.direction: Optional[ArgumentDirectionEnum] = None

        # This turns the argument of the service to an array. Tags: xml.sequenceOffset=20
        self.swArraysize: Optional[ValueList] = None

        # Data properties of this SwServiceArg. Stereotypes: atpSplitable Tags: atp.Splitkey=swDataDefProps xml.sequenceOffset=30
        self.swDataDefProps: Optional[SwDataDefProps] = None

    def getDirection(self) -> Optional[ArgumentDirectionEnum]:
        """
        Specifies the direction of the data transfer. The direction shall indicate the direction of the actual information that is being consumed by the caller and/or the callee, not the direction of formal arguments in C. The attribute is optional for backwards compatibility reasons. For example, if a pointer is used to pass a memory address for the expected result, the direction shall be "out". If a pointer is used to pass a memory address with content to be read by the callee, its direction shall be "in".

        Returns:
            Optional[ArgumentDirectionEnum]: The direction
        """
        return self.direction

    def setDirection(self, value: Optional[ArgumentDirectionEnum]) -> "SwServiceArg":
        """
        Specifies the direction of the data transfer. The direction shall indicate the direction of the actual information that is being consumed by the caller and/or the callee, not the direction of formal arguments in C. The attribute is optional for backwards compatibility reasons. For example, if a pointer is used to pass a memory address for the expected result, the direction shall be "out". If a pointer is used to pass a memory address with content to be read by the callee, its direction shall be "in". A None value is a no-op and does not overwrite an existing direction.

        Args:
            value: The direction to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.direction = value
        return self

    def getSwArraysize(self) -> Optional[ValueList]:
        """
        This turns the argument of the service to an array.

        Returns:
            Optional[ValueList]: The swArraysize
        """
        return self.swArraysize

    def setSwArraysize(self, value: Optional[ValueList]) -> "SwServiceArg":
        """
        This turns the argument of the service to an array. A None value is a no-op and does not overwrite an existing swArraysize.

        Args:
            value: The swArraysize to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swArraysize = value
        return self

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """
        Data properties of this SwServiceArg.

        Returns:
            Optional[SwDataDefProps]: The swDataDefProps
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> "SwServiceArg":
        """
        Data properties of this SwServiceArg. A None value is a no-op and does not overwrite an existing swDataDefProps.

        Args:
            value: The swDataDefProps to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swDataDefProps = value
        return self
