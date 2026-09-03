"""
N/A-confirmation tests for AtpBlueprintMapping (R23-11 Table C.13, p.162).

AtpBlueprintMapping is an abstract shell: Base = ARObject, no own attributes
(PDF C.13 atpBlueprint/atpBlueprintedElement refs are atpDerived/skipped in XSD
ATP-BLUEPRINT-MAPPING). The only handlers are read/writeAtpBlueprintMapping, which
delegate to the ARObject base chain; the concrete BlueprintMapping is round-tripped
through BlueprintMappingSet (see tests/test_armodel/parser/test_blueprint_mapping_set.py).
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestAtpBlueprintMappingReaderWriter:
    """
    N/A contract: AtpBlueprintMapping has no own XML element, so there is no
    dedicated attribute read/write method -- only the base-delegating handlers.
    """

    def test_base_is_arobject_no_own_attributes(self):
        """Rule 0001.1/0001.3: abstract ARObject shell; no own attribute accessors."""
        assert AtpBlueprintMapping.__bases__[0] is ARObject
        # no own attribute accessors modeled on the abstract base
        assert not hasattr(AtpBlueprintMapping, "getBlueprint")
        assert not hasattr(AtpBlueprintMapping, "setBlueprint")

    def test_base_delegating_handlers_exist(self):
        """read/writeAtpBlueprintMapping exist and delegate to the ARObject base chain."""
        assert hasattr(ARXMLParser, "readAtpBlueprintMapping")
        assert hasattr(ARXMLWriter, "writeAtpBlueprintMapping")
