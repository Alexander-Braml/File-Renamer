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
    for i in range(100):
        with open(f'C:\\RenameDir\\#{i} - DELETEDELETEDELETE - IMPORTANT{i}', 'w+'):
            pass


if __name__ == "__main__":
    ren = Renamer('C:\\RenameDir')
    print(ren.save_files())
    ren.main()
