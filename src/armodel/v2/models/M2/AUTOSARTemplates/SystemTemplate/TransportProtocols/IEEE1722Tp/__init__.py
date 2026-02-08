"""
V2 M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp package.
"""

from .IEEE1722TpAcf import *
from .IEEE1722TpAv import *

# Classes:
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722TpAcfConnection import IEEE1722TpAcfConnection
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722TpAvConnection import IEEE1722TpAvConnection
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722TpConfig import IEEE1722TpConfig
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722TpConnection import IEEE1722TpConnection

__all__ = [
    # .IEEE1722TpAcf.*,
    # .IEEE1722TpAv.*,
    "IEEE1722TpAcfConnection",
    "IEEE1722TpAvConnection",
    "IEEE1722TpConfig",
    "IEEE1722TpConnection",
]
