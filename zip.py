from container import Container


class Zip(Container):

    def get_size(self):
        return super(Zip, self).get_size() // 2
