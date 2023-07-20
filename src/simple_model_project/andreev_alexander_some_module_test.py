import pytest

from andreev_alexander_some_module import Modeling, createinstance


@pytest.fixture
def class_instance() -> Modeling:
    return Modeling()

def test_createinstance(class_instance: Modeling):
    cls_instance = createinstance()
    assert type(cls_instance) == type(class_instance)

def test_name_method(class_instance: Modeling):
    assert "andreev_alexander_some_module" == class_instance.name()

def test_prepare_method(class_instance: Modeling):
    assert class_instance.prepare() is None
