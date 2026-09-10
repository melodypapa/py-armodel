import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ArVariableInImplementationDataInstanceRef, AutosarVariableRef
from armodel.writer.arxml_writer import ARXMLWriter


def _ref(value: str) -> RefType:
    return RefType().setValue(value)


def test_write_ar_variable_implementation_data_instance_ref_in_xsd_order():
    writer = ARXMLWriter()
    implementation_ref = ArVariableInImplementationDataInstanceRef()
    implementation_ref.setPortPrototypeRef(_ref("/Port"))
    implementation_ref.setRootVariableDataPrototypeRef(_ref("/Root"))
    implementation_ref.addContextDataPrototypeRef(_ref("/Context1"))
    implementation_ref.addContextDataPrototypeRef(_ref("/Context2"))
    implementation_ref.setTargetDataPrototypeRef(_ref("/Target"))
    ref = AutosarVariableRef().setAutosarVariableInImplDatatype(implementation_ref)

    element = ET.Element("ROOT")
    writer.setAutosarVariableRef(element, "AUTOSAR-VARIABLE-REF", ref)
    child = element.find("AUTOSAR-VARIABLE-REF/AUTOSAR-VARIABLE-IN-IMPL-DATATYPE")

    assert [item.tag for item in child] == [
        "PORT-PROTOTYPE-REF",
        "ROOT-VARIABLE-DATA-PROTOTYPE-REF",
        "CONTEXT-DATA-PROTOTYPE-REF",
        "CONTEXT-DATA-PROTOTYPE-REF",
        "TARGET-DATA-PROTOTYPE-REF",
    ]
    assert [item.text for item in child] == ["/Port", "/Root", "/Context1", "/Context2", "/Target"]
