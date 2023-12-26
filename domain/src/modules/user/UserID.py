import sys
sys.path.append("../domain")

from Identifier import Identifier
import uuid

class IdUtils:
    @staticmethod
    def uuid():
        return str(uuid.uuid4()).replace("-", "").lower()


class UserID(Identifier):
    def __init__(self, value):
        self.value = value

    @classmethod
    def unique(cls):
        return cls.from_value(IdUtils.uuid())

    @classmethod
    def from_value(cls, an_id):
        return cls(an_id)

    def get_value(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, UserID):
            return self.get_value() == other.get_value()
        return False

    def __hash__(self):
        return hash(self.get_value())
