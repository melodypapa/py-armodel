"""
V2 M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior package.
"""

# Classes:
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.ConsistencyNeeds import (
    ConsistencyNeeds,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.DataPrototypeGroup import (
    DataPrototypeGroup,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.RunnableEntityGroup import (
    RunnableEntityGroup,
)

__all__ = [
    # .InstanceRef.*,
    "ConsistencyNeeds",
    "DataPrototypeGroup",
    "RunnableEntityGroup",
]
