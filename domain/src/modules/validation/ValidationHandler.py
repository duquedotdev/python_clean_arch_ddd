from typing import List

class ValidationHandler:
    def __init__(self):
        self.errors = []

    def append(self, an_error):
        self.errors.append(an_error)
        return self

    def append_handler(self, an_handler):
        self.errors.extend(an_handler.get_errors())
        return self

    def validate(self, a_validation):
        return a_validation.validate()

    def get_errors(self):
        return self.errors

    def has_error(self):
        return bool(self.errors)

    def first_error(self):
        return self.errors[0] if self.errors else None

    class Validation:
        def validate(self):
            pass
