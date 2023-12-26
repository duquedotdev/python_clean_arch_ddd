import pytest
import sys
sys.path.append('domain/src/modules')

from modules.Identifier import Identifier
from modules.Entity import Entity

@pytest.mark.identifier
def test_identifier_creation():
    identifier = Identifier("uuid")
    entity = Entity(identifier)
    assert entity.get_id() == identifier

@pytest.mark.entity
def test_entity_creation():
    identifier = Identifier("example_id")
    entity = Entity(identifier)
    assert entity.get_id() == identifier
    assert entity.get_domain_events() == list()
    assert not entity.has_error()
    assert entity.first_error() is None
