class ResourceNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__("Resource Not Found")

class ResourceConflictException(Exception):
    def __init__(self) -> None:
        super().__init__("There was a confrict")