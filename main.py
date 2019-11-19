from drive import Drive
from folder import Folder
from zip import Zip
from text import Text
from controller import Controller


def main():
    controller = Controller()
    controller.create(Drive, 'drive0', None)
    controller.create(Drive, 'drive1', None)
    controller.create(Folder, 'folder0', 'drive0')
    controller.create(Folder, 'folder1', 'drive0')
    controller.create(Folder, 'folder2', 'drive1')
    controller.create(Folder, 'folder3', 'drive1')
    controller.create(Folder, 'my_folder', 'drive0\\folder0')
    controller.create(Text, 'my_text', 'drive0\\folder0\\my_folder')
    controller.write_to_file('drive0\\folder0\\my_folder\\my_text', 'hello world')
    controller.move('drive0\\folder0\\my_folder\\my_text', 'drive0\\folder0\\my_folder\\my_new_text')
    print(controller.get_entity('drive0\\folder0\\my_folder\\my_new_text').content)
    print('drive0 size: ' + str(controller.get_entity('drive0').get_size()))
    controller.create(Zip, 'zip0', 'drive0\\folder1')
    controller.create(Text, 'my_zipped_text', 'drive0\\folder1\\zip0')
    controller.write_to_file('drive0\\folder1\\zip0\\my_zipped_text', 'some really awesome text with a length of 45')
    print('zip0 size: ' + str(controller.get_entity('drive0\\folder1\\zip0').get_size()))
    print('drive0 size: ' + str(controller.get_entity('drive0').get_size()))
    print('folder3 size: ' + str(controller.get_entity('drive1\\folder3').get_size()))
    controller.delete('drive0\\folder0')


main()
