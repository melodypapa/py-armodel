from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ..GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean, ARLiteral, ARNumerical

class BswModuleEntry(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.service_id = None                      # type: ARNumerical
        self.is_reentrant = None                    # type: ARBoolean
        self.is_synchronous = None                  # type: ARBoolean
        self.call_type = None                       # type: ARLiteral
        self._execution_context = None              # type: ARLiteral
        self._sw_service_impl_policy = None         # type: ARLiteral

    @property
    def execution_context(self):
        return self._execution_context

    @execution_context.setter
    def execution_context(self, value):
        if value.upper() not in ("HOOK", "INTERRUPT-CAT-1", "INTERRUPT-CAT-2", "TASK", "UNSPECIFIED"):
            raise ValueError("Invalid execution context <%s> of BswModuleEntry <%s>" % (value, self.short_name))
        self._execution_context = value

    @property
    def sw_service_impl_policy(self):
        return self._sw_service_impl_policy

    @sw_service_impl_policy.setter
    def sw_service_impl_policy(self, value):
        if value.upper() not in ("INLINE", "INLINE-CONDITIONAL", "MACRO", "STANDARD"):
            raise ValueError("Invalid SwServiceImplPolicy <%s> of BswModuleEntry <%s>" % (value, self.short_name))
        self._sw_service_impl_policy = value

    def __str__(self) -> str:
        result = []
        result.append("short_name             : %s" % self.short_name)
        if self.service_id != None:
            result.append("service_id             : %d" % self.service_id)
        if self.is_reentrant != None:
            result.append("is_reentrant           : %s" % self.is_reentrant)
        if self.is_synchronous != None:
            result.append("is_synchronous         : %s" % self.is_synchronous)
        if self.call_type != None:
            result.append("call_type              : %s" % self.call_type)
        if self.execution_context != None:
            result.append("execution_context      : %s" % self.execution_context)
        if self.sw_service_impl_policy != None:
            result.append("sw_service_impl_policy : %s" % self.sw_service_impl_policy)

        return "\n".join(result)