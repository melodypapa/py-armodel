"""Writer round-trip tests for AutosarDataPrototype.typeTRef (SWCT Table 5.29).

type (AutosarDataType, 0..1, tref) is the class's only own attribute, serialized
as TYPE-TREF through the reusable writeAutosarDataPrototype helper that concrete
subclasses call; the XSD group AUTOSAR-DATA-PROTOTYPE emits it before subclass
elements (e.g. INIT-VALUE).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR, AUTOSARDoc
from armodel.models.M2.AUTOSARTemplates.CommonStructure import NumericalValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, TRefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class TestAutosarDataPrototypeWriter:
    def test_write_type_tref_field_values(self):
        AUTOSAR.getInstance().new()
        writer = ARXMLWriter()
        ar_root = AUTOSAR.getInstance().createARPackage("Pkg")
        prototype = ParameterDataPrototype(ar_root, "PP")

        type_ref = TRefType()
        type_ref.setValue("/DataTypes/UInt8")
        type_ref.setDest("IMPLEMENTATION-DATA-TYPE")
        prototype.setTypeTRef(type_ref)

        parent = ET.Element("PARENT")
        writer.writeParameterDataPrototype(parent, prototype)

        pdp = parent[0]
        assert pdp.tag == "PARAMETER-DATA-PROTOTYPE"
        type_tref = pdp.find("TYPE-TREF")
        assert type_tref.text == "/DataTypes/UInt8"
        assert type_tref.get("DEST") == "IMPLEMENTATION-DATA-TYPE"

    def test_write_type_tref_absent(self):
        AUTOSAR.getInstance().new()
        writer = ARXMLWriter()
        ar_root = AUTOSAR.getInstance().createARPackage("Pkg")
        prototype = ParameterDataPrototype(ar_root, "PP")

        parent = ET.Element("PARENT")
        writer.writeParameterDataPrototype(parent, prototype)

        pdp = parent[0]
        assert pdp.tag == "PARAMETER-DATA-PROTOTYPE"
        assert pdp.find("TYPE-TREF") is None

    def test_write_type_tref_before_subclass_elements(self):
        AUTOSAR.getInstance().new()
        writer = ARXMLWriter()
        ar_root = AUTOSAR.getInstance().createARPackage("Pkg")
        prototype = VariableDataPrototype(ar_root, "DE")

        type_ref = TRefType()
        type_ref.setValue("/DataTypes/UInt8")
        type_ref.setDest("IMPLEMENTATION-DATA-TYPE")
        prototype.setTypeTRef(type_ref)

        numerical = Numerical()
        numerical.setValue(42)
        init_value = NumericalValueSpecification()
        init_value.setValue(numerical)
        prototype.setInitValue(init_value)

        parent = ET.Element("PARENT")
        writer.writeVariableDataPrototype(parent, prototype)

        vdp = parent[0]
        children = [child.tag for child in vdp]
        assert children.index("TYPE-TREF") < children.index("INIT-VALUE")

    def test_round_trip_type_tref(self):
        AUTOSAR.getInstance().new()
        writer = ARXMLWriter()
        ar_root = AUTOSAR.getInstance().createARPackage("Pkg")
        sr_if = ar_root.createSenderReceiverInterface("SR")
        prototype = sr_if.createDataElement("DE")

        type_ref = TRefType()
        type_ref.setValue("/DataTypes/UInt8")
        type_ref.setDest("IMPLEMENTATION-DATA-TYPE")
        prototype.setTypeTRef(type_ref)

        parent = ET.Element("PARENT")
        writer.writeSenderReceiverInterface(parent, sr_if)
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Pkg</SHORT-NAME>
                    <ELEMENTS>
                        {ET.tostring(parent[0], encoding="unicode")}
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""  # xsd-skip: fragment embeds runtime ET.tostring(writer output); static scan cannot resolve it

        document = AUTOSARDoc()
        ARXMLParser().readARPackages(ET.fromstring(xml), document)

        sr_if_read = document.getARPackages()[0].getSenderReceiverInterfaces()[0]
        prototype_read = sr_if_read.getDataElements()[0]
        assert prototype_read.getShortName() == "DE"
        assert prototype_read.getTypeTRef().getValue() == "/DataTypes/UInt8"
        assert prototype_read.getTypeTRef().getDest() == "IMPLEMENTATION-DATA-TYPE"
