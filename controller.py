from drive import Drive


class Controller:

    def __init__(self):
        self.__drives = []

    def __add_drive(self, drive):
        self.__drives.append(drive)

    def __get_entity(self, path):
        path.split('\\')

    def create(self, entity_type, name, parent_path):
        pass

    def delete(self, path):
        pass

    def move(self, source_path, destination_path):
        pass

    def write_to_file(self, path, content):
        pass
