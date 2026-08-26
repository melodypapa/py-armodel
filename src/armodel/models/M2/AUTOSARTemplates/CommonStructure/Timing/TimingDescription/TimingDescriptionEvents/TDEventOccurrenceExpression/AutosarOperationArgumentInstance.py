from typing import Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression.OperationArgumentInComponentInstanceRef import (
    OperationArgumentInComponentInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class AutosarOperationArgumentInstance(Identifiable):
    """
    This class represents a reference to an argument instance. This way it is possible to reference an argument instance in the occurrence expression formula. The argument instance can target to one of the following arguments: • a whole argument used in an operation of a PortPrototype with ClientServerInterface • an element inside of a composite argument used in an operation of a PortPrototype with ClientServer Interface
    """

    # AutosarOperationArgumentInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.53, p.85
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # operationArgumentInstanceIRef is an InstanceRef (OperationArgumentInComponentInstanceRef), read/written via its own reader/writer.
    # [x] __init__                               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getOperationArgumentInstanceIRef       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setOperationArgumentInstanceIRef       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef
        self.operationArgumentInstanceIRef: Optional[OperationArgumentInComponentInstanceRef] = None

    def getOperationArgumentInstanceIRef(self) -> Optional[OperationArgumentInComponentInstanceRef]:
        """This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef."""
        return self.operationArgumentInstanceIRef

    def setOperationArgumentInstanceIRef(self, value: Optional[OperationArgumentInComponentInstanceRef]) -> "AutosarOperationArgumentInstance":
        """This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef. A None value is a no-op and does not overwrite an existing operationArgumentInstanceIRef."""
        if value is not None:
            self.operationArgumentInstanceIRef = value
        return self
