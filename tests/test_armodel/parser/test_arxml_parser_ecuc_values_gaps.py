"""Tests for ECUC Module Configuration Values handler gaps."""
import xml.etree.ElementTree as ET
import pytest
from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucContainerValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationISignalProps,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()


def _make_pkg():
    return _autosar_root().createARPackage("Pkg")


def _make_container_value(short_name="ContainerValue"):
    pkg = _make_pkg()
    return EcucContainerValue(pkg, short_name)


def _make_module_configuration_values(short_name="ModuleValues"):
    pkg = _make_pkg()
    return pkg.createEcucModuleConfigurationValues(short_name)


def _make_physical_dimension(short_name="PhysDim"):
    pkg = _make_pkg()
    return pkg.createPhysicalDimension(short_name)


def _make_isignal_group(short_name="ISignalGroup"):
    pkg = _make_pkg()
    return pkg.createISignalGroup(short_name)


class TestGetEcucInstanceReferenceValue:
    """Tests for getEcucInstanceReferenceValue (L5127-5131)."""

    def test_with_value_iref_and_definition_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <DEFINITION-REF DEST="ECUC-REFERENCE-DEF">/Path/To/Def</DEFINITION-REF>
            <VALUE-IREF>
                <BASE-REF DEST="SW-COMPONENT-TYPE">/Base/Path</BASE-REF>
                <CONTEXT-ELEMENT-REF DEST="R-PORT-PROTOTYPE">/Context/El1</CONTEXT-ELEMENT-REF>
                <TARGET-REF DEST="VARIABLE-DATA-PROTOTYPE">/Target/Path</TARGET-REF>
            </VALUE-IREF>
            """,
            root_tag="ECUC-INSTANCE-REFERENCE-VALUE",
        )
        value = parser.getEcucInstanceReferenceValue(element)
        assert value is not None
        assert value.getDefinitionRef() is not None
        iref = value.valueRef
        assert iref is not None
        assert iref.getBaseRef() is not None
        assert iref.getTargetRef() is not None
        assert len(iref.getContextElementRefs()) == 1

    def test_without_value_iref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <DEFINITION-REF DEST="ECUC-REFERENCE-DEF">/Path/To/Def</DEFINITION-REF>
            """,
            root_tag="ECUC-INSTANCE-REFERENCE-VALUE",
        )
        value = parser.getEcucInstanceReferenceValue(element)
        assert value is not None
        assert value.getDefinitionRef() is not None
        assert value.valueRef is None

    def test_with_annotations(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <DEFINITION-REF DEST="ECUC-REFERENCE-DEF">/Path/To/Def</DEFINITION-REF>
            <ANNOTATIONS>
                <ANNOTATION>
                    <LABEL>
                        <L-4 L="EN">Note</L-4>
                    </LABEL>
                </ANNOTATION>
            </ANNOTATIONS>
            """,
            root_tag="ECUC-INSTANCE-REFERENCE-VALUE",
        )
        value = parser.getEcucInstanceReferenceValue(element)
        assert value is not None
        assert len(value.getAnnotations()) == 1


class TestReadEcucContainerValueReferenceValues:
    """Tests for readEcucContainerValueReferenceValues (L5133-5141)."""

    def test_reads_ecuc_reference_value(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        container = _make_container_value()
        element = _snip(
            """
            <REFERENCE-VALUES>
                <ECUC-REFERENCE-VALUE>
                    <DEFINITION-REF DEST="ECUC-REFERENCE-DEF">/Path/To/RefDef</DEFINITION-REF>
                    <VALUE-REF DEST="SOME-ELEMENT">/Path/To/Target</VALUE-REF>
                </ECUC-REFERENCE-VALUE>
            </REFERENCE-VALUES>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucContainerValueReferenceValues(element, container)
        refs = container.getReferenceValues()
        assert len(refs) == 1

    def test_reads_ecuc_instance_reference_value(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        container = _make_container_value()
        element = _snip(
            """
            <REFERENCE-VALUES>
                <ECUC-INSTANCE-REFERENCE-VALUE>
                    <DEFINITION-REF DEST="ECUC-REFERENCE-DEF">/Path/To/RefDef</DEFINITION-REF>
                    <VALUE-IREF>
                        <BASE-REF DEST="SW-COMPONENT-TYPE">/Base/Path</BASE-REF>
                        <TARGET-REF DEST="VARIABLE-DATA-PROTOTYPE">/Target/Path</TARGET-REF>
                    </VALUE-IREF>
                </ECUC-INSTANCE-REFERENCE-VALUE>
            </REFERENCE-VALUES>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucContainerValueReferenceValues(element, container)
        refs = container.getReferenceValues()
        assert len(refs) == 1

    def test_reads_multiple_reference_values(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        container = _make_container_value()
        element = _snip(
            """
            <REFERENCE-VALUES>
                <ECUC-REFERENCE-VALUE>
                    <DEFINITION-REF DEST="ECUC-REFERENCE-DEF">/Path/To/RefDef1</DEFINITION-REF>
                    <VALUE-REF DEST="SOME-ELEMENT">/Path/To/Target1</VALUE-REF>
                </ECUC-REFERENCE-VALUE>
                <ECUC-INSTANCE-REFERENCE-VALUE>
                    <DEFINITION-REF DEST="ECUC-REFERENCE-DEF">/Path/To/RefDef2</DEFINITION-REF>
                    <VALUE-IREF>
                        <BASE-REF DEST="SW-COMPONENT-TYPE">/Base/Path</BASE-REF>
                        <TARGET-REF DEST="VARIABLE-DATA-PROTOTYPE">/Target/Path</TARGET-REF>
                    </VALUE-IREF>
                </ECUC-INSTANCE-REFERENCE-VALUE>
            </REFERENCE-VALUES>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucContainerValueReferenceValues(element, container)
        refs = container.getReferenceValues()
        assert len(refs) == 2

    def test_empty_reference_values(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        container = _make_container_value()
        element = _snip(
            """
            <REFERENCE-VALUES>
            </REFERENCE-VALUES>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucContainerValueReferenceValues(element, container)
        assert len(container.getReferenceValues()) == 0

    def test_unsupported_type_warning(self, warning_parser, caplog):
        AUTOSAR.getInstance().setARRelease("R23-11")
        container = _make_container_value()
        element = _snip(
            """
            <REFERENCE-VALUES>
                <ECUC-UNKNOWN-REF-VALUE>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </ECUC-UNKNOWN-REF-VALUE>
                <ECUC-REFERENCE-VALUE>
                    <DEFINITION-REF DEST="ECUC-REFERENCE-DEF">/Path/To/RefDef</DEFINITION-REF>
                    <VALUE-REF DEST="SOME-ELEMENT">/Path/To/Target</VALUE-REF>
                </ECUC-REFERENCE-VALUE>
            </REFERENCE-VALUES>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        import logging
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucContainerValueReferenceValues(element, container)
        assert any(
            "Unsupported EcucParameterValue" in rec.getMessage()
            for rec in caplog.records
        )
        assert len(container.getReferenceValues()) == 1


class TestReadEcucContainerValue:
    """Tests for readEcucContainerValue (L5143-5145)."""

    def test_full_handler_with_all_sections(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        container = _make_container_value("MyContainer")
        element = _snip(
            """
            <SHORT-NAME>MyContainer</SHORT-NAME>
            <DEFINITION-REF DEST="ECUC-PARAM-CONF-CONTAINER-DEF">/Path/To/ContainerDef</DEFINITION-REF>
            <PARAMETER-VALUES>
                <ECUC-TEXTUAL-PARAM-VALUE>
                    <DEFINITION-REF DEST="ECUC-STRING-PARAM-DEF">/Path/To/StringDef</DEFINITION-REF>
                    <VALUE>hello</VALUE>
                </ECUC-TEXTUAL-PARAM-VALUE>
            </PARAMETER-VALUES>
            <REFERENCE-VALUES>
                <ECUC-REFERENCE-VALUE>
                    <DEFINITION-REF DEST="ECUC-REFERENCE-DEF">/Path/To/RefDef</DEFINITION-REF>
                    <VALUE-REF DEST="SOME-ELEMENT">/Path/To/Target</VALUE-REF>
                </ECUC-REFERENCE-VALUE>
            </REFERENCE-VALUES>
            <SUB-CONTAINERS>
                <ECUC-CONTAINER-VALUE>
                    <SHORT-NAME>SubContainer</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
            </SUB-CONTAINERS>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucContainerValue(element, container)
        assert container.getDefinitionRef() is not None
        assert len(container.getParameterValues()) == 1
        assert len(container.getReferenceValues()) == 1
        assert len(container.getSubContainers()) == 1

    def test_minimal_handler_only_short_name(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        container = _make_container_value("MinimalContainer")
        element = _snip(
            """
            <SHORT-NAME>MinimalContainer</SHORT-NAME>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucContainerValue(element, container)
        assert container.getDefinitionRef() is None
        assert len(container.getParameterValues()) == 0
        assert len(container.getReferenceValues()) == 0
        assert len(container.getSubContainers()) == 0


class TestReadEcucContainerValueEcucContainerValue:
    """Tests for readEcucContainerValueEcucContainerValue (L5147-5148)."""

    def test_creates_sub_container_on_parent(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = _make_container_value("ParentContainer")
        element = _snip(
            """
            <SHORT-NAME>ChildContainer</SHORT-NAME>
            <DEFINITION-REF DEST="ECUC-PARAM-CONF-CONTAINER-DEF">/Path/To/ChildDef</DEFINITION-REF>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucContainerValueEcucContainerValue(element, parent)
        sub_containers = parent.getSubContainers()
        assert len(sub_containers) == 1
        assert sub_containers[0].getShortName() == "ChildContainer"
        assert sub_containers[0].getDefinitionRef() is not None


class TestReadEcucContainerValueSubContainers:
    """Tests for readEcucContainerValueSubContainers (L5150-5162)."""

    def test_reads_ecuc_container_value(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = _make_container_value("ParentContainer")
        element = _snip(
            """
            <SUB-CONTAINERS>
                <ECUC-CONTAINER-VALUE>
                    <SHORT-NAME>SubContainer1</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
                <ECUC-CONTAINER-VALUE>
                    <SHORT-NAME>SubContainer2</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
            </SUB-CONTAINERS>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucContainerValueSubContainers(element, parent)
        sub_containers = parent.getSubContainers()
        assert len(sub_containers) == 2
        assert sub_containers[0].getShortName() == "SubContainer1"
        assert sub_containers[1].getShortName() == "SubContainer2"

    def test_empty_sub_containers(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = _make_container_value("ParentContainer")
        element = _snip(
            """
            <SUB-CONTAINERS>
            </SUB-CONTAINERS>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucContainerValueSubContainers(element, parent)
        assert len(parent.getSubContainers()) == 0

    def test_unsupported_type_warning(self, warning_parser, caplog):
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = _make_container_value("ParentContainer")
        element = _snip(
            """
            <SUB-CONTAINERS>
                <ECUC-UNKNOWN-CONTAINER>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </ECUC-UNKNOWN-CONTAINER>
                <ECUC-CONTAINER-VALUE>
                    <SHORT-NAME>ValidSub</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
            </SUB-CONTAINERS>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        import logging
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucContainerValueSubContainers(element, parent)
        assert any(
            "Unsupported Sub Container" in rec.getMessage()
            for rec in caplog.records
        )
        assert len(parent.getSubContainers()) == 1


class TestReadEcucModuleConfigurationValuesEcucContainerValue:
    """Tests for readEcucModuleConfigurationValuesEcucContainerValue (L5164-5170)."""

    def test_creates_container_on_parent(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        values = _make_module_configuration_values("ModuleValues")
        element = _snip(
            """
            <SHORT-NAME>TopContainer</SHORT-NAME>
            <DEFINITION-REF DEST="ECUC-PARAM-CONF-CONTAINER-DEF">/Path/To/ContainerDef</DEFINITION-REF>
            """,
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucModuleConfigurationValuesEcucContainerValue(element, values)
        containers = values.getContainers()
        assert len(containers) == 1
        assert containers[0].getShortName() == "TopContainer"
        assert containers[0].getDefinitionRef() is not None


class TestReadEcucModuleConfigurationValuesContainers:
    """Tests for readEcucModuleConfigurationValuesContainers (L5172-5184)."""

    def test_reads_ecuc_container_value(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        values = _make_module_configuration_values("ModuleValues")
        element = _snip(
            """
            <CONTAINERS>
                <ECUC-CONTAINER-VALUE>
                    <SHORT-NAME>Container1</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
                <ECUC-CONTAINER-VALUE>
                    <SHORT-NAME>Container2</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
            </CONTAINERS>
            """,
            root_tag="ECUC-MODULE-CONFIGURATION-VALUES",
        )
        parser.readEcucModuleConfigurationValuesContainers(element, values)
        containers = values.getContainers()
        assert len(containers) == 2

    def test_empty_containers(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        values = _make_module_configuration_values("ModuleValues")
        element = _snip(
            """
            <CONTAINERS>
            </CONTAINERS>
            """,
            root_tag="ECUC-MODULE-CONFIGURATION-VALUES",
        )
        parser.readEcucModuleConfigurationValuesContainers(element, values)
        assert len(values.getContainers()) == 0

    def test_unsupported_type_warning(self, warning_parser, caplog):
        AUTOSAR.getInstance().setARRelease("R23-11")
        values = _make_module_configuration_values("ModuleValues")
        element = _snip(
            """
            <CONTAINERS>
                <ECUC-UNKNOWN-CONTAINER>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </ECUC-UNKNOWN-CONTAINER>
                <ECUC-CONTAINER-VALUE>
                    <SHORT-NAME>ValidContainer</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
            </CONTAINERS>
            """,
            root_tag="ECUC-MODULE-CONFIGURATION-VALUES",
        )
        import logging
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucModuleConfigurationValuesContainers(element, values)
        assert any(
            "Unsupported Container" in rec.getMessage()
            for rec in caplog.records
        )
        assert len(values.getContainers()) == 1


class TestReadEcucModuleConfigurationValues:
    """Tests for readEcucModuleConfigurationValues (L5164-5184)."""

    def test_full_handler_with_all_fields(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        values = _make_module_configuration_values("ModuleValues")
        element = _snip(
            """
            <SHORT-NAME>ModuleValues</SHORT-NAME>
            <DEFINITION-REF DEST="ECUC-MODULE-DEF">/Path/To/ModuleDef</DEFINITION-REF>
            <IMPLEMENTATION-CONFIG-VARIANT>VARIANT-PRE-COMPILE</IMPLEMENTATION-CONFIG-VARIANT>
            <MODULE-DESCRIPTION-REF DEST="ECUC-MODULE-DEF">/Path/To/ModuleDesc</MODULE-DESCRIPTION-REF>
            <CONTAINERS>
                <ECUC-CONTAINER-VALUE>
                    <SHORT-NAME>TopContainer</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
            </CONTAINERS>
            """,
            root_tag="ECUC-MODULE-CONFIGURATION-VALUES",
        )
        parser.readEcucModuleConfigurationValues(element, values)
        assert values.getDefinitionRef() is not None
        assert values.getImplementationConfigVariant() is not None
        assert values.getModuleDescriptionRef() is not None
        assert len(values.getContainers()) == 1

    def test_minimal_handler_only_short_name(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        values = _make_module_configuration_values("MinimalModule")
        element = _snip(
            """
            <SHORT-NAME>MinimalModule</SHORT-NAME>
            """,
            root_tag="ECUC-MODULE-CONFIGURATION-VALUES",
        )
        parser.readEcucModuleConfigurationValues(element, values)
        assert values.getDefinitionRef() is None
        assert values.getImplementationConfigVariant() is None
        assert values.getModuleDescriptionRef() is None
        assert len(values.getContainers()) == 0


class TestReadPhysicalDimension:
    """Tests for readPhysicalDimension (L5186-5196)."""

    def test_with_all_exponents(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        dim = _make_physical_dimension("PhysDim")
        element = _snip(
            """
            <SHORT-NAME>PhysDim</SHORT-NAME>
            <LENGTH-EXP>1</LENGTH-EXP>
            <LUMINOUS-INTENSITY-EXP>2</LUMINOUS-INTENSITY-EXP>
            <MASS-EXP>3</MASS-EXP>
            <MOLAR-AMOUNT-EXP>4</MOLAR-AMOUNT-EXP>
            <TEMPERATURE-EXP>5</TEMPERATURE-EXP>
            <TIME-EXP>6</TIME-EXP>
            <CURRENT-EXP>7</CURRENT-EXP>
            """,
            root_tag="PHYSICAL-DIMENSION",
        )
        parser.readPhysicalDimension(element, dim)
        assert dim.getLengthExp() is not None
        assert dim.getLuminousIntensityExp() is not None
        assert dim.getMassExp() is not None
        assert dim.getMolarAmountExp() is not None
        assert dim.getTemperatureExp() is not None
        assert dim.getTimeExp() is not None
        assert dim.getCurrentExp() is not None

    def test_without_exponents(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        dim = _make_physical_dimension("EmptyDim")
        element = _snip(
            """
            <SHORT-NAME>EmptyDim</SHORT-NAME>
            """,
            root_tag="PHYSICAL-DIMENSION",
        )
        parser.readPhysicalDimension(element, dim)
        assert dim.getLengthExp() is None
        assert dim.getLuminousIntensityExp() is None
        assert dim.getMassExp() is None
        assert dim.getMolarAmountExp() is None
        assert dim.getTemperatureExp() is None
        assert dim.getTimeExp() is None
        assert dim.getCurrentExp() is None


class TestReadISignalGroupISignalRef:
    """Tests for readISignalGroupISignalRef (L5197-5199)."""

    def test_reads_signal_refs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <I-SIGNAL-REFS>
                <I-SIGNAL-REF DEST="I-SIGNAL">/sig/Signal1</I-SIGNAL-REF>
                <I-SIGNAL-REF DEST="I-SIGNAL">/sig/Signal2</I-SIGNAL-REF>
            </I-SIGNAL-REFS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupISignalRef(element, group)
        refs = group.getISignalRefs()
        assert len(refs) == 2

    def test_empty_signal_refs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <I-SIGNAL-REFS>
            </I-SIGNAL-REFS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupISignalRef(element, group)
        assert len(group.getISignalRefs()) == 0


class TestReadISignalGroupComBasedSignalGroupTransformation:
    """Tests for readISignalGroupComBasedSignalGroupTransformation (L5201-5203)."""

    def test_reads_transformation_refs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS>
                <DATA-TRANSFORMATION-REF-CONDITIONAL>
                    <DATA-TRANSFORMATION-REF DEST="DATA-TRANSFORMATION">/trans/Trans1</DATA-TRANSFORMATION-REF>
                </DATA-TRANSFORMATION-REF-CONDITIONAL>
                <DATA-TRANSFORMATION-REF-CONDITIONAL>
                    <DATA-TRANSFORMATION-REF DEST="DATA-TRANSFORMATION">/trans/Trans2</DATA-TRANSFORMATION-REF>
                </DATA-TRANSFORMATION-REF-CONDITIONAL>
            </COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupComBasedSignalGroupTransformation(element, group)
        refs = group.getComBasedSignalGroupTransformationRefs()
        assert len(refs) == 2

    def test_empty_transformations(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS>
            </COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupComBasedSignalGroupTransformation(element, group)
        assert len(group.getComBasedSignalGroupTransformationRefs()) == 0


class TestReadTransformationISignalProps:
    """Tests for readTransformationISignalProps (L5205-5206)."""

    def test_reads_arobject_attributes(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = ET.fromstring(
            f"<END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL "
            f"xmlns='{NS}' T='2024-01-01T00:00:00' UUID='abc-123'>"
            f"</END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>"
        )
        parser.readTransformationISignalProps(element, props)
        assert props.timestamp == "2024-01-01T00:00:00"
        assert props.uuid == "abc-123"

    def test_without_arobject_attributes(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            "",
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL",
        )
        parser.readTransformationISignalProps(element, props)
        assert props.timestamp is None
        assert props.uuid is None


class TestReadEndToEndTransformationISignalPropsDataIds:
    """Tests for readEndToEndTransformationISignalPropsDataIds (L5208-5211)."""

    def test_with_data_ids(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            """
            <DATA-IDS>
                <DATA-ID>1</DATA-ID>
            </DATA-IDS>
            """,
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL",
        )
        parser.readEndToEndTransformationISignalPropsDataIds(element, props)
        data_ids = props.getDataIds()
        assert len(data_ids) == 1

    def test_without_data_ids(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            "",
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL",
        )
        parser.readEndToEndTransformationISignalPropsDataIds(element, props)
        assert len(props.getDataIds()) == 0


class TestReadEndToEndTransformationISignalProps:
    """Tests for readEndToEndTransformationISignalProps (L5213-5219)."""

    def test_full_handler_with_all_fields(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            """
            <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                    <TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/trans/Tech1</TRANSFORMER-REF>
                    <DATA-IDS>
                        <DATA-ID>1</DATA-ID>
                    </DATA-IDS>
                    <DATA-LENGTH>64</DATA-LENGTH>
                </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
            </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
            """,
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS",
        )
        parser.readEndToEndTransformationISignalProps(element, props)
        assert props.getTransformerRef() is not None
        assert len(props.getDataIds()) == 1
        assert props.getDataLength() is not None

    def test_without_variants_element(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            "",
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS",
        )
        parser.readEndToEndTransformationISignalProps(element, props)
        assert props.getTransformerRef() is None
        assert len(props.getDataIds()) == 0
        assert props.getDataLength() is None

    def test_minimal_variants_only_transformer_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            """
            <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                    <TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/trans/Tech1</TRANSFORMER-REF>
                </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
            </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
            """,
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS",
        )
        parser.readEndToEndTransformationISignalProps(element, props)
        assert props.getTransformerRef() is not None
        assert len(props.getDataIds()) == 0
        assert props.getDataLength() is None


class TestReadISignalGroupTransformationISignalProps:
    """Tests for readISignalGroupTransformationISignalProps (L5221-5229)."""

    def test_reads_end_to_end_transformation_props(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <TRANSFORMATION-I-SIGNAL-PROPSS>
                <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
                    <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                        <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                            <TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/trans/Tech1</TRANSFORMER-REF>
                            <DATA-IDS>
                                <DATA-ID>1</DATA-ID>
                            </DATA-IDS>
                            <DATA-LENGTH>32</DATA-LENGTH>
                        </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                    </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
            </TRANSFORMATION-I-SIGNAL-PROPSS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupTransformationISignalProps(element, group)
        props = group.getTransformationISignalProps()
        assert props is not None
        assert props.getTransformerRef() is not None
        assert len(props.getDataIds()) == 1
        assert props.getDataLength() is not None

    def test_empty_transformation_props(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <TRANSFORMATION-I-SIGNAL-PROPSS>
            </TRANSFORMATION-I-SIGNAL-PROPSS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupTransformationISignalProps(element, group)
        assert group.getTransformationISignalProps() is None

    def test_unsupported_type_warning(self, warning_parser, caplog):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <TRANSFORMATION-I-SIGNAL-PROPSS>
                <UNKNOWN-TRANSFORMATION-PROPS>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-TRANSFORMATION-PROPS>
                <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
                    <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                        <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                            <TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/trans/Tech1</TRANSFORMER-REF>
                        </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                    </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
            </TRANSFORMATION-I-SIGNAL-PROPSS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        import logging
        with caplog.at_level(logging.ERROR):
            warning_parser.readISignalGroupTransformationISignalProps(element, group)
        assert any(
            "Unsupported TransformationISignalProps" in rec.getMessage()
            for rec in caplog.records
        )
        props = group.getTransformationISignalProps()
        assert props is not None
        assert props.getTransformerRef() is not None
