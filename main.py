from entity import Entity
from container import Container
from drive import Drive
from folder import Folder
from zip import Zip
from text import Text
from controller import Controller


def main():
    controller = Controller()
    folder = Folder('hello', 'hello')
    print(type(folder) == Container)


main()
