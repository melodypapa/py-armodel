"""
AUTOSAR V2 Models - Clean import architecture.

V2 Implementation:
- Absolute imports only (CODING_RULE_V2_00001)
- No TYPE_CHECKING (CODING_RULE_V2_00002)
- Explicit __all__ exports (CODING_RULE_V2_00003)
- String annotations for forward refs (CODING_RULE_V2_00005)
- V2 module path convention (CODING_RULE_V2_00004)

Compatible with V1 API.
"""

# Version
__version__ = "2.0.0"

# MSR imports
from armodel.v2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import *
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate import *
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import *
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import *
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import *
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Filter import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import *

# Additional CommonStructure imports
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HardwareConfiguration import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.SoftwareContext import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.AtpBlueprint import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.Traceable import *
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import *

# Additional DiagnosticExtract imports
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract import *
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import *
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import *
from armodel.v2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import *

# ECUCParameterDefTemplate
from armodel.v2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import *
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate import *
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import *

# Additional EcuResourceTemplate imports
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementConnector import *

# GenericStructure imports
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.AtpDefinition import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import *

# Components wildcard import removed to avoid circular import with InternalBehavior
# from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import *
# Additional SWComponentTemplate imports
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import *

# Additional SystemTemplate imports
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    EcuInstance,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import *
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import *
from armodel.v2.models.M2.MSR.AsamHdo import *
from armodel.v2.models.M2.MSR.AsamHdo.AdminData import *
from armodel.v2.models.M2.MSR.AsamHdo.BaseTypes import *
from armodel.v2.models.M2.MSR.AsamHdo.ComputationMethod import *
from armodel.v2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import *
from armodel.v2.models.M2.MSR.AsamHdo.SpecialData import *
from armodel.v2.models.M2.MSR.AsamHdo.Units import *

# Additional MSR imports
from armodel.v2.models.M2.MSR.CalibrationData import *
from armodel.v2.models.M2.MSR.CalibrationData.CalibrationValue import *
from armodel.v2.models.M2.MSR.DataDictionary import *
from armodel.v2.models.M2.MSR.DataDictionary.AuxillaryObjects import *
from armodel.v2.models.M2.MSR.DataDictionary.Axis import *
from armodel.v2.models.M2.MSR.DataDictionary.CalibrationParameter import *
from armodel.v2.models.M2.MSR.DataDictionary.DataDefProperties import *
from armodel.v2.models.M2.MSR.DataDictionary.RecordLayout import *
from armodel.v2.models.M2.MSR.DataDictionary.ServiceProcessTask import *
from armodel.v2.models.M2.MSR.DataDictionary.SystemConstant import *
from armodel.v2.models.M2.MSR.Documentation import *
from armodel.v2.models.M2.MSR.Documentation.Annotation import *
from armodel.v2.models.M2.MSR.Documentation.BlockElements import *
from armodel.v2.models.M2.MSR.Documentation.BlockElements.Figure import *
from armodel.v2.models.M2.MSR.Documentation.BlockElements.Formula import *
from armodel.v2.models.M2.MSR.Documentation.TextModel import *
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import *
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import *
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import *
from armodel.v2.models.M2.MSR.Documentation.TextModel.LanguageDataModel import *
from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import *

# utils
from armodel.v2.models.utils import *
from armodel.v2.models.utils.uuid_mgr import *

# NOTE: Some classes in subdirectories with name collisions cannot be directly imported:
# - BswBehavior/*.py files (9 classes)
# - BswInterfaces/*.py files (3 classes)
# - BswOverview/InstanceRefs/*.py files (1 class)
# These are accessible via their full import paths, e.g.:
# from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.BswAsynchronousServerCallReturnsEvent

# Define __all__ to enable re-export of wildcard imports
# Start with version
__all__ = ['__version__']

# This collects all public names (not starting with _) for re-export
_all_exports = [name for name in globals() if not name.startswith('_')]
__all__.extend(_all_exports)
