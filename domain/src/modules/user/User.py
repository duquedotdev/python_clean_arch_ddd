from dataclasses import dataclass
from typing import List
from datetime import datetime, date
from uuid import uuid4


@dataclass
class UserID:
    value: str

    @classmethod
    def unique(cls):
        return cls(str(uuid4()))


class ValidationHandler:
    pass  # Implement your validation handler if needed


class UserValidator:
    def __init__(self, user, handler):
        pass  # Implement your validation logic


@dataclass
class User:
    id: UserID
    name: str
    email: str
    birthdate: date
    address: str
    skills: List[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime = None

    def __post_init__(self):
        if self.is_active is None:
            raise ValueError("'is_active' should not be None")

    @classmethod
    def new_user(cls, name, email, birthdate, address, skills, is_active):
        id = UserID.unique()
        now = datetime.now()
        deleted_at = None if is_active else now
        return cls(
            id,
            name,
            email,
            birthdate,
            address,
            skills,
            is_active,
            now,
            now,
            deleted_at
        )


    @classmethod
    def with_data(cls, user_id, name, email, birthdate, address, skills, is_active, created_at, updated_at, deleted_at):
        return cls(
            user_id,
            name,
            email,
            birthdate,
            address,
            skills,
            is_active,
            created_at,
            updated_at,
            deleted_at
        )

    @classmethod
    def with_user(cls, an_user):
        return cls.with_data(
            an_user.id,
            an_user.name,
            an_user.email,
            an_user.birthdate,
            an_user.address,
            an_user.skills,
            an_user.is_active,
            an_user.created_at,
            an_user.updated_at,
            an_user.deleted_at
        )

    def validate(self, handler):
        UserValidator(self, handler).validate()

    def activate(self):
        self.deleted_at = None
        self.is_active = True
        self.updated_at = datetime.now()
        return self

    def deactivate(self):
        if not self.deleted_at:
            self.deleted_at = datetime.now()

        self.is_active = False
        self.updated_at = datetime.now()
        return self

    def update(self, name, email, birthdate, address, skills, is_active):
        if is_active:
            self.activate()
        else:
            self.deactivate()

        self.name = name
        self.email = email
        self.address = address
        self.birthdate = birthdate
        self.skills = skills
        self.updated_at = datetime.now()
        return self
    
