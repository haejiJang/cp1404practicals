class PromgrammingLanguage:
    """Represent information on programming language"""
    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if language is dynamically typed."""


