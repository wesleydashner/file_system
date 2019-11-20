from container import Container


class Drive(Container):

    def __init__(self, name):
        # drives have no parent, so None is passed in
        super(Drive, self).__init__(name, None)
