"""Writer round-trip tests for VariableDataPrototype (SWCT Table 5.31).

initValue (ValueSpecification, 0..1, aggr) is the class's only own attribute,
serialized as INIT-VALUE inside the VARIABLE-DATA-PROTOTYPE element, after
TYPE-TREF per the XSD group order.
"""

import xml.etree.cElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import NumericalValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from armodel.writer.arxml_writer import ARXMLWriter


class TestVariableDataPrototypeWriter:
    def test_write_field_values(self):
        AUTOSAR.getInstance().new()
        writer = ARXMLWriter()
        ar_root = AUTOSAR.getInstance().createARPackage("Pkg")
        prototype = VariableDataPrototype(ar_root, "DE")

        type_ref = RefType()
        type_ref.setValue("/DataTypes/UInt8")
        type_ref.setDest("IMPLEMENTATION-DATA-TYPE")
        prototype.setTypeTRef(type_ref)

        numerical = ARNumerical()
        numerical.setValue(42)
        init_value = NumericalValueSpecification()
        init_value.setValue(numerical)
        prototype.setInitValue(init_value)

        parent = ET.Element("PARENT")
        writer.writeVariableDataPrototype(parent, prototype)

        vdp = parent[0]
        assert vdp.tag == "VARIABLE-DATA-PROTOTYPE"
        type_tref = vdp.find("TYPE-TREF")
        assert type_tref.text == "/DataTypes/UInt8"
        assert type_tref.get("DEST") == "IMPLEMENTATION-DATA-TYPE"
        init_value_element = vdp.find("INIT-VALUE")
        assert init_value_element is not None
        assert init_value_element.find("NUMERICAL-VALUE-SPECIFICATION").find("VALUE").text == "42"
        children = [child.tag for child in vdp]
        assert children.index("TYPE-TREF") < children.index("INIT-VALUE")

    def test_write_no_init_value(self):
        AUTOSAR.getInstance().new()
        writer = ARXMLWriter()
        ar_root = AUTOSAR.getInstance().createARPackage("Pkg")
        prototype = VariableDataPrototype(ar_root, "DE")

        parent = ET.Element("PARENT")
        writer.writeVariableDataPrototype(parent, prototype)

        vdp = parent[0]
        assert vdp.tag == "VARIABLE-DATA-PROTOTYPE"
        assert vdp.find("INIT-VALUE") is None
