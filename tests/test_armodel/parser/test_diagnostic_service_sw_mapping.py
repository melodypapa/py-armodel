"""Parser tests for DiagnosticServiceSwMapping (Table 5.15, p.239).

XSD group DIAGNOSTIC-SERVICE-SW-MAPPING (AUTOSAR_00052.xsd l.43883) element
order: ACCESSED-DATA-PROTOTYPE-IREF, DIAGNOSTIC-DATA-ELEMENT-REF,
DIAGNOSTIC-PARAMETER-REF, MAPPED-BSW-SERVICE-DEPENDENCY-REF,
MAPPED-FLAT-SWC-SERVICE-DEPENDENCY-REF,
MAPPED-SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF, PARAMETER-ELEMENT-ACCESS,
SERVICE-INSTANCE-REF (MAPPED-SWC-SERVICE-DEPENDENCY-IREF XSD-only, not modeled).
Base DIAGNOSTIC-MAPPING group is read by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticServiceSwMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-SERVICE-SW-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticServiceSwMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticServiceSwMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<ACCESSED-DATA-PROTOTYPE-IREF DEST='DATA-PROTOTYPE'>/AUTOSAR/Interfaces/Op1</ACCESSED-DATA-PROTOTYPE-IREF>"
            "<DIAGNOSTIC-DATA-ELEMENT-REF DEST='DIAGNOSTIC-DATA-ELEMENT'>/AUTOSAR/DataElements/Did1</DIAGNOSTIC-DATA-ELEMENT-REF>"
            "<DIAGNOSTIC-PARAMETER-REF DEST='DIAGNOSTIC-PARAMETER-IDENT'>/AUTOSAR/ParamIdents/Ident1</DIAGNOSTIC-PARAMETER-REF>"
            "<MAPPED-BSW-SERVICE-DEPENDENCY-REF DEST='BSW-SERVICE-DEPENDENCY-IDENT'>/AUTOSAR/BswDeps/Dep1</MAPPED-BSW-SERVICE-DEPENDENCY-REF>"
            "<MAPPED-FLAT-SWC-SERVICE-DEPENDENCY-REF DEST='SWC-SERVICE-DEPENDENCY'>/AUTOSAR/SwcDeps/Dep2</MAPPED-FLAT-SWC-SERVICE-DEPENDENCY-REF>"
            "<MAPPED-SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF DEST='SWC-SERVICE-DEPENDENCY'>/AUTOSAR/System/SwcDep3</MAPPED-SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF>"
            "<PARAMETER-ELEMENT-ACCESS>"
            "<TARGET-ELEMENT-REF DEST='DIAGNOSTIC-PARAMETER-ELEMENT'>/AUTOSAR/ParamElements/Target</TARGET-ELEMENT-REF>"
            "</PARAMETER-ELEMENT-ACCESS>"
            "<SERVICE-INSTANCE-REF DEST='DIAGNOSTIC-SERVICE-INSTANCE'>/AUTOSAR/Services/Svc1</SERVICE-INSTANCE-REF>"
        )
        parser.readDiagnosticServiceSwMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getAccessedDataPrototypeIRef().getValue() == "/AUTOSAR/Interfaces/Op1"
        assert mapping.getDiagnosticDataElementRef().getValue() == "/AUTOSAR/DataElements/Did1"
        assert mapping.getDiagnosticParameterRef().getValue() == "/AUTOSAR/ParamIdents/Ident1"
        assert mapping.getMappedBswServiceDependencyRef().getValue() == "/AUTOSAR/BswDeps/Dep1"
        assert mapping.getMappedFlatSwcServiceDependencyRef().getValue() == "/AUTOSAR/SwcDeps/Dep2"
        assert mapping.getMappedSwcServiceDependencyInSystemIRef().getValue() == "/AUTOSAR/System/SwcDep3"
        assert mapping.getParameterElementAccess() is not None
        assert mapping.getParameterElementAccess().getTargetElementRef().getValue() == "/AUTOSAR/ParamElements/Target"
        assert mapping.getServiceInstanceRef().getValue() == "/AUTOSAR/Services/Svc1"

    def test_read_empty(self, parser):
        mapping = DiagnosticServiceSwMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticServiceSwMapping(element, mapping)
        assert mapping.getAccessedDataPrototypeIRef() is None
        assert mapping.getDiagnosticDataElementRef() is None
        assert mapping.getDiagnosticParameterRef() is None
        assert mapping.getMappedBswServiceDependencyRef() is None
        assert mapping.getMappedFlatSwcServiceDependencyRef() is None
        assert mapping.getMappedSwcServiceDependencyInSystemIRef() is None
        assert mapping.getParameterElementAccess() is None
        assert mapping.getServiceInstanceRef() is None
