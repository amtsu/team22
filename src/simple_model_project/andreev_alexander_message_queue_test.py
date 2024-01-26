import pytest

from andreev_alexander_message_queue import MessageQueue, createinstance


@pytest.fixture
def class_instance() -> MessageQueue:
    return MessageQueue()


def test_createinstance(class_instance: MessageQueue):
    cls_instance = createinstance()
    assert type(cls_instance) == type(class_instance)

def test_name_method(class_instance: MessageQueue):
    assert "andreev_alexander_message_queue" == class_instance.name()

def test_that_prepare_method_returns_none(class_instance: MessageQueue):
    assert class_instance.prepare() is None

def test_that_prepare_method_returns_message_queue(class_instance: MessageQueue):
    cls_instance = createinstance()
    assert len(cls_instance.queue) == len(class_instance.queue)
