import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement, CryptoServiceQueue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

CLASS_NOTE = "This meta-class has the ability to represent a crypto queue. Tags: atp.recommendedPackage=CryptoServiceQueues"
CLASS_CONSTRAINTS = ("[constr_5058] Value range for CryptoServiceQueue.queueSize: If the CryptoServiceQueue.queueSize is defined it shall have a value which is equal or greater than 1.",)
NOTES = {
    "queueSize": "Defines the queue size of the CryptoServiceQueue.",
}


class TestCryptoServiceQueue:
    """Test cases for CryptoServiceQueue (Table 6.53, p.381)."""

    def test_inheritance(self):
        assert issubclass(CryptoServiceQueue, ARElement)

    def test_concrete_instantiation(self):
        queue = CryptoServiceQueue(None, "CryptoServiceQueue1")
        assert queue.getShortName() == "CryptoServiceQueue1"

    def test_initialization_defaults(self):
        queue = CryptoServiceQueue(None, "CryptoServiceQueue1")
        assert queue.getQueueSize() is None

    def test_get_set_queue_size(self):
        queue = CryptoServiceQueue(None, "CryptoServiceQueue1")

        value = PositiveInteger().setValue("32")
        assert queue.setQueueSize(value) is queue
        assert queue.getQueueSize() is value
        assert queue.getQueueSize().getValue() == 32
        queue.setQueueSize(None)
        assert queue.getQueueSize() is value

    def test_annotation_pins(self):
        getter_hints = typing.get_type_hints(CryptoServiceQueue.getQueueSize)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]
        setter_hints = typing.get_type_hints(CryptoServiceQueue.setQueueSize)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CryptoServiceQueue

    def test_class_docstring_note(self):
        assert inspect.cleandoc(CryptoServiceQueue.__doc__) == CLASS_NOTE + "\n\n" + "\n".join(CLASS_CONSTRAINTS)

    def test_accessor_docstrings_verbatim(self):
        queue = CryptoServiceQueue(None, "CryptoServiceQueue1")
        for attr, note in NOTES.items():
            getter = getattr(queue, "get" + attr[0].upper() + attr[1:])
            setter = getattr(queue, "set" + attr[0].upper() + attr[1:])
            assert inspect.cleandoc(getter.__doc__) == note
            assert inspect.cleandoc(setter.__doc__).split("\n")[0] == note

    def test_init_has_no_docstring(self):
        assert CryptoServiceQueue.__init__.__doc__ is None
