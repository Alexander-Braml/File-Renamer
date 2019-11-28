import re
import os
from os.path import isfile, join
import Utils
from Variables import Variables


class UserInteraction:
    def __init__(self):
        self.vals = Variables()

    def main(self):
        self.ask_user_data()
        return self.vals

    def ask_user_data(self):
        self.save_path()
        self.save_files()
        first_file_name = self.vals.files[0]
        print(f'name of first file is \'{first_file_name}\'')
        first_file_name = first_file_name.replace('.', '°')
        self.save_seperator()
        first_file_name = self.split_strip_user(first_file_name, self.vals.file_name_seperator)
        idx_output = ''
        for idx, fns in enumerate(first_file_name):
            idx_output += f'\'{fns}\' [{idx}]' if idx == 0 else f' | \'{fns}\' [{idx}]'
        print(idx_output)
        self.save_num_index()
        self.save_num_start()
        self.save_fill_with_zeros()
        self.save_num_len()
        print(f'The first number is {Utils.get_formatted_number(self.vals, first_file_name)}')
        self.save_process_index_order()
        new_name = Utils.format_new_name(self.vals, first_file_name)
        print(new_name)
        self.save_new_name_seperator()
        new_name = Utils.replace_new_name_stars(self.vals, new_name)
        print(new_name)

    def save_path(self):
        self.vals.path = input('Please enter full path to directory >')
        if self.vals.path.find('\\'):
            self.vals.path = self.vals.path.replace('\\', '\\\\')
        os.chdir(self.vals.path)

    def save_files(self):
        self.vals.files = [f for f in os.listdir(self.vals.path) if isfile(join(self.vals.path, f))]

    def save_seperator(self):
        self.vals.file_name_seperator = input('Enter seperator >') + '|°'

    def split_strip_user(self, str_param, seps):
        str_list = re.split(seps, str_param)
        str_list = [item.strip() for item in str_list]
        self.vals.file_extension = str_list[-1]
        str_list.remove(str_list[-1])
        return str_list

    def save_num_index(self):
        self.vals.num_index = int(input('Enter index of number to sort >'))

    def save_num_start(self):
        self.vals.num_start = len(input('Enter chars in front of number >'))

    def save_fill_with_zeros(self):
        self.vals.fill_with_zeros = bool(input('Fill space before number with zeros? >'))

    def save_num_len(self):
        self.vals.max_len = 0
        for file in self.vals.files:
            current_len = len(file.split(self.vals.file_name_seperator))  # [self.num_index].strip()[self.num_start:])
            if self.vals.max_len < current_len:
                self.vals.max_len = current_len

    def save_process_index_order(self):
        new_order_raw = input('Sort indexes to new indexes >')
        for idx, no in enumerate(re.split('->|,', new_order_raw)):
            self.vals.new_order.append(int(no))

    def save_new_name_seperator(self):
        self.vals.new_name_seperator = input('Enter seperator instead of \'**\' >')
