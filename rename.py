import os
from os import listdir
from os.path import isfile, join


class Renamer:
    def __init__(self, path):
        os.chdir(path)
        self.path = path

    def main(self):
        pass

    def save_files(self):
        onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        print(onlyfiles)


def create_test_files():
    for i in range(1001):
        with open(f'C:\\RenameDir\\Python3! - ##!{i} - ImportantStuff - DeleteThis - NotImportant.txt', 'w+'):
            pass


if __name__ == "__main__":
    ren = Renamer('C:\\RenameDir')
    create_test_files()
    print(ren.save_files())
    ren.main()
