from abc import ABC, abstractmethod
from datetime import datetime

class DomainEvent(ABC):
    @abstractmethod
    def occurred_on(self):
        pass
