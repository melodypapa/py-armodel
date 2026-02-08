from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class McFunctionDataRefSet(ARObject):
    """
    Refers to a set of data assigned to an McFunction in a particular role. The
    data are given • either by entries in a FlatMap • or by data instances that
    are part of MC support data. These two possibilities are exclusive within a
    given McFunctionDataRefSet. Which one to use depends on the process and tool
    environment. The set is subject to variability because the same functional
    model may be used with various representation of the data. Tags:
    vh.latestBindingTime=preCompileTime

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 187, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 455, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to an entry in a FlatMap that is part of the set, for calibration
                # parameter or measured variable.
        # atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        self._flatMapEntry: List["FlatInstanceDescriptor"] = []

    @property
    def flat_map_entry(self) -> List["FlatInstanceDescriptor"]:
        """Get flatMapEntry (Pythonic accessor)."""
        return self._flatMapEntry
        # Refers to a data instance within MC support data that is the set, i.
        # e.
        # a calibration parameter or measured atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        self._mcDataInstance: List["McDataInstance"] = []

    @property
    def mc_data_instance(self) -> List["McDataInstance"]:
        """Get mcDataInstance (Pythonic accessor)."""
        return self._mcDataInstance

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFlatMapEntry(self) -> List["FlatInstanceDescriptor"]:
        """
        AUTOSAR-compliant getter for flatMapEntry.

        Returns:
            The flatMapEntry value

        Note:
            Delegates to flat_map_entry property (CODING_RULE_V2_00017)
        """
        return self.flat_map_entry  # Delegates to property

    def getMcDataInstance(self) -> List["McDataInstance"]:
        """
        AUTOSAR-compliant getter for mcDataInstance.

        Returns:
            The mcDataInstance value

        Note:
            Delegates to mc_data_instance property (CODING_RULE_V2_00017)
        """
        return self.mc_data_instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import (
    List,
    Union,
)

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptEnablerImplTypeEnum import (
    RptEnablerImplTypeEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptExecutionControlEnum import (
    RptExecutionControlEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptPreparationEnum import (
    RptPreparationEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptSupportData(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    Represents RPT support data in AUTOSAR.
    Defines data structures for supporting read-protect-transform functionality.
    """


    def __init__(self) -> None:
        """
        Initializes the RptSupportData with default values.
        """
        super().__init__()
        self.rptComponents: List[RefType] = []
        self.rptEnablerImplType: Union[Union[RptEnablerImplTypeEnum, None] , None] = None
        self.rptExecutionControl: Union[Union[RptExecutionControlEnum, None] , None] = None
        self.rptPreparation: Union[Union[RptPreparationEnum, None] , None] = None

    def addRptComponent(self, ref: RefType):
        """
        Adds an RPT component reference.

        Args:
            ref: The RPT component reference to add

        Returns:
            self for method chaining
        """
        self.rptComponents.append(ref)
        return self

    def getRptComponents(self) -> List[RefType]:
        """
        Gets the list of RPT component references.

        Returns:
            List of RPT component references
        """
        return self.rptComponents

    def getRptEnablerImplType(self) -> Union[RptEnablerImplTypeEnum, None]:
        """
        Gets the RPT enabler implementation type.

        Returns:
            RPT enabler implementation type enum value
        """
        return self.rptEnablerImplType

    def setRptEnablerImplType(self, value: RptEnablerImplTypeEnum) -> "RptSupportData":
        """
        Sets the RPT enabler implementation type.

        Args:
            value: RPT enabler implementation type enum value to set

        Returns:
            self for method chaining
        """
        self.rptEnablerImplType = value
        return self

    def getRptExecutionControl(self) -> Union[RptExecutionControlEnum, None]:
        """
        Gets the RPT execution control type.

        Returns:
            RPT execution control enum value
        """
        return self.rptExecutionControl

    def setRptExecutionControl(self, value: RptExecutionControlEnum) -> "RptSupportData":
        """
        Sets the RPT execution control type.

        Args:
            value: RPT execution control enum value to set

        Returns:
            self for method chaining
        """
        self.rptExecutionControl = value
        return self

    def getRptPreparation(self) -> Union[RptPreparationEnum, None]:
        """
        Gets the RPT preparation type.

        Returns:
            RPT preparation enum value
        """
        return self.rptPreparation

    def setRptPreparation(self, value: RptPreparationEnum) -> "RptSupportData":
        """
        Sets the RPT preparation type.

        Args:
            value: RPT preparation enum value to set

        Returns:
            self for method chaining
        """
        self.rptPreparation = value
        return self

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptAccessEnum import (
    RptAccessEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptSwPrototypingAccess(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    Represents RPT software prototyping access in AUTOSAR.
    Defines access controls for software prototyping through RPT.
    """


    def __init__(self) -> None:
        """
        Initializes the RptSwPrototypingAccess with default values.
        """
        super().__init__()
        self.portRef: Union[Union[RefType, None] , None] = None
        self.rptAccess: Union[Union[RptAccessEnum, None] , None] = None

    def getPortRef(self) -> Union[RefType, None]:
        """
        Gets the port reference.

        Returns:
            Reference to the port
        """
        return self.portRef

    def setPortRef(self, value: RefType) -> "RptSwPrototypingAccess":
        """
        Sets the port reference.

        Args:
            value: The port reference to set

        Returns:
            self for method chaining
        """
        self.portRef = value
        return self

    def getRptAccess(self) -> Union[RptAccessEnum, None]:
        """
        Gets the RPT access type.

        Returns:
            RPT access enum value
        """
        return self.rptAccess

    def setRptAccess(self, value: RptAccessEnum) -> "RptSwPrototypingAccess":
        """
        Sets the RPT access type.

        Args:
            value: RPT access enum value to set

        Returns:
            self for method chaining
        """
        self.rptAccess = value
        return self

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class RptComponent(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    Represents an RPT (Read-Protect-Transform) component in AUTOSAR.
    Defines a component that supports read-protect-transform functionality.
    """


    def __init__(self) -> None:
        """
        Initializes the RptComponent with default values.
        """
        super().__init__()
        self.componentRef: Union[str, None] = None
        self.portRef: Union[str, None] = None

    def getComponentRef(self) -> Union[str, None]:
        """
        Gets the component reference.

        Returns:
            String representing the component reference
        """
        return self.componentRef

    def setComponentRef(self, value: str) -> "RptComponent":
        """
        Sets the component reference.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.componentRef = value
        return self

    def getPortRef(self) -> Union[str, None]:
        """
        Gets the port reference.

        Returns:
            String representing the port reference
        """
        return self.portRef

    def setPortRef(self, value: str) -> "RptComponent":
        """
        Sets the port reference.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.portRef = value
        return self

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptAccessEnum import (
    RptAccessEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptExecutableEntity(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    Represents an RPT executable entity in AUTOSAR.
    Defines an executable entity that supports read-protect-transform functionality.
    """


    def __init__(self) -> None:
        """
        Initializes the RptExecutableEntity with default values.
        """
        super().__init__()
        self.executableEntityRef: Union[Union[RefType, None] , None] = None
        self.rptAccess: Union[Union[RptAccessEnum, None] , None] = None

    def getExecutableEntityRef(self) -> Union[RefType, None]:
        """
        Gets the executable entity reference.

        Returns:
            Reference to the executable entity
        """
        return self.executableEntityRef

    def setExecutableEntityRef(self, value: RefType) -> "RptExecutableEntity":
        """
        Sets the executable entity reference.

        Args:
            value: The executable entity reference to set

        Returns:
            self for method chaining
        """
        self.executableEntityRef = value
        return self

    def getRptAccess(self) -> Union[RptAccessEnum, None]:
        """
        Gets the RPT access type.

        Returns:
            RPT access enum value
        """
        return self.rptAccess

    def setRptAccess(self, value: RptAccessEnum) -> "RptExecutableEntity":
        """
        Sets the RPT access type.

        Args:
            value: RPT access enum value to set

        Returns:
            self for method chaining
        """
        self.rptAccess = value
        return self

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptAccessEnum import (
    RptAccessEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptExecutableEntityEvent(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    Represents an RPT executable entity event in AUTOSAR.
    Defines an event associated with an RPT executable entity.
    """


    def __init__(self) -> None:
        """
        Initializes the RptExecutableEntityEvent with default values.
        """
        super().__init__()
        self.eventRef: Union[Union[RefType, None] , None] = None
        self.rptAccess: Union[Union[RptAccessEnum, None] , None] = None

    def getEventRef(self) -> Union[RefType, None]:
        """
        Gets the event reference.

        Returns:
            Reference to the event
        """
        return self.eventRef

    def setEventRef(self, value: RefType) -> "RptExecutableEntityEvent":
        """
        Sets the event reference.

        Args:
            value: The event reference to set

        Returns:
            self for method chaining
        """
        self.eventRef = value
        return self

    def getRptAccess(self) -> Union[RptAccessEnum, None]:
        """
        Gets the RPT access type.

        Returns:
            RPT access enum value
        """
        return self.rptAccess

    def setRptAccess(self, value: RptAccessEnum) -> "RptExecutableEntityEvent":
        """
        Sets the RPT access type.

        Args:
            value: RPT access enum value to set

        Returns:
            self for method chaining
        """
        self.rptAccess = value
        return self

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptExecutionContext(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    Represents an RPT execution context in AUTOSAR.
    Defines the execution context for RPT functionality.
    """


    def __init__(self) -> None:
        """
        Initializes the RptExecutionContext with default values.
        """
        super().__init__()
        self.contextRef: Union[Union[RefType, None] , None] = None

    def getContextRef(self) -> Union[RefType, None]:
        """
        Gets the context reference.

        Returns:
            Reference to the context
        """
        return self.contextRef

    def setContextRef(self, value: RefType) -> "RptExecutionContext":
        """
        Sets the context reference.

        Args:
            value: The context reference to set

        Returns:
            self for method chaining
        """
        self.contextRef = value
        return self

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptAccessEnum import (
    RptAccessEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptServicePoint(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    Represents an RPT service point in AUTOSAR.
    Defines a service point that supports read-protect-transform functionality.
    """


    def __init__(self) -> None:
        """
        Initializes the RptServicePoint with default values.
        """
        super().__init__()
        self.operationRef: Union[Union[RefType, None] , None] = None
        self.rptAccess: Union[Union[RptAccessEnum, None] , None] = None

    def getOperationRef(self) -> Union[RefType, None]:
        """
        Gets the operation reference.

        Returns:
            Reference to the operation
        """
        return self.operationRef

    def setOperationRef(self, value: RefType) -> "RptServicePoint":
        """
        Sets the operation reference.

        Args:
            value: The operation reference to set

        Returns:
            self for method chaining
        """
        self.operationRef = value
        return self

    def getRptAccess(self) -> Union[RptAccessEnum, None]:
        """
        Gets the RPT access type.

        Returns:
            RPT access enum value
        """
        return self.rptAccess

    def setRptAccess(self, value: RptAccessEnum) -> "RptServicePoint":
        """
        Sets the RPT access type.

        Args:
            value: RPT access enum value to set

        Returns:
            self for method chaining
        """
        self.rptAccess = value
        return self
