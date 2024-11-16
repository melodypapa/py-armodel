
from ....models.implementation import AutosarEngineeringObject, Code
from ....models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestImplementation:
    def test_code(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        code = Code(ar_root, "code")
        assert(code.short_name == "code")

        data = [
            ["Autosar::include::BswM.h", "SWHDR"],
            ["Autosar::src::BswM.c", "SWSRC"]
        ]

        for item in data:
            engineering_obj = AutosarEngineeringObject()
            engineering_obj.setShortLabel(item[0])\
                           .setCategory(item[1])
            code.addArtifactDescriptor(engineering_obj)

        assert(len(code.getArtifactDescriptors()) == 2)
        assert(len(code.getArtifactDescriptors("SWHDR")) == 1)
        assert(len(code.getArtifactDescriptors("SWSRC")) == 1)