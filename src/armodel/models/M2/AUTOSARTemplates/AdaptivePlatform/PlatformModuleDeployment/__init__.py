from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.AdaptiveModuleImplementation import (  # noqa: F401
    PlatformModuleEndpointConfiguration,
    PlatformModuleEthernetEndpointConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment import (  # noqa: F401
    CryptoKeySlot,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import (  # noqa: F401
    FirewallRule,
    FirewallRuleProps,
    StateDependentFirewall,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem import (
    # noqa: F401     IdsPlatformInstantiation,
    IdsmModuleInstantiation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (  # noqa: F401
    IdsmTrafficLimitation,
    SecurityEventAggregationFilter,
    SecurityEventContextProps,
    SecurityEventStateFilter,
)

# ARPackage re-exports are lazy: an eager import here would close an import-time cycle
# (ARPackage imports this module's ARElement bases transitively); PEP 562 __getattr__
# keeps `from ...PlatformModuleDeployment import X` and wildcard imports working.
from importlib import import_module as _import_module  # noqa: E402

_LAZY_IMPORTS = {
    "IdsmInstance": "armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage",
    "SecurityEventContextMapping": "armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage",
    "SecurityEventContextMappingCommConnector": "armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage",
    "SecurityEventFilterChain": "armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage",
}


def __getattr__(name):
    try:
        module_name = _LAZY_IMPORTS[name]
    except KeyError:
        raise AttributeError("module %r has no attribute %r" % (__name__, name))
    return getattr(_import_module(module_name), name)


__all__ = [
    "SecurityEventStateFilter",
    "SecurityEventFilterChain",
    "SecurityEventContextProps",
    "SecurityEventContextMappingCommConnector",
    "SecurityEventContextMapping",
    "SecurityEventAggregationFilter",
    "IdsmTrafficLimitation",
    "IdsmInstance",
    "PlatformModuleEndpointConfiguration",
    "PlatformModuleEthernetEndpointConfiguration",
    "CryptoKeySlot",
    "FirewallRule",
    "FirewallRuleProps",
    "StateDependentFirewall",
    "IdsPlatformInstantiation",
    "IdsmModuleInstantiation",
]
