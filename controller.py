from drive import Drive
from exceptions import *
from text import Text


class Controller:

    def __init__(self):
        self.__drives = []

    def add_drive(self, drive):
        if type(drive) == Drive:
            self.__drives.append(drive)
            return True
        return False

    # raises PathNotFound
    def get_entity(self, path):
        path = path.split('\\')
        drive_found = False
        for drive in self.__drives:
            if drive.name == path[0]:
                entity = drive
                drive_found = True
        if not drive_found:
            raise PathNotFound()
        for item_name in path[1:]:
            found = False
            for sub_item in entity.contents:
                if sub_item.name == item_name:
                    entity = sub_item
                    found = True
                    break
            if not found:
                raise PathNotFound()
        return entity

    # raises PathNotFound, IllegalFileSystemOperation, PathAlreadyExists
    def create(self, entity_type, name, parent_path):
        if entity_type == Drive and not parent_path:
            self.add_drive(Drive(name))
            return
        parent = self.get_entity(parent_path)
        if type(parent) == Text:
            raise IllegalFileSystemOperation('parent is a text file')
        if entity_type == Drive and parent_path:
            raise IllegalFileSystemOperation('drive cannot have a parent')
        try:
            self.get_entity(parent_path + '\\' + name)
            raise PathAlreadyExists
        except PathNotFound:
            parent.add_child(entity_type(name, parent))

    # raises PathNotFound
    def delete(self, path):
        self.get_entity(path).delete()

    # raises PathNotFound
    def move(self, source_path, destination_path):
        entity = self.get_entity(source_path)
        entity.delete()
        # TODO: add entity at destination_path

    def write_to_file(self, path, content):
        pass
