"""Extracts XSD pattern facets for the ARLiteral classes of PrimitiveTypes.py.

Run from the repository root. Prints ClassName<TAB>XSD-TYPE<TAB>facet lines to
stdout; classes whose customType has no matching facet go to stderr.
"""

import re
import sys
from pathlib import Path

from lxml import etree

XSD_PATH = Path("autosar/R23-11/xsd/AUTOSAR_00052.xsd")
SRC_PATH = Path("src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py")
NS = {"xsd": "http://www.w3.org/2001/XMLSchema"}


def collect_xsd_patterns():
    tree = etree.parse(str(XSD_PATH))
    patterns = {}
    for node in tree.findall(".//xsd:simpleType", NS) + tree.findall(".//xsd:complexType", NS):
        name = node.get("name")
        if not name:
            continue
        facets = [p.get("value") for p in node.findall(".//xsd:pattern", NS) if p.get("value")]
        if facets:
            patterns[name] = facets
    return patterns


def collect_classes():
    text = SRC_PATH.read_text()
    classes = {}
    matches = list(re.finditer(r"^class (\w+)\(", text, re.M))
    for index, match in enumerate(matches):
        name = match.group(1)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start() : end]
        custom = re.search(r"xml\.xsd\.customType=([A-Za-z0-9_\-]+)", block)
        if custom is not None:
            classes[name] = custom.group(1)
    return classes


def resolve_facets(patterns, xsd_type):
    if xsd_type in patterns:
        return patterns[xsd_type]
    return patterns.get(xsd_type + "--SIMPLE", [])


def main():
    patterns = collect_xsd_patterns()
    classes = collect_classes()
    for class_name in sorted(classes):
        xsd_type = classes[class_name]
        for facet in resolve_facets(patterns, xsd_type):
            print("%s\t%s\t%s" % (class_name, xsd_type, facet))
    print("classes without XSD pattern facet: %s" % ", ".join(sorted(n for n, t in classes.items() if not resolve_facets(patterns, t))), file=sys.stderr)


if __name__ == "__main__":
    main()
