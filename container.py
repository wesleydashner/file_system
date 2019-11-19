from entity import Entity
from exceptions import *


class Container(Entity):

    def __init__(self, name, parent):
        super(Container, self).__init__(name, parent)
        self.contents = []

    def add_child(self, child):
        self.contents.append(child)

    # raises PathNotFound
    def remove_child(self, name):
        found = False
        for item in self.contents:
            if item.name == name:
                self.contents.remove(item)
                found = True
        if not found:
            raise PathNotFound()

    def get_size(self):
        total = 0
        for entity in self.contents:
            total += entity.get_size()
        return total
