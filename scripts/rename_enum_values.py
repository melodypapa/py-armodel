"""Rename AREnum literal values to the R23-11 XSD enumeration spellings.

Value strings ONLY: constant names, comments, tuple order, and class
structure are untouched. Also regenerates *_XML_MAP keys in the parser and
writer whose keys reference renamed values.
"""
import os
import re

XSD_PATH = os.path.join("src", "armodel", "validation", "schemas", "R23-11", "AUTOSAR_00052.xsd")
MODELS_DIR = os.path.join("src", "armodel", "models")
MAP_FILES = [
    os.path.join("src", "armodel", "parser", "arxml_parser.py"),
    os.path.join("src", "armodel", "writer", "arxml_writer.py"),
]

SKIP_CLASSES = {
    # IEEE-1722 empty stubs: XSD counterparts exist but they define zero constants (nothing to rename)
    "IEEE1722TpAafAes3DataTypeEnum", "IEEE1722TpAafFormatEnum", "IEEE1722TpAafNominalRateEnum",
    "IEEE1722TpAcfCanMessageTypeEnum", "IEEE1722TpCrfPullEnum", "IEEE1722TpCrfTypeEnum",
    "IEEE1722TpRvfColorSpaceEnum", "IEEE1722TpRvfFrameRateEnum", "IEEE1722TpRvfPixelDepthEnum",
    "IEEE1722TpRvfPixelFormatEnum",
}


def kebab(name):
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", name)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "-", s)
    s = re.sub(r"(?<=[A-Za-z])(?=\d)", "-", s)
    s = re.sub(r"(?<=\d)(?=[A-Za-z])", "-", s)
    return s.upper()


def load_xsd_enums(path):
    xsd = open(path, encoding="utf-8").read()
    enums = {}
    for n, body in re.findall(r'<xsd:simpleType name="([^"]+)">(.*?)</xsd:simpleType>', xsd, re.S):
        if "xsd:enumeration" in body and not n.endswith("--SUBTYPES-ENUM"):
            enums[n] = re.findall(r'<xsd:enumeration value="([^"]*)"', body)
    return enums


def class_renames(block, xsvals):
    """Return {old_value: new_value} for constants in this class block."""
    renames = {}
    for n, v in re.findall(r'\n    ([A-Z][A-Z0-9_]*) = "([^"]*)"', block):
        if v in xsvals or v in renames.values():
            continue
        # match by constant name, hyphen/underscore-insensitive (XSD has
        # double-hyphen tokens like J-1939-NM--AAC / AUTO-IP--DOIP)
        norm = re.sub(r"[^A-Z0-9]", "", n)
        target = None
        # 1. exact normalized equality
        for xv in xsvals:
            if re.sub(r"[^A-Z0-9]", "", xv) == norm:
                target = xv
                break
        # 2. legacy ENUM_ prefix on the constant name
        if target is None and norm.startswith("ENUM"):
            stripped = norm[4:]
            for xv in xsvals:
                if re.sub(r"[^A-Z0-9]", "", xv) == stripped:
                    target = xv
                    break
        # 3. truncated constant name: unique XSD value starting with it
        if target is None:
            hits = [xv for xv in xsvals if re.sub(r"[^A-Z0-9]", "", xv).startswith(norm)]
            if len(hits) == 1:
                target = hits[0]
        if target is None:
            raise RuntimeError("%s: no XSD value matches constant %s = %r" % (block.split("(")[0], n, v))
        renames[v] = target
    return renames


def main():
    xsd = load_xsd_enums(XSD_PATH)
    all_renames = {}  # old -> new, across every class
    for root, _, files in os.walk(MODELS_DIR):
        for fn in files:
            if not fn.endswith(".py"):
                continue
            path = os.path.join(root, fn)
            src = open(path, encoding="utf-8").read()
            orig = src
            # collect matches first, edit in reverse so earlier spans stay valid
            matches = list(re.finditer(r"class (\w+)\(AREnum\):", src))[::-1]
            for m in matches:
                cls = m.group(1)
                if cls in SKIP_CLASSES:
                    continue
                base = kebab(cls)
                xsvals = None
                for cand in (base, base + "--SIMPLE"):
                    if cand in xsd:
                        xsvals = xsd[cand]
                        break
                if xsvals is None:
                    continue
                start = m.start()
                nxt = re.search(r"\nclass ", src[m.end():])
                end = m.end() + nxt.start() if nxt else len(src)
                block = src[start:end]
                renames = class_renames(block, xsvals)
                if not renames:
                    continue
                for old, new in renames.items():
                    if all_renames.get(old, new) != new:
                        raise RuntimeError("conflicting rename for %r: %r vs %r" % (old, all_renames[old], new))
                    all_renames[old] = new
                new_block = block
                for old, new in sorted(renames.items(), key=lambda kv: -len(kv[0])):
                    new_block = new_block.replace('"%s"' % old, '"%s"' % new)
                src = src[:start] + new_block + src[end:]
            if src != orig:
                open(path, "w", encoding="utf-8").write(src)
                print("rewrote", path)

    for path in MAP_FILES:
        src = open(path, encoding="utf-8").read()
        orig = src
        for old, new in sorted(all_renames.items(), key=lambda kv: -len(kv[0])):
            src = src.replace('"%s":' % old, '"%s":' % new)
        if src != orig:
            open(path, "w", encoding="utf-8").write(src)
            print("regenerated map keys in", path)
    print("total renames:", len(all_renames))


if __name__ == "__main__":
    main()
