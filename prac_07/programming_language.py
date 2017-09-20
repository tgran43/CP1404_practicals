class ProgrammingLanguage:
    def __init__(self, language="", typing="", reflection=False, year=0):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.language = language

    def __str__(self):
        return str(
            "{}, {} Typing, Reflection={}, First appeared in {}".format(self.language, self.typing, self.reflection,
                                                                        self.year))

    def is_dynamic(self):
        if self.typing.upper() == "DYNAMIC":
            return True
        else:
            return False
