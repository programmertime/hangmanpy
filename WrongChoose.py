class WrongChoose(Exception):
    def __init__(self,m) -> None:
        self.message = m

    def __str__(self) -> str:
        return self.message