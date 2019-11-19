from container import Container


class Drive(Container):

    def __init__(self, name):
        self.name = name
        self.path = name
        self.parent = None
        self.contents = []
