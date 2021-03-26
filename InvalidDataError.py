class InvalidDataError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Could not process order, data was corrupted. InvalidDataError - {0}'.format(self.message)
        else:
            return 'InvalidDataError has been Raised'

