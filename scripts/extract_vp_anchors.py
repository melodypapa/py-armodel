import re
import sys

XSD = "autosar/R23-11/xsd/AUTOSAR_00052.xsd"

SPECIAL = {
    "AR-PACKAGE": "ARPackage",
}


def to_class_name(kebab: str) -> str:
    if kebab in SPECIAL:
        return SPECIAL[kebab]
    return "".join(part.capitalize() for part in kebab.split("-"))


def main() -> int:
    lines = open(XSD).read().split("\n")
    anchors, current = [], None
    for line in lines:
        m = re.search(r'<xsd:(complexType|group) name="([A-Z0-9-]+)"', line)
        if m:
            current = m.group(2)
        if 'name="VARIATION-POINT"' in line and current and current != "VARIATION-POINT":
            anchors.append(current)
    with open("docs/superpowers/plans/vp_anchors.txt", "w") as f:
        for name in anchors:
            f.write("%s -> %s\n" % (name, to_class_name(name)))
    print("anchors:", len(anchors))
    return 0


if __name__ == "__main__":
    sys.exit(main())
