from typing import Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression.VariableInComponentInstanceRef import (
    VariableInComponentInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class AutosarVariableInstance(Identifiable):
    """
    This class represents a reference to a variable instance within AUTOSAR. This way it is possible to reference a variable instance in the occurrence expression formula. The variable instance can target to one of the following variables: • a variable provided via a PortPrototype as whole • an element inside of a composite variable provided via a PortPrototype
    """

    # AutosarVariableInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.52, p.85
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # variableInstanceIRef is an InstanceRef (VariableInComponentInstanceRef), read/written via its own reader/writer.
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getVariableInstanceIRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setVariableInstanceIRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This is the reference to the instanceRef definition. InstanceRef implemented by: VariableInComponentInstanceRef
        self.variableInstanceIRef: Optional[VariableInComponentInstanceRef] = None

    def getVariableInstanceIRef(self) -> Optional[VariableInComponentInstanceRef]:
        """This is the reference to the instanceRef definition. InstanceRef implemented by: VariableInComponentInstanceRef."""
        return self.variableInstanceIRef

    def setVariableInstanceIRef(self, value: Optional[VariableInComponentInstanceRef]) -> "AutosarVariableInstance":
        """This is the reference to the instanceRef definition. InstanceRef implemented by: VariableInComponentInstanceRef. A None value is a no-op and does not overwrite an existing variableInstanceIRef."""
        if value is not None:
            self.variableInstanceIRef = value
        return self
