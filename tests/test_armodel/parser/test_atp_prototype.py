"""
Regression tests for AtpPrototype (Table 5.4) reader/writer coverage.

AtpPrototype is abstract and its single attribute `atpType` (AtpType, 1, ref) is
marked `<<atpDerived>>` in the XSD ATP-PROTOTYPE group (comment: "Association
<<atpDerived>>atpType skipped"). Therefore there is no XML element for atpType and
no dedicated readAtpPrototype/writeAtpPrototype: inherited members are reached
through the shared readAtpFeature/writeAtpFeature helpers. Steps 5/6 are N/A;
this test pins that N/A contract so a future regression (e.g. someone adding a
spurious ATP-TYPE element) is caught.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestAtpPrototypeReaderWriter:
    """
    Confirm AtpPrototype has no own XML element mapping (atpType is atpDerived).
    """

    def test_no_dedicated_reader_writer_methods(self):
        assert not hasattr(ARXMLParser, "readAtpPrototype")
        assert not hasattr(ARXMLWriter, "writeAtpPrototype")

    def test_atp_type_is_in_memory_derived_field(self):
        """
        atpType exists as an in-memory field but is not serialized: it survives
        set/get, confirming the model carries it, while no XML element exists.
        """

        class ConcreteAtpPrototype(AtpPrototype):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = ConcreteAtpPrototype(ar_root, "MyProto")
        ref = RefType().setValue("/T/MyType").setDest("ATP-TYPE--SUBTYPES-ENUM")
        obj.setAtpTypeRef(ref)
        assert obj.getAtpTypeRef() is ref
