import os
import threading
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional

from lxml import etree

XSI_SCHEMA_LOCATION = "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation"

SCHEMA_DIR = os.path.join(os.path.dirname(__file__), "schemas")

_SCHEMA_PATHS: Dict[str, str] = {
    "autosar_00052.xsd": os.path.join(SCHEMA_DIR, "R23-11", "AUTOSAR_00052.xsd"),
    "autosar_00046.xsd": os.path.join(SCHEMA_DIR, "R4.4.0", "AUTOSAR_00046.xsd"),
    "autosar_00044.xsd": os.path.join(SCHEMA_DIR, "R4.3.1", "AUTOSAR_00044.xsd"),
    "autosar.xsd": os.path.join(SCHEMA_DIR, "R3.2.3", "AUTOSAR.xsd"),
}

_SCHEMA_CACHE: Dict[str, etree.XMLSchema] = {}
_CACHE_LOCK = threading.Lock()


class _AUTOSARResolver(etree.Resolver):
    def __init__(self, schema_dir: str, fallback_dir: Optional[str] = None) -> None:
        self.schema_dir = schema_dir
        self.fallback_dir = fallback_dir

    def resolve(self, url, id, context):
        candidate = os.path.join(self.schema_dir, os.path.basename(url))
        if os.path.exists(candidate):
            return self.resolve_filename(candidate, context)
        if self.fallback_dir is not None:
            fallback_candidate = os.path.join(self.fallback_dir, os.path.basename(url))
            if os.path.exists(fallback_candidate):
                return self.resolve_filename(fallback_candidate, context)
        return None


def register_schema_file(xsd_filename: str, xsd_path: str) -> None:
    _SCHEMA_PATHS[xsd_filename.lower()] = xsd_path


def detect_schema_path(data: bytes) -> Optional[str]:
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return None
    schema_location = root.attrib.get(XSI_SCHEMA_LOCATION)
    if not schema_location:
        return None
    tokens = schema_location.split()
    if len(tokens) < 2:
        return None
    return _SCHEMA_PATHS.get(tokens[-1].lower())


def get_schema(xsd_path: str) -> etree.XMLSchema:
    key = os.path.realpath(xsd_path)
    with _CACHE_LOCK:
        if key not in _SCHEMA_CACHE:
            parser = etree.XMLParser()
            parser.resolvers.add(_AUTOSARResolver(os.path.dirname(key), fallback_dir=SCHEMA_DIR))
            _SCHEMA_CACHE[key] = etree.XMLSchema(etree.parse(key, parser))
        return _SCHEMA_CACHE[key]


class ValidationError(object):
    def __init__(self, line: Optional[int], column: Optional[int], message: str, domain: str) -> None:
        self.line = line
        self.column = column
        self.message = message
        self.domain = domain

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ValidationError):
            return NotImplemented
        return (self.line, self.column, self.message, self.domain) == (other.line, other.column, other.message, other.domain)

    def __hash__(self) -> int:
        return hash((self.line, self.column, self.message, self.domain))

    def __repr__(self) -> str:
        return "ValidationError(line=%s, column=%s, message=%r, domain=%r)" % (self.line, self.column, self.message, self.domain)


class ARXMLValidator(object):
    def __init__(self, xsd_path: str) -> None:
        self.xsd_path = xsd_path

    def validate_bytes(self, data: bytes) -> List[ValidationError]:
        parser = etree.XMLParser()
        parser.resolvers.add(_AUTOSARResolver(os.path.dirname(os.path.realpath(self.xsd_path)), fallback_dir=SCHEMA_DIR))
        try:
            document = etree.fromstring(data, parser)
        except etree.XMLSyntaxError as e:
            return [ValidationError(line=e.lineno, column=e.offset, message="XML syntax error: %s" % e.msg, domain="syntax")]
        schema = get_schema(self.xsd_path)
        if schema.validate(document):
            return []
        return [ValidationError(line=error.line, column=error.column, message=error.message, domain="schema") for error in schema.error_log]

    def validate_string(self, xml: str) -> List[ValidationError]:
        return self.validate_bytes(xml.encode("utf-8"))
