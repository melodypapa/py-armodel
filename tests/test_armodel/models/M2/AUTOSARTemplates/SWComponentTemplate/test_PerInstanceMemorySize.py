import inspect
import re
from typing import List, Optional, get_type_hints

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import PerInstanceMemorySize, SwcImplementation


class TestPerInstanceMemorySize:
    def test_spec_notes_are_verbatim(self):
        class_note = (
            "Resources needed by the allocation of PerInstanceMemory for each SWC instance. Note that these resources are not covered by an ObjectFileSection, "
            "because they are supposed to be allocated by the RTE."
        )
        alignment_note = "Required alignment (1,2,4,...) of the referenced PerInstanceMemory. Unit: byte."
        alignment_constraint = (
            " [constr_1970] Existence of attribute PerInstanceMemorySize.alignment: For each PerInstanceMemorySize, attribute alignment shall exist at the time when the RTE is generated."
        )
        per_instance_memory_note = "This represents the referenced PerInstanceMemory."
        per_instance_memory_constraint = " [constr_1971] Existence of attribute PerInstanceMemorySize.perInstanceMemory: For each PerInstanceMemorySize, the reference to PerInstanceMemory in the role perInstanceMemory shall exist at the time when the RTE is generated."
        size_note = (
            "Size (in bytes) of the reference perInstanceMemory. The aggregation of PerInstanceMemorySize is subject to variability with the purpose to support "
            "variability in the software components implementations. Different algorithms in the implementation might require a different PerInstanceMemorySize."
        )
        size_constraint = " [constr_1972] Existence of attribute PerInstanceMemorySize.size: For each PerInstanceMemorySize, attribute size shall exist at the time when the RTE is generated."
        assert PerInstanceMemorySize.__doc__ is not None
        assert inspect.cleandoc(PerInstanceMemorySize.__doc__) == class_note
        assert PerInstanceMemorySize.__init__.__doc__ is None
        assert PerInstanceMemorySize.getAlignment.__doc__.strip() == alignment_note + alignment_constraint
        assert PerInstanceMemorySize.setAlignment.__doc__.strip() == alignment_note + alignment_constraint + " A None value is a no-op and does not overwrite an existing alignment."
        assert PerInstanceMemorySize.getPerInstanceMemoryRef.__doc__.strip() == per_instance_memory_note + per_instance_memory_constraint
        assert (
            PerInstanceMemorySize.setPerInstanceMemoryRef.__doc__.strip()
            == per_instance_memory_note + per_instance_memory_constraint + " A None value is a no-op and does not overwrite an existing perInstanceMemoryRef."
        )
        assert PerInstanceMemorySize.getSize.__doc__.strip() == size_note + size_constraint
        assert PerInstanceMemorySize.setSize.__doc__.strip() == size_note + size_constraint + " A None value is a no-op and does not overwrite an existing size."

    def test_base_and_inheritance_shape(self):
        assert PerInstanceMemorySize.__bases__ == (ARObject, VariationPointCapable)
        assert issubclass(PerInstanceMemorySize, ARObject)
        assert issubclass(PerInstanceMemorySize, VariationPointCapable)
        assert PerInstanceMemorySize.setAlignment.__annotations__["return"] == "PerInstanceMemorySize"
        assert PerInstanceMemorySize.setPerInstanceMemoryRef.__annotations__["return"] == "PerInstanceMemorySize"
        assert PerInstanceMemorySize.setSize.__annotations__["return"] == "PerInstanceMemorySize"

    def test_initialization_defaults(self):
        value = PerInstanceMemorySize()
        assert value.alignment is None
        assert value.perInstanceMemoryRef is None
        assert value.size is None
        assert value.variationPoint is None
        assert value.getAlignment() is None
        assert value.getPerInstanceMemoryRef() is None
        assert value.getSize() is None

    def test_member_types_and_order(self):
        source = inspect.getsource(PerInstanceMemorySize)
        init_source = inspect.getsource(PerInstanceMemorySize.__init__)
        assert re.findall(r"self\.(\w+):", init_source) == ["alignment", "perInstanceMemoryRef", "size"]
        assert re.findall(r"^    def (\w+)", source, re.MULTILINE) == [
            "__init__",
            "getAlignment",
            "setAlignment",
            "getPerInstanceMemoryRef",
            "setPerInstanceMemoryRef",
            "getSize",
            "setSize",
        ]
        assert get_type_hints(PerInstanceMemorySize.getAlignment).get("return") == Optional[PositiveInteger]
        assert get_type_hints(PerInstanceMemorySize.setAlignment).get("value") == Optional[PositiveInteger]
        assert get_type_hints(PerInstanceMemorySize.getPerInstanceMemoryRef).get("return") == Optional[RefType]
        assert get_type_hints(PerInstanceMemorySize.setPerInstanceMemoryRef).get("value") == Optional[RefType]
        assert get_type_hints(PerInstanceMemorySize.getSize).get("return") == Optional[PositiveInteger]
        assert get_type_hints(PerInstanceMemorySize.setSize).get("value") == Optional[PositiveInteger]
        assert get_type_hints(SwcImplementation.getPerInstanceMemorySizes).get("return") == List[PerInstanceMemorySize]
        assert get_type_hints(SwcImplementation.addPerInstanceMemorySize).get("value") == Optional[PerInstanceMemorySize]

    def test_get_set_alignment(self):
        value = PerInstanceMemorySize()
        alignment = PositiveInteger().setValue("16")
        assert value.setAlignment(alignment) is value
        assert value.getAlignment() is alignment
        assert value.getAlignment().getValue() == 16
        assert value.setAlignment(None) is value
        assert value.getAlignment() is alignment

    def test_get_set_per_instance_memory_ref(self):
        value = PerInstanceMemorySize()
        memory_ref = RefType()
        memory_ref.setValue("/Pkg/Memory")
        memory_ref.setDest("PER-INSTANCE-MEMORY")
        assert value.setPerInstanceMemoryRef(memory_ref) is value
        assert value.getPerInstanceMemoryRef() is memory_ref
        assert value.getPerInstanceMemoryRef().getValue() == "/Pkg/Memory"
        assert value.getPerInstanceMemoryRef().getDest() == "PER-INSTANCE-MEMORY"
        assert value.setPerInstanceMemoryRef(None) is value
        assert value.getPerInstanceMemoryRef() is memory_ref

    def test_get_set_size(self):
        value = PerInstanceMemorySize()
        size = PositiveInteger().setValue("64")
        assert value.setSize(size) is value
        assert value.getSize() is size
        assert value.getSize().getValue() == 64
        assert value.setSize(None) is value
        assert value.getSize() is size

    def test_variation_point_mixin(self):
        value = PerInstanceMemorySize()
        variation_point = VariationPoint()
        assert value.setVariationPoint(variation_point) is value
        assert value.getVariationPoint() is variation_point
        assert value.setVariationPoint(None) is value
        assert value.getVariationPoint() is variation_point
