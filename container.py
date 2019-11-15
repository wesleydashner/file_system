from entity import Entity


class Container(Entity):

    def __init__(self):
        super(Container, self).__init__()
        self.contents = []
