class InvalidDataError(Exception):
    def __init__(self, message):
        self.error_message = message

    def get_error_message(self):
        return self.error_message