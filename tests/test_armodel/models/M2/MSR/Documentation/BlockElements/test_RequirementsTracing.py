"""This module contains tests for the RequirementsTracing module."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import StandardNameEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import StructuredReq, TraceableText
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class TestTraceableText:
    """Test class for TraceableText class."""

    def test_traceable_text_matches_table_note(self):
        assert TraceableText.__doc__.strip() == (
            "This meta-class represents the ability to denote a traceable text item such as requirements etc. "
            "The following approach applies: shortName represents the tag for tracing, longName represents the head line, "
            "category represents the kind of the tagged text (see [constr_2540])"
        )

    def test_traceable_text_initialization(self):
        """Test that a TraceableText object can be initialized with default values."""
        traceable_text = TraceableText(None, "TraceableText")
        assert traceable_text.text is None
        assert traceable_text.traceRefs == []

    def test_traceable_text_text_methods(self):
        """Test the text getter and setter."""
        traceable_text = TraceableText(None, "TraceableText")
        text = DocumentationBlock()

        result = traceable_text.setText(text)
        assert traceable_text.getText() == text
        assert result == traceable_text

        traceable_text.setText(None)
        assert traceable_text.getText() == text

    def test_traceable_text_trace_refs_methods(self):
        """Test the traceRefs getter and addTraceRef."""
        traceable_text = TraceableText(None, "TraceableText")
        trace_ref = RefType()

        result = traceable_text.addTraceRef(trace_ref)
        assert trace_ref in traceable_text.getTraceRefs()
        assert result == traceable_text

        traceable_text.addTraceRef(None)
        assert traceable_text.getTraceRefs() == [trace_ref]


class TestStructuredReq:
    """Test class for StructuredReq class."""

    def test_structured_req_initialization(self):
        """Test that a StructuredReq object can be initialized with default values."""
        structured_req = StructuredReq(None, "StructuredReq")
        assert structured_req.date is None
        assert structured_req.appliesTo == []
        assert structured_req.importance is None
        assert structured_req.issuedBy is None
        assert structured_req.type is None
        assert structured_req.description is None
        assert structured_req.rationale is None
        assert structured_req.dependencies is None
        assert structured_req.useCase is None
        assert structured_req.conflicts is None
        assert structured_req.supportingMaterial is None
        assert structured_req.remark is None
        assert structured_req.testedItemRefs == []

    def test_structured_req_date_methods(self):
        """Test the date getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        date = DateTime().setValue("2023-11-01")

        result = structured_req.setDate(date)
        assert structured_req.getDate() == date
        assert result == structured_req

        structured_req.setDate(None)
        assert structured_req.getDate() == date

    def test_structured_req_applies_to_methods(self):
        """Test the appliesTo getter and addAppliesTo."""
        structured_req = StructuredReq(None, "StructuredReq")
        applies_to = StandardNameEnum().setValue("AP")

        result = structured_req.addAppliesTo(applies_to)
        assert structured_req.getAppliesTos() == [applies_to]
        assert result == structured_req

        structured_req.addAppliesTo(None)
        assert structured_req.getAppliesTos() == [applies_to]

    def test_structured_req_description_methods(self):
        """Test the description getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        description = DocumentationBlock()

        result = structured_req.setDescription(description)
        assert structured_req.getDescription() == description
        assert result == structured_req

        structured_req.setDescription(None)
        assert structured_req.getDescription() == description

    def test_structured_req_importance_methods(self):
        """Test the importance getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        importance = String().setValue("high")

        result = structured_req.setImportance(importance)
        assert structured_req.getImportance() == importance
        assert result == structured_req

        structured_req.setImportance(None)
        assert structured_req.getImportance() == importance

    def test_structured_req_issued_by_methods(self):
        """Test the issuedBy getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        issued_by = String().setValue("AUTOSAR")

        result = structured_req.setIssuedBy(issued_by)
        assert structured_req.getIssuedBy() == issued_by
        assert result == structured_req

        structured_req.setIssuedBy(None)
        assert structured_req.getIssuedBy() == issued_by

    def test_structured_req_type_methods(self):
        """Test the type getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        req_type = String().setValue("enhancement")

        result = structured_req.setType(req_type)
        assert structured_req.getType() == req_type
        assert result == structured_req

        structured_req.setType(None)
        assert structured_req.getType() == req_type

    def test_structured_req_rationale_methods(self):
        """Test the rationale getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        rationale = DocumentationBlock()

        result = structured_req.setRationale(rationale)
        assert structured_req.getRationale() == rationale
        assert result == structured_req

        structured_req.setRationale(None)
        assert structured_req.getRationale() == rationale

    def test_structured_req_dependencies_methods(self):
        """Test the dependencies getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        dependencies = DocumentationBlock()

        result = structured_req.setDependencies(dependencies)
        assert structured_req.getDependencies() == dependencies
        assert result == structured_req

        structured_req.setDependencies(None)
        assert structured_req.getDependencies() == dependencies

    def test_structured_req_use_case_methods(self):
        """Test the useCase getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        use_case = DocumentationBlock()

        result = structured_req.setUseCase(use_case)
        assert structured_req.getUseCase() == use_case
        assert result == structured_req

        structured_req.setUseCase(None)
        assert structured_req.getUseCase() == use_case

    def test_structured_req_conflicts_methods(self):
        """Test the conflicts getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        conflicts = DocumentationBlock()

        result = structured_req.setConflicts(conflicts)
        assert structured_req.getConflicts() == conflicts
        assert result == structured_req

        structured_req.setConflicts(None)
        assert structured_req.getConflicts() == conflicts

    def test_structured_req_supporting_material_methods(self):
        """Test the supportingMaterial getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        supporting_material = DocumentationBlock()

        result = structured_req.setSupportingMaterial(supporting_material)
        assert structured_req.getSupportingMaterial() == supporting_material
        assert result == structured_req

        structured_req.setSupportingMaterial(None)
        assert structured_req.getSupportingMaterial() == supporting_material

    def test_structured_req_remark_methods(self):
        """Test the remark getter and setter."""
        structured_req = StructuredReq(None, "StructuredReq")
        remark = DocumentationBlock()

        result = structured_req.setRemark(remark)
        assert structured_req.getRemark() == remark
        assert result == structured_req

        structured_req.setRemark(None)
        assert structured_req.getRemark() == remark

    def test_structured_req_tested_item_refs_methods(self):
        """Test the testedItemRefs getter and addTestedItemRef."""
        structured_req = StructuredReq(None, "StructuredReq")
        tested_item_ref = RefType()

        result = structured_req.addTestedItemRef(tested_item_ref)
        assert tested_item_ref in structured_req.getTestedItemRefs()
        assert result == structured_req

        structured_req.addTestedItemRef(None)
        assert structured_req.getTestedItemRefs() == [tested_item_ref]

    def test_structured_req_inherited_variation_point(self):
        """Test the inherited variationPoint member declared by the StructuredReq XSD group."""
        structured_req = StructuredReq(None, "StructuredReq")
        variation_point = VariationPoint()

        result = structured_req.setVariationPoint(variation_point)
        assert structured_req.getVariationPoint() is variation_point
        assert result is structured_req

        structured_req.setVariationPoint(None)
        assert structured_req.getVariationPoint() is variation_point
