import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SecureCommunicationProps,
    SecuredIPdu,
    SecuredPduHeaderEnum,
)

CLASS_NOTE = (
    "If useAsCryptographicPdu is not set or set to false this IPdu contains the payload of an Authentic IPdu "
    "supplemented by additional Authentication Information (Freshness Counter and an Authenticator). If "
    "useAsCryptographicPdu is set to true this IPdu contains the Authenticator for a payload that is transported in "
    "a separate message. The separate Authentic IPdu is described by the Pdu that is referenced with the payload "
    "reference from this SecuredIPdu. Tags: atp.recommendedPackage=Pdus"
)
NOTES = {
    "authenticationPropsRef": ("Reference to authentication properties that are valid for this SecuredIPdu."),
    "dynamicRuntimeLengthHandling": (
        "Defines whether the length information for handling this SecuredIPdu with SecuredIPdu.useSecuredPdu "
        "Header=noHeader is taken from the configuration or from the actually provided length information during "
        "runtime. true: SecuredIPdu length information is taken from the actually provided length information during "
        "runtime. false: SecuredIPdu length information is taken from the configuration."
    ),
    "freshnessPropsRef": ("Reference to freshness properties that are valid for this SecuredIPdu."),
    "payloadRef": ("Reference to a Pdu that will be protected against unauthorized manipulation and replay attacks."),
    "secureCommunicationProps": ("Specific configuration properties for this SecuredIPdu."),
    "useAsCryptographicIPdu": (
        "If this attribute is set to true the SecuredIPdu contains the Authentication Information for an AuthenticIPdu "
        "that is transmitted in a separate message. The AuthenticIPdu contains the original payload, i.e. the secured "
        "data. If this attribute is set to false this SecuredIPdu contains the payload of an Authentic IPdu "
        "supplemented by additional Authentication Information."
    ),
    "useSecuredPduHeader": (
        "This attribute defines the size of the header which is inserted into the SecuredIPdu. If this attribute is set "
        "to anything but noHeader, the SecuredIPdu contains the Secured I-PDU Header to indicate the length of the "
        "AuthenticIPdu. The AuthenticIPdu contains the original payload, i.e. the secured data."
    ),
}


class TestSecuredIPdu:
    """Test cases for SecuredIPdu (Table 6.42, p.368)."""

    def test_initialization_defaults(self):
        ipdu = SecuredIPdu(None, "Ipdu")
        assert ipdu.getAuthenticationPropsRef() is None
        assert ipdu.getDynamicRuntimeLengthHandling() is None
        assert ipdu.getFreshnessPropsRef() is None
        assert ipdu.getPayloadRef() is None
        assert ipdu.getSecureCommunicationProps() is None
        assert ipdu.getUseAsCryptographicIPdu() is None
        assert ipdu.getUseSecuredPduHeader() is None

    def test_get_set_round_trip_and_none_noop(self):
        ipdu = SecuredIPdu(None, "Ipdu")

        ref = RefType()
        ref.value = "/props/auth"
        assert ipdu.setAuthenticationPropsRef(ref) is ipdu
        assert ipdu.getAuthenticationPropsRef() is ref
        ipdu.setAuthenticationPropsRef(None)
        assert ipdu.getAuthenticationPropsRef() is ref

        assert ipdu.setDynamicRuntimeLengthHandling(True) is ipdu
        assert ipdu.getDynamicRuntimeLengthHandling() is True

        props = SecureCommunicationProps()
        assert ipdu.setSecureCommunicationProps(props) is ipdu
        assert ipdu.getSecureCommunicationProps() is props

        assert ipdu.setUseSecuredPduHeader(SecuredPduHeaderEnum.SECURED_PDU_HEADER16_BIT) is ipdu
        assert ipdu.getUseSecuredPduHeader() == SecuredPduHeaderEnum.SECURED_PDU_HEADER16_BIT

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SecuredIPdu.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        ipdu = SecuredIPdu(None, "Ipdu")
        assert inspect.cleandoc(ipdu.getAuthenticationPropsRef.__doc__) == NOTES["authenticationPropsRef"], "authenticationPropsRef"
        assert inspect.cleandoc(ipdu.setAuthenticationPropsRef.__doc__).split("\n")[0] == NOTES["authenticationPropsRef"], "authenticationPropsRef"
        assert inspect.cleandoc(ipdu.getDynamicRuntimeLengthHandling.__doc__) == NOTES["dynamicRuntimeLengthHandling"], "dynamicRuntimeLengthHandling"
        assert inspect.cleandoc(ipdu.setDynamicRuntimeLengthHandling.__doc__).split("\n")[0] == NOTES["dynamicRuntimeLengthHandling"], "dynamicRuntimeLengthHandling"
        assert inspect.cleandoc(ipdu.getFreshnessPropsRef.__doc__) == NOTES["freshnessPropsRef"], "freshnessPropsRef"
        assert inspect.cleandoc(ipdu.setFreshnessPropsRef.__doc__).split("\n")[0] == NOTES["freshnessPropsRef"], "freshnessPropsRef"
        assert inspect.cleandoc(ipdu.getPayloadRef.__doc__) == NOTES["payloadRef"], "payloadRef"
        assert inspect.cleandoc(ipdu.setPayloadRef.__doc__).split("\n")[0] == NOTES["payloadRef"], "payloadRef"
        assert inspect.cleandoc(ipdu.getSecureCommunicationProps.__doc__) == NOTES["secureCommunicationProps"], "secureCommunicationProps"
        assert inspect.cleandoc(ipdu.setSecureCommunicationProps.__doc__).split("\n")[0] == NOTES["secureCommunicationProps"], "secureCommunicationProps"
        assert inspect.cleandoc(ipdu.getUseAsCryptographicIPdu.__doc__) == NOTES["useAsCryptographicIPdu"], "useAsCryptographicIPdu"
        assert inspect.cleandoc(ipdu.setUseAsCryptographicIPdu.__doc__).split("\n")[0] == NOTES["useAsCryptographicIPdu"], "useAsCryptographicIPdu"
        assert inspect.cleandoc(ipdu.getUseSecuredPduHeader.__doc__) == NOTES["useSecuredPduHeader"], "useSecuredPduHeader"
        assert inspect.cleandoc(ipdu.setUseSecuredPduHeader.__doc__).split("\n")[0] == NOTES["useSecuredPduHeader"], "useSecuredPduHeader"
