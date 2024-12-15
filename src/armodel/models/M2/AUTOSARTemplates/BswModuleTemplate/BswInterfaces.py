from typing import List

from ....M2.MSR.DataDictionary.ServiceProcessTask import SwServiceArg
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical, Boolean, Identifier, NameToken

class BswModuleEntry(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arguments = []                         # type: List[SwServiceArg]
        self.bswEntryKind = None                    # type: BswEntryKindEnum
        self.callType = None                        # type: BswCallType
        self.executionContext = None                # type: BswExecutionContext
        self.functionPrototypeEmitter = None        # type: NameToken
        self.isReentrant = None                     # type: Boolean
        self.isSynchronous = None                   # type: Boolean
        self.returnType = None                      # type: SwServiceArg
        self.role = None                            # type: Identifier
        self.serviceId = None                       # type: ARNumerical
        self.swServiceImplPolicy = None             # type: SwServiceImplPolicyEnum

    def getArguments(self):
        return self.arguments

    def createArgument(self, short_name: str) -> SwServiceArg:
        if (short_name not in self.elements):
            arg = SwServiceArg(self, short_name)
            self.addElement(arg)
            self.arguments.append(arg)
        return self.getElement(short_name)

    def getBswEntryKind(self):
        return self.bswEntryKind

    def setBswEntryKind(self, value):
        self.bswEntryKind = value
        return self

    def getCallType(self):
        return self.callType

    def setCallType(self, value):
        self.callType = value
        return self

    def getExecutionContext(self):
        return self.executionContext

    def setExecutionContext(self, value):
        if value.upper() not in ("HOOK", "INTERRUPT-CAT-1", "INTERRUPT-CAT-2", "TASK", "UNSPECIFIED"):
            raise ValueError("Invalid execution context <%s> of BswModuleEntry <%s>" % (value, self.short_name))
        self.executionContext = value
        return self

    def getFunctionPrototypeEmitter(self):
        return self.functionPrototypeEmitter

    def setFunctionPrototypeEmitter(self, value):
        self.functionPrototypeEmitter = value
        return self

    def getIsReentrant(self):
        return self.isReentrant

    def setIsReentrant(self, value):
        self.isReentrant = value
        return self

    def getIsSynchronous(self):
        return self.isSynchronous

    def setIsSynchronous(self, value):
        self.isSynchronous = value
        return self

    def getReturnType(self):
        return self.returnType

    def setReturnType(self, value):
        self.returnType = value
        return self

    def getRole(self):
        return self.role

    def setRole(self, value):
        self.role = value
        return self

    def getServiceId(self):
        return self.serviceId

    def setServiceId(self, value):
        self.serviceId = value
        return self

    def getSwServiceImplPolicy(self):
        return self.swServiceImplPolicy

    def setSwServiceImplPolicy(self, value):
        if value.upper() not in ("INLINE", "INLINE-CONDITIONAL", "MACRO", "STANDARD"):
            raise ValueError("Invalid SwServiceImplPolicy <%s> of BswModuleEntry <%s>" % (value, self.short_name))
        self.swServiceImplPolicy = value
        return self

    def __str__(self) -> str:
        result = []

        result.append("short_name             : %s" % self.short_name)
        if self.serviceId != None:
            result.append("service_id             : %d" % self.serviceId)
        if self.isReentrant != None:
            result.append("is_reentrant           : %s" % self.isReentrant)
        if self.isSynchronous != None:
            result.append("is_synchronous         : %s" % self.isSynchronous)
        if self.callType != None:
            result.append("call_type              : %s" % self.callType)
        if self.execution_context != None:
            result.append("execution_context      : %s" % self.executionContext)
        if self.sw_service_impl_policy != None:
            result.append("sw_service_impl_policy : %s" % self.swServiceImplPolicy)

        return "\n".join(result)
    