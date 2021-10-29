class EmptyString(Exception):
    def __init__(self) -> None:
        self.__str__()

    def __str__(self) -> str:
        return "the input cannot be empty..."