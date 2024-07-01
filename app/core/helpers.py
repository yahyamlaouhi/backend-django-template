class ObjectAlreadyExists(Exception):
    """Exception raised when an object already exists."""

    def __init__(self, message="Object already exists"):
        self.message = message
        super().__init__(self.message)
