from abc import ABCMeta
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean, ARLiteral, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.swc_internal_behavior.instance_refs_usage import AutosarParameterRef, AutosarVariableRef


class RoleBasedDataAssignment(ARObject):
    def __init__(self):
        super().__init__()

        self.role = None                    # type: ARLiteral
        self.used_data_element = None       # type: AutosarVariableRef
        self.used_parameter_element = None  # type: AutosarParameterRef
        self.used_pim_ref = None            # type: RefType


class ServiceNeeds(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ServiceNeeds:
            raise NotImplementedError("ServiceNeeds is an abstract class.")

        super().__init__(parent, short_name)


class NvBlockNeeds(ServiceNeeds):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.calc_ram_block_crc = None                  # type: ARBoolean
        self.check_static_block_id = None               # type: ARBoolean
        self.n_data_sets = None                         # type: int
        self.n_rom_blocks = None                        # type: int
        self.ram_block_status_control = None            # type: str
        self.readonly = None                            # type: ARBoolean
        self.reliability = None                         # type: str
        self.resistant_to_changed_sw = None             # type: ARBoolean
        self.restore_at_start = None                    # type: ARBoolean
        self.select_block_for_first_init_all = None     # type: ARBoolean
        self.store_at_shutdown = None                   # type: ARBoolean 
        self.store_cyclic = None                        # type: ARBoolean
        self.store_emergency = None                     # type: ARBoolean
        self.store_immediate = None                     # type: ARBoolean
        self.store_on_change = None                     # type: ARBoolean
        self.use_auto_validation_at_shut_down = None    # type: ARBoolean
        self.use_crc_comp_mechanism = None              # type: ARBoolean
        self.write_only_once = None                     # type: ARBoolean
        self.write_verification = None                  # type: ARBoolean
        self.writing_frequency = None                   # type: ARBoolean
        self.writing_priority = None                    # type: ARBoolean