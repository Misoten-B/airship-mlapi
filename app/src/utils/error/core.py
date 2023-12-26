class ResourceNotFoundException(Exception):
    target:str
    def __init__(self,target:str) -> None:
        self.target=target
        super().__init__(f"Resource Not Found:{self.target}")

class ResourceConflictException(Exception):
    target:str
    def __init__(self,target:str) -> None:
        self.target=target
        super().__init__(f"There was a confrict:{self.target}")