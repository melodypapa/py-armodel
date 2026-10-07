"""
Test suite for the TimingCpSoftwareCluster classes
(CP_TPS_TimingExtensions Tables 4.5-4.7, pp.157-158, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Notes and the member declaration order (markdown
displayed row order) of the TDCpSoftwareClusterMappingSet /
TDCpSoftwareClusterMapping / TDCpSoftwareClusterResourceMapping model classes.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCpSoftwareCluster import (
    TDCpSoftwareClusterMapping,
    TDCpSoftwareClusterMappingSet,
    TDCpSoftwareClusterResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

SET_NOTE = "This is used to gather of classic platform software cluster mappings. Tags: atp.recommendedPackage=TimingExtensions"
MAPPING_NOTE = "This is used to specify a mapping between a software cluster that provides temporal and dynamic resources and the software clusters that need these resources."
RESOURCE_MAPPING_NOTE = "This is used to assign an unequivocal global resource identification to a temporal and dynamic resource."

RESOURCE_TO_TD_NOTE = "Maps a CP software cluster resource to a temporal resource. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tdCpSoftwareClusterResourceToTdMapping.shortName, tdCpSoftwareClusterResourceToTdMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild"
CLUSTER_TO_TD_NOTE = "Maps a temporal resource to a mapping between a providing CP software cluster and requesting CP software clusters. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tdCpSoftwareClusterToTdMapping.short Name, tdCpSoftwareClusterToTdMapping.variation Point.shortLabel vh.latestBindingTime=postBuild"
PROVIDER_NOTE = "This is the software cluster that provides the temporal and dynamic resource."
REQUESTOR_NOTE = "This is the software cluster that requests the temporal and dynamic resource."
TIMING_DESCRIPTION_NOTE = "The timing description representing the temporal and dynamic resource."
RESOURCE_NOTE = "The specific resource identification assigned to the temporal and dynamic resource."


class TestTDCpSoftwareClusterMapping:
    def _create(self) -> TDCpSoftwareClusterMapping:
        return TDCpSoftwareClusterMapping(AUTOSAR.getInstance(), "Mapping1")

    def test_inheritance(self):
        assert issubclass(TDCpSoftwareClusterMapping, Identifiable)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TDCpSoftwareClusterMapping.__doc__) == MAPPING_NOTE

    def test_initialization(self):
        mapping = self._create()

        assert mapping.getShortName() == "Mapping1"
        assert mapping.getProviderRef() is None
        assert mapping.getRequestorRefs() == []
        assert mapping.getTimingDescriptionRef() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCpSoftwareCluster")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "TDCpSoftwareClusterMapping")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("providerRef", "Optional[RefType]"),
            ("requestorRefs", "List[RefType]"),
            ("timingDescriptionRef", "Optional[RefType]"),
        ]

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(TDCpSoftwareClusterMapping.getProviderRef.__doc__) == PROVIDER_NOTE
        assert inspect.cleandoc(TDCpSoftwareClusterMapping.setProviderRef.__doc__) == PROVIDER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing providerRef."
        assert inspect.cleandoc(TDCpSoftwareClusterMapping.addRequestorRef.__doc__) == REQUESTOR_NOTE
        assert inspect.cleandoc(TDCpSoftwareClusterMapping.getRequestorRefs.__doc__) == REQUESTOR_NOTE
        assert inspect.cleandoc(TDCpSoftwareClusterMapping.getTimingDescriptionRef.__doc__) == TIMING_DESCRIPTION_NOTE
        assert (
            inspect.cleandoc(TDCpSoftwareClusterMapping.setTimingDescriptionRef.__doc__)
            == TIMING_DESCRIPTION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing timingDescriptionRef."
        )

    def test_get_set_provider_and_requestors(self):
        mapping = self._create()

        provider = RefType().setDest("CP-SOFTWARE-CLUSTER").setValue("/Clusters/Provider")
        assert mapping.setProviderRef(provider) is mapping
        assert mapping.getProviderRef() is provider

        requestor = RefType().setDest("CP-SOFTWARE-CLUSTER").setValue("/Clusters/Requestor")
        assert mapping.addRequestorRef(requestor) is mapping
        assert mapping.getRequestorRefs() == [requestor]
        assert mapping.addRequestorRef(None) is mapping
        assert mapping.getRequestorRefs() == [requestor]


class TestTDCpSoftwareClusterResourceMapping:
    def _create(self) -> TDCpSoftwareClusterResourceMapping:
        return TDCpSoftwareClusterResourceMapping(AUTOSAR.getInstance(), "ResourceMapping1")

    def test_inheritance(self):
        assert issubclass(TDCpSoftwareClusterResourceMapping, Identifiable)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TDCpSoftwareClusterResourceMapping.__doc__) == RESOURCE_MAPPING_NOTE

    def test_initialization(self):
        mapping = self._create()

        assert mapping.getShortName() == "ResourceMapping1"
        assert mapping.getResourceRef() is None
        assert mapping.getTimingDescriptionRef() is None

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(TDCpSoftwareClusterResourceMapping.getResourceRef.__doc__) == RESOURCE_NOTE
        assert inspect.cleandoc(TDCpSoftwareClusterResourceMapping.setResourceRef.__doc__) == RESOURCE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing resourceRef."
        assert inspect.cleandoc(TDCpSoftwareClusterResourceMapping.getTimingDescriptionRef.__doc__) == TIMING_DESCRIPTION_NOTE
        assert (
            inspect.cleandoc(TDCpSoftwareClusterResourceMapping.setTimingDescriptionRef.__doc__)
            == TIMING_DESCRIPTION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing timingDescriptionRef."
        )

    def test_get_set_resource(self):
        mapping = self._create()

        resource = RefType().setDest("CP-SOFTWARE-CLUSTER-RESOURCE").setValue("/Resources/Res1")
        assert mapping.setResourceRef(resource) is mapping
        assert mapping.getResourceRef() is resource


class TestTDCpSoftwareClusterMappingSet:
    def _create(self) -> TDCpSoftwareClusterMappingSet:
        return TDCpSoftwareClusterMappingSet(AUTOSAR.getInstance(), "MappingSet1")

    def test_inheritance(self):
        assert issubclass(TDCpSoftwareClusterMappingSet, ARElement)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TDCpSoftwareClusterMappingSet.__doc__) == SET_NOTE

    def test_initialization(self):
        mapping_set = self._create()

        assert mapping_set.getShortName() == "MappingSet1"
        assert mapping_set.getTdCpSoftwareClusterResourceToTdMappings() == []
        assert mapping_set.getTdCpSoftwareClusterToTdMappings() == []

    def test_create_mappings(self):
        package = AUTOSAR.getInstance().createARPackage("Timing")
        mapping_set = package.createTDCpSoftwareClusterMappingSet("MappingSet1")

        resource_mapping = mapping_set.createTdCpSoftwareClusterResourceToTdMapping("ResToTd1")
        assert isinstance(resource_mapping, TDCpSoftwareClusterResourceMapping)
        cluster_mapping = mapping_set.createTdCpSoftwareClusterToTdMapping("ClusterToTd1")
        assert isinstance(cluster_mapping, TDCpSoftwareClusterMapping)

        assert mapping_set.getTdCpSoftwareClusterResourceToTdMappings() == [resource_mapping]
        assert mapping_set.getTdCpSoftwareClusterToTdMappings() == [cluster_mapping]
        assert mapping_set.getReferrableElement("ResToTd1", TDCpSoftwareClusterResourceMapping) is resource_mapping

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(TDCpSoftwareClusterMappingSet.createTdCpSoftwareClusterResourceToTdMapping.__doc__) == RESOURCE_TO_TD_NOTE
        assert inspect.cleandoc(TDCpSoftwareClusterMappingSet.getTdCpSoftwareClusterResourceToTdMappings.__doc__) == RESOURCE_TO_TD_NOTE
        assert inspect.cleandoc(TDCpSoftwareClusterMappingSet.createTdCpSoftwareClusterToTdMapping.__doc__) == CLUSTER_TO_TD_NOTE
        assert inspect.cleandoc(TDCpSoftwareClusterMappingSet.getTdCpSoftwareClusterToTdMappings.__doc__) == CLUSTER_TO_TD_NOTE
