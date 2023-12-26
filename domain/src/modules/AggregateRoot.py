from typing import List
from Identifier import Identifier  
from Entity import Entity  
from events.DomainEvent import DomainEvent  

class AggregateRoot(Entity):
    def __init__(self, id: Identifier, events: List[DomainEvent] = None):
        super().__init__(id, events)