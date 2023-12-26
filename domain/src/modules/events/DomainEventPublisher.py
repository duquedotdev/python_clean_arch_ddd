from abc import ABC, abstractmethod
from events import DomainEvent  # Supondo que você tenha a interface DomainEvent definida em outro arquivo

class DomainEventPublisher(ABC):
    @abstractmethod
    def publish_event(self, event: DomainEvent):
        pass
