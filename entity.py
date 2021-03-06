# abstract class
class Entity:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        # if not a drive
        if parent:
            self.path = parent.path + '\\' + self.name
        else:
            self.path = name

    # raises PathNotFound
    def delete(self):
        self.parent.remove_child(self.name)

    # abstract method
    def get_size(self):
        pass
