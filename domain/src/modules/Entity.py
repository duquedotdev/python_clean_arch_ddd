from typing import List
from Identifier import Identifier
from events.DomainEvent import DomainEvent
from events.DomainEventPublisher import DomainEventPublisher
from validation.ValidationHandler import ValidationHandler

class Entity:
    def __init__(self, id: Identifier, domain_events: List[DomainEvent] = None):
        if id is None:
            raise ValueError("'id' should not be None")
        self.id = id
        self.domain_events = [] if domain_events is None else domain_events.copy()
        self.validation_handler = ValidationHandler()

    def validate(self, handler):
        return handler.validate(self.validation_handler)

    def get_id(self):
        return self.id

    def get_domain_events(self):
        return list(self.domain_events)

    def publish_domain_events(self, publisher: DomainEventPublisher):
        if publisher is None:
            return

        for event in self.domain_events:
            publisher.publish_event(event)

        self.domain_events.clear()

    def register_event(self, event: DomainEvent):
        if event is not None:
            self.domain_events.append(event)

    def has_error(self):
        return self.validation_handler.has_error()

    def first_error(self):
        return self.validation_handler.first_error()

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Entity):
            return False
        return self.get_id() == other.get_id()

    def __hash__(self):
        return hash(self.get_id())
