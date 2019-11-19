class Entity:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.path = parent.path + '\\' + self.name

    # raises PathNotFound
    def delete(self):
        self.parent.remove_child(self.name)

    def get_size(self):
        print('ERROR: get_size in Entity called')
