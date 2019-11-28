import os
import Utils
from UserInteraction import UserInteraction


class Renamer:
    def __init__(self):
        ui = UserInteraction()
        self.vals = ui.main()

    def rename_(self, file_name):
        os.rename(file_name, self.get_new_name(file_name))

    def rename_all(self):
        for file in self.vals.files:
            self.rename_(file)

    def get_new_name(self, file_name):
        file_name = file_name.replace('.', '°')
        splitted_file_name = Utils.split_strip(file_name, self.vals.file_name_seperator)
        new_name = Utils.format_new_name(self.vals, splitted_file_name)
        new_name = Utils.replace_new_name_stars(self.vals, new_name)
        return new_name
