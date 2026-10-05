"""Shared helper functions for parser tests.

Importable utilities used across the per-topic parser test modules.
Fixtures live in ``conftest.py``; this module hosts plain functions only.
"""

import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR

#: AUTOSAR R4.0 XML namespace used by every snippet helper.
NS = "http://autosar.org/schema/r4.0"


def _snip(inner: str, root_tag: str = "ROOT", attrs: str = "") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS.

    ``attrs`` is spliced onto the root tag verbatim, e.g.
    ``attrs=' S="1234" T="2024-01-01T00:00:00Z"'`` — used to pin the
    ``AR:AR-OBJECT`` checksum/timestamp round-trip (Rule 0025).
    """
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'{attrs}>{inner}</{root_tag}>")


def _autosar_root():
    """Return the AUTOSAR singleton for use as a parent in model constructors."""
    return AUTOSAR.getInstance()
