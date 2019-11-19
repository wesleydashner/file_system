from entity import Entity


class Text(Entity):

    def __init__(self):
        super(Text, self).__init__(name, parent)
        self.content = ''

    def get_size(self):
        return len(self.content)
