"""Tests for ECUC (ECU Configuration) parsing handlers."""

import xml.etree.ElementTree as ET
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
