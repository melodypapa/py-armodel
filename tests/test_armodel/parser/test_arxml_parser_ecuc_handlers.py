"""Tests for ECUC (ECU Configuration) parsing handlers."""

import logging
import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest
from armodel.models import AUTOSAR
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


class TestEcucContainerDefParameters:
    """Tests for readEcucContainerDefParameters handler."""

    def test_readEcucBooleanParamDef_with_value(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-BOOLEAN-PARAM-DEF>
                    <SHORT-NAME>EnableFeature</SHORT-NAME>
                    <DEFAULT-VALUE>true</DEFAULT-VALUE>
                </ECUC-BOOLEAN-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "EnableFeature"
        assert params[0].getDefaultValue() is not None
        assert params[0].getDefaultValue().getValue() == True

    def test_readEcucBooleanParamDef_without_value(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-BOOLEAN-PARAM-DEF>
                    <SHORT-NAME>EnableFeature</SHORT-NAME>
                </ECUC-BOOLEAN-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "EnableFeature"
        assert params[0].getDefaultValue() is None

    def test_readEcucStringParamDef_with_default(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-STRING-PARAM-DEF>
                    <SHORT-NAME>ConfigString</SHORT-NAME>
                    <DEFAULT-VALUE>default_value</DEFAULT-VALUE>
                    <MAX-LENGTH>100</MAX-LENGTH>
                    <MIN-LENGTH>1</MIN-LENGTH>
                </ECUC-STRING-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "ConfigString"
        assert params[0].getDefaultValue() is not None
        assert params[0].getMaxLength().getValue() == 100
        assert params[0].getMinLength().getValue() == 1

    def test_readEcucStringParamDef_without_default(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-STRING-PARAM-DEF>
                    <SHORT-NAME>ConfigString</SHORT-NAME>
                </ECUC-STRING-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "ConfigString"
        assert params[0].getDefaultValue() is None

    def test_readEcucIntegerParamDef_with_limits(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-INTEGER-PARAM-DEF>
                    <SHORT-NAME>MaxRetries</SHORT-NAME>
                    <DEFAULT-VALUE>10</DEFAULT-VALUE>
                    <MAX>100</MAX>
                    <MIN>0</MIN>
                </ECUC-INTEGER-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "MaxRetries"
        assert params[0].getDefaultValue().getValue() == 10
        assert params[0].getMax().getValue() == 100
        assert params[0].getMin().getValue() == 0

    def test_readEcucIntegerParamDef_without_limits(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-INTEGER-PARAM-DEF>
                    <SHORT-NAME>Counter</SHORT-NAME>
                </ECUC-INTEGER-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "Counter"
        assert params[0].getDefaultValue() is None
        assert params[0].getMax() is None
        assert params[0].getMin() is None

    def test_readEcucFloatParamDef_with_limits(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-FLOAT-PARAM-DEF>
                    <SHORT-NAME>Tolerance</SHORT-NAME>
                    <DEFAULT-VALUE>0.5</DEFAULT-VALUE>
                    <MAX>
                        <VALUE>10.0</VALUE>
                        <INTERVAL-TYPE>CLOSED</INTERVAL-TYPE>
                    </MAX>
                    <MIN>
                        <VALUE>0.0</VALUE>
                        <INTERVAL-TYPE>CLOSED</INTERVAL-TYPE>
                    </MIN>
                </ECUC-FLOAT-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "Tolerance"
        assert params[0].getDefaultValue() is not None

    def test_readEcucFloatParamDef_without_limits(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-FLOAT-PARAM-DEF>
                    <SHORT-NAME>Ratio</SHORT-NAME>
                </ECUC-FLOAT-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "Ratio"
        assert params[0].getDefaultValue() is None

    def test_readEcucEnumerationParamDef_with_literals(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-ENUMERATION-PARAM-DEF>
                    <SHORT-NAME>Mode</SHORT-NAME>
                    <DEFAULT-VALUE>STANDARD</DEFAULT-VALUE>
                    <LITERALS>
                        <ECUC-ENUMERATION-LITERAL-DEF>
                            <SHORT-NAME>STANDARD</SHORT-NAME>
                        </ECUC-ENUMERATION-LITERAL-DEF>
                        <ECUC-ENUMERATION-LITERAL-DEF>
                            <SHORT-NAME>ADVANCED</SHORT-NAME>
                        </ECUC-ENUMERATION-LITERAL-DEF>
                    </LITERALS>
                </ECUC-ENUMERATION-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "Mode"
        assert params[0].getDefaultValue() is not None
        literals = params[0].getLiterals()
        assert len(literals) == 2

    def test_readEcucEnumerationParamDef_without_literals(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-ENUMERATION-PARAM-DEF>
                    <SHORT-NAME>EmptyMode</SHORT-NAME>
                </ECUC-ENUMERATION-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "EmptyMode"
        assert params[0].getDefaultValue() is None

    def test_readEcucFunctionNameDef_with_value(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-FUNCTION-NAME-DEF>
                    <SHORT-NAME>InitFunction</SHORT-NAME>
                    <ECUC-FUNCTION-NAME-DEF-VARIANTS>
                        <ECUC-FUNCTION-NAME-DEF-CONDITIONAL>
                            <DEFAULT-VALUE>Init_MyModule</DEFAULT-VALUE>
                            <MIN-LENGTH>1</MIN-LENGTH>
                            <MAX-LENGTH>50</MAX-LENGTH>
                        </ECUC-FUNCTION-NAME-DEF-CONDITIONAL>
                    </ECUC-FUNCTION-NAME-DEF-VARIANTS>
                </ECUC-FUNCTION-NAME-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "InitFunction"

    def test_readEcucFunctionNameDef_without_value(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-FUNCTION-NAME-DEF>
                    <SHORT-NAME>CallbackFunc</SHORT-NAME>
                </ECUC-FUNCTION-NAME-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "CallbackFunc"

    def test_readEcucContainerDefParameters_multiple_types(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-BOOLEAN-PARAM-DEF>
                    <SHORT-NAME>Enable</SHORT-NAME>
                    <DEFAULT-VALUE>true</DEFAULT-VALUE>
                </ECUC-BOOLEAN-PARAM-DEF>
                <ECUC-STRING-PARAM-DEF>
                    <SHORT-NAME>Name</SHORT-NAME>
                    <DEFAULT-VALUE>default</DEFAULT-VALUE>
                </ECUC-STRING-PARAM-DEF>
                <ECUC-INTEGER-PARAM-DEF>
                    <SHORT-NAME>Count</SHORT-NAME>
                    <DEFAULT-VALUE>5</DEFAULT-VALUE>
                </ECUC-INTEGER-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 3
        assert params[0].getShortName() == "Enable"
        assert params[1].getShortName() == "Name"
        assert params[2].getShortName() == "Count"

    def test_readEcucContainerDefParameters_unsupported_type_warning(
        self, warning_parser
    ):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-UNKNOWN-PARAM-DEF>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </ECUC-UNKNOWN-PARAM-DEF>
                <ECUC-BOOLEAN-PARAM-DEF>
                    <SHORT-NAME>Enable</SHORT-NAME>
                </ECUC-BOOLEAN-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        warning_parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "Enable"


class TestEcucCommonAttributes:
    """Tests for readEcucCommonAttributes handler."""

    def test_readEcucCommonAttributes_with_multiplicity(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucBooleanParamDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        param = EcucBooleanParamDef(_autosar_root(), "ParamDef")
        element = _snip(
            """
            <SHORT-NAME>ParamDef</SHORT-NAME>
            <LOWER-MULTIPLICITY>1</LOWER-MULTIPLICITY>
            <UPPER-MULTIPLICITY>10</UPPER-MULTIPLICITY>
            """,
            root_tag="ECUC-BOOLEAN-PARAM-DEF",
        )
        parser.readEcucCommonAttributes(element, param)
        assert param.getLowerMultiplicity().getValue() == 1
        assert param.getUpperMultiplicity().getValue() == 10

    def test_readEcucCommonAttributes_with_origin(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucBooleanParamDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        param = EcucBooleanParamDef(_autosar_root(), "ParamDef")
        element = _snip(
            """
            <SHORT-NAME>ParamDef</SHORT-NAME>
            <ORIGIN>MANUFACTURER</ORIGIN>
            """,
            root_tag="ECUC-BOOLEAN-PARAM-DEF",
        )
        parser.readEcucCommonAttributes(element, param)
        assert param.getOrigin() is not None

    def test_readEcucCommonAttributes_with_multiplicity_config_classes(
        self, parser
    ):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucBooleanParamDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        param = EcucBooleanParamDef(_autosar_root(), "ParamDef")
        element = _snip(
            """
            <SHORT-NAME>ParamDef</SHORT-NAME>
            <MULTIPLICITY-CONFIG-CLASSES>
                <ECUC-MULTIPLICITY-CONFIGURATION-CLASS>
                    <CONFIG-CLASS>PRE-COMMIT</CONFIG-CLASS>
                    <CONFIG-VARIANT>VARIANT-1</CONFIG-VARIANT>
                </ECUC-MULTIPLICITY-CONFIGURATION-CLASS>
            </MULTIPLICITY-CONFIG-CLASSES>
            """,
            root_tag="ECUC-BOOLEAN-PARAM-DEF",
        )
        parser.readEcucCommonAttributes(element, param)
        cfg_classes = param.getMultiplicityConfigClasses()
        assert len(cfg_classes) == 1
        assert cfg_classes[0].getConfigClass() is not None
        assert cfg_classes[0].getConfigVariant() is not None

    def test_readEcucCommonAttributes_with_value_config_classes(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucBooleanParamDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        param = EcucBooleanParamDef(_autosar_root(), "ParamDef")
        element = _snip(
            """
            <SHORT-NAME>ParamDef</SHORT-NAME>
            <VALUE-CONFIG-CLASSES>
                <ECUC-VALUE-CONFIGURATION-CLASS>
                    <CONFIG-CLASS>POST-BUILD</CONFIG-CLASS>
                    <CONFIG-VARIANT>VARIANT-2</CONFIG-VARIANT>
                </ECUC-VALUE-CONFIGURATION-CLASS>
            </VALUE-CONFIG-CLASSES>
            """,
            root_tag="ECUC-BOOLEAN-PARAM-DEF",
        )
        parser.readEcucCommonAttributes(element, param)
        cfg_classes = param.getValueConfigClasses()
        assert len(cfg_classes) == 1
        assert cfg_classes[0].getConfigClass() is not None
        assert cfg_classes[0].getConfigVariant() is not None

    def test_readEcucCommonAttributes_with_post_build_variants(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucBooleanParamDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        param = EcucBooleanParamDef(_autosar_root(), "ParamDef")
        element = _snip(
            """
            <SHORT-NAME>ParamDef</SHORT-NAME>
            <POST-BUILD-VARIANT-MULTIPLICITY>true</POST-BUILD-VARIANT-MULTIPLICITY>
            <POST-BUILD-VARIANT-VALUE>false</POST-BUILD-VARIANT-VALUE>
            <REQUIRES-INDEX>true</REQUIRES-INDEX>
            """,
            root_tag="ECUC-BOOLEAN-PARAM-DEF",
        )
        parser.readEcucCommonAttributes(element, param)
        assert param.getPostBuildVariantMultiplicity() is not None
        assert param.getPostBuildVariantMultiplicity().getValue() == True
        assert param.getPostBuildVariantValue() is not None
        assert param.getPostBuildVariantValue().getValue() == False
        assert param.getRequiresIndex() is not None
        assert param.getRequiresIndex().getValue() == True


class TestEcucContainerDefReferences:
    """Tests for readEcucContainerDefReferences handler."""

    def test_readEcucSymbolicNameReferenceDef_with_destination(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <REFERENCES>
                <ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
                    <SHORT-NAME>TargetRef</SHORT-NAME>
                    <DESTINATION-REF DESTINATION="SomeType">/Path/To/Target</DESTINATION-REF>
                </ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
            </REFERENCES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefReferences(element, container)
        refs = container.getReferences()
        assert len(refs) == 1
        assert refs[0].getShortName() == "TargetRef"
        assert refs[0].getDestinationRef() is not None

    def test_readEcucSymbolicNameReferenceDef_without_destination(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <REFERENCES>
                <ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
                    <SHORT-NAME>EmptyRef</SHORT-NAME>
                </ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
            </REFERENCES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefReferences(element, container)
        refs = container.getReferences()
        assert len(refs) == 1
        assert refs[0].getShortName() == "EmptyRef"
        assert refs[0].getDestinationRef() is None

    def test_readEcucReferenceDef_with_destination(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <REFERENCES>
                <ECUC-REFERENCE-DEF>
                    <SHORT-NAME>ComponentRef</SHORT-NAME>
                    <DESTINATION-REF DESTINATION="SwComponentType">/Components/MyComponent</DESTINATION-REF>
                </ECUC-REFERENCE-DEF>
            </REFERENCES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefReferences(element, container)
        refs = container.getReferences()
        assert len(refs) == 1
        assert refs[0].getShortName() == "ComponentRef"

    def test_readEcucReferenceDef_without_destination(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <REFERENCES>
                <ECUC-REFERENCE-DEF>
                    <SHORT-NAME>OptionalRef</SHORT-NAME>
                </ECUC-REFERENCE-DEF>
            </REFERENCES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefReferences(element, container)
        refs = container.getReferences()
        assert len(refs) == 1
        assert refs[0].getShortName() == "OptionalRef"
        assert refs[0].getDestinationRef() is None

    def test_readEcucContainerDefReferences_unsupported_type_warning(
        self, warning_parser
    ):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.getInstance().setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <REFERENCES>
                <ECUC-UNKNOWN-REF-DEF>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </ECUC-UNKNOWN-REF-DEF>
                <ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
                    <SHORT-NAME>ValidRef</SHORT-NAME>
                </ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
            </REFERENCES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        warning_parser.readEcucContainerDefReferences(element, container)
        refs = container.getReferences()
        assert len(refs) == 1
        assert refs[0].getShortName() == "ValidRef"


# ===========================================================================
# Merged from test_arxml_parser_ecuc_values_gaps.py
# Tests for ECUC Module Configuration Values handlers (L5127-5184).
# ===========================================================================


def _make_pkg():
    return _autosar_root().createARPackage("Pkg")


def _make_container_value(short_name="ContainerValue"):
    from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
        EcucContainerValue,
    )
    pkg = _make_pkg()
    return EcucContainerValue(pkg, short_name)


def _make_module_configuration_values(short_name="ModuleValues"):
    pkg = _make_pkg()
    return pkg.createEcucModuleConfigurationValues(short_name)


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


# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestEcucContainerAndModuleDef:
    def _make_module_def(self):
        from armodel.models import EcucModuleDef
        return EcucModuleDef(parent=_autosar_root(), short_name="Md")

    def test_readEcucModuleDefSupportedConfigVariants_adds(
        self, parser
    ):
        module_def = self._make_module_def()
        element = _snip(
            "<SUPPORTED-CONFIG-VARIANTS>"
            "<SUPPORTED-CONFIG-VARIANT>V1</SUPPORTED-CONFIG-VARIANT>"
            "<SUPPORTED-CONFIG-VARIANT>V2</SUPPORTED-CONFIG-VARIANT>"
            "</SUPPORTED-CONFIG-VARIANTS>"
        )
        parser.readEcucModuleDefSupportedConfigVariants(
            element, module_def
        )
        assert len(module_def.getSupportedConfigVariants()) == 2

    def test_getEcucMultiplicityConfigurationClasses_unsupported_warns(
        self, warning_parser, caplog
    ):
        element = _snip(
            "<MULTIPLICITY-CONFIG-CLASSES><BAD/></MULTIPLICITY-CONFIG-CLASSES>"
        )
        with caplog.at_level(logging.ERROR):
            result = warning_parser.getEcucMultiplicityConfigurationClasses(
                element
            )
        assert result == []
        assert any("Unsupported MultiplicityConfigClass"
                   in r.getMessage() for r in caplog.records)

    def test_readEcucContainerDef_sets_attrs(self, parser):
        from armodel.models import EcucParamConfContainerDef
        container = EcucParamConfContainerDef(
            _autosar_root(), "Cd"
        )
        element = _snip(
            "<MULTIPLICITY-CONFIG-CLASSES>"
            "<ECUC-MULTIPLICITY-CONFIGURATION-CLASS>"
            "<CONFIG-CLASS>VARIANT</CONFIG-CLASS>"
            "<CONFIG-VARIANT>POST-BUILD</CONFIG-VARIANT>"
            "</ECUC-MULTIPLICITY-CONFIGURATION-CLASS>"
            "</MULTIPLICITY-CONFIG-CLASSES>"
            "<POST-BUILD-VARIANT-MULTIPLICITY>true</POST-BUILD-VARIANT-MULTIPLICITY>"
            "<REQUIRES-INDEX>true</REQUIRES-INDEX>"
            "<MULTIPLE-CONFIGURATION-CONTAINER>true</MULTIPLE-CONFIGURATION-CONTAINER>"
        )
        parser.readEcucContainerDef(element, container)
        assert len(container.getMultiplicityConfigClasses()) == 1
        assert container.getPostBuildVariantMultiplicity().getValue() is True

    def test_getEcucValueConfigurationClasses_unsupported_warns(
        self, warning_parser, caplog
    ):
        element = _snip(
            "<VALUE-CONFIG-CLASSES><BAD/></VALUE-CONFIG-CLASSES>"
        )
        with caplog.at_level(logging.ERROR):
            result = warning_parser.getEcucValueConfigurationClasses(
                element
            )
        assert result == []
        assert any("Unsupported ValueConfigClass" in r.getMessage()
                   for r in caplog.records)

    def test_readEcucEnumerationParamDefLiterals_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EcucEnumerationParamDef
        param_def = EcucEnumerationParamDef(
            _autosar_root(), "Enum"
        )
        element = _snip(
            "<LITERALS><BAD/></LITERALS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucEnumerationParamDefLiterals(
                element, param_def
            )
        assert any("Unsupported EnumerationLiteral" in r.getMessage()
                   for r in caplog.records)

    def test_readEcucContainerDefSubContainers_creates_sub(
        self, parser
    ):
        from armodel.models import EcucParamConfContainerDef
        container = EcucParamConfContainerDef(
            _autosar_root(), "Cd"
        )
        element = _snip(
            "<SUB-CONTAINERS>"
            "<ECUC-PARAM-CONF-CONTAINER-DEF>"
            "<SHORT-NAME>Sub</SHORT-NAME>"
            "</ECUC-PARAM-CONF-CONTAINER-DEF>"
            "</SUB-CONTAINERS>"
        )
        parser.readEcucContainerDefSubContainers(element, container)
        assert len(container.getSubContainers()) == 1

    def test_readEcucContainerDefSubContainers_choice(self, parser):
        from armodel.models import EcucParamConfContainerDef
        container = EcucParamConfContainerDef(
            _autosar_root(), "Cd"
        )
        element = _snip(
            "<SUB-CONTAINERS>"
            "<ECUC-CHOICE-CONTAINER-DEF>"
            "<SHORT-NAME>Ch</SHORT-NAME>"
            "</ECUC-CHOICE-CONTAINER-DEF>"
            "</SUB-CONTAINERS>"
        )
        parser.readEcucContainerDefSubContainers(element, container)
        assert len(container.getSubContainers()) == 1

    def test_readEcucContainerDefSubContainers_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EcucParamConfContainerDef
        container = EcucParamConfContainerDef(
            _autosar_root(), "Cd"
        )
        element = _snip(
            "<SUB-CONTAINERS><BAD/></SUB-CONTAINERS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucContainerDefSubContainers(
                element, container
            )
        assert any("Unsupported SubContainer" in r.getMessage()
                   for r in caplog.records)

    def test_readEcucParamConfContainerDef_full(self, parser):
        from armodel.models import EcucParamConfContainerDef
        container = EcucParamConfContainerDef(
            _autosar_root(), "Cd"
        )
        element = _snip(
            "<SHORT-NAME>Cd</SHORT-NAME>"
        )
        parser.readEcucParamConfContainerDef(element, container)

    def test_readEcucChoiceContainerDefChoices_creates(self, parser):
        from armodel.models import EcucChoiceContainerDef
        container = EcucChoiceContainerDef(
            _autosar_root(), "Ch"
        )
        element = _snip(
            "<CHOICES>"
            "<ECUC-PARAM-CONF-CONTAINER-DEF>"
            "<SHORT-NAME>C1</SHORT-NAME>"
            "</ECUC-PARAM-CONF-CONTAINER-DEF>"
            "</CHOICES>"
        )
        parser.readEcucChoiceContainerDefChoices(element, container)
        assert len(container.getChoices()) == 1

    def test_readEcucChoiceContainerDefChoices_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EcucChoiceContainerDef
        container = EcucChoiceContainerDef(
            _autosar_root(), "Ch"
        )
        element = _snip(
            "<CHOICES><BAD/></CHOICES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucChoiceContainerDefChoices(
                element, container
            )
        assert any("Unsupported Choice" in r.getMessage()
                   for r in caplog.records)

    def test_readEcucChoiceContainerDef_full(self, parser):
        from armodel.models import EcucChoiceContainerDef
        container = EcucChoiceContainerDef(
            _autosar_root(), "Ch"
        )
        element = _snip("<SHORT-NAME>Ch</SHORT-NAME>")
        parser.readEcucChoiceContainerDef(element, container)

    def test_readEcucModuleDefContainers_creates_param_conf(
        self, parser
    ):
        module_def = self._make_module_def()
        element = _snip(
            "<CONTAINERS>"
            "<ECUC-PARAM-CONF-CONTAINER-DEF>"
            "<SHORT-NAME>C1</SHORT-NAME>"
            "</ECUC-PARAM-CONF-CONTAINER-DEF>"
            "</CONTAINERS>"
        )
        parser.readEcucModuleDefContainers(element, module_def)
        assert len(module_def.getContainers()) == 1

    def test_readEcucModuleDefContainers_creates_choice(self, parser):
        module_def = self._make_module_def()
        element = _snip(
            "<CONTAINERS>"
            "<ECUC-CHOICE-CONTAINER-DEF>"
            "<SHORT-NAME>C2</SHORT-NAME>"
            "</ECUC-CHOICE-CONTAINER-DEF>"
            "</CONTAINERS>"
        )
        parser.readEcucModuleDefContainers(element, module_def)
        assert len(module_def.getContainers()) == 1

    def test_readEcucModuleDefContainers_unsupported_warns(
        self, warning_parser, caplog
    ):
        module_def = self._make_module_def()
        element = _snip(
            "<CONTAINERS><BAD/></CONTAINERS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucModuleDefContainers(
                element, module_def
            )
        assert any("Unsupported Container" in r.getMessage()
                   for r in caplog.records)


# ==================== SwSystemconstantValueSet (L4695) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestEcucParameterValue:
    def test_readEcucParameterValue_adds_annotation(self, parser):
        from armodel.models import EcucTextualParamValue
        param_value = EcucTextualParamValue()
        element = _snip(
            '<DEFINITION-REF DEST="ECUC-STRING-PARAM-DEF">/d</DEFINITION-REF>'
            "<ANNOTATIONS>"
            "<ANNOTATION>"
            "<SHORT-NAME>a</SHORT-NAME>"
            "</ANNOTATION>"
            "</ANNOTATIONS>"
        )
        parser.readEcucParameterValue(element, param_value)
        assert param_value.getDefinitionRef() is not None
        assert len(param_value.getAnnotations()) == 1

    def test_readEcucContainerValueParameterValues_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EcucContainerValue
        container = EcucContainerValue(
            parent=MagicMock(), short_name="Cv"
        )
        element = _snip(
            "<PARAMETER-VALUES><BAD/></PARAMETER-VALUES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucContainerValueParameterValues(
                element, container
            )
        assert any("Unsupported EcucParameterValue" in r.getMessage()
                   for r in caplog.records)


# ==================== SystemSignalGroup (L5249) ====================

