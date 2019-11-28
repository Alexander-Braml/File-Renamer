import re
import os
from os.path import isfile, join


class Renamer:
    def __init__(self):
        self.path = ''
        self.files = []
        self.file_extension = ''
        self.file_name_seperator = ''
        self.num_index = 0
        self.num_start = 0
        self.fill_with_zeros = False
        self.new_order = []
        self.new_name_seperator = ''
        self.max_len = 0

    @staticmethod
    def split_strip(str_param, seps):
        str_list = re.split(seps, str_param)
        str_list = [item.strip() for item in str_list]
        return str_list

    def split_strip_user(self, str_param, seps):
        str_list = re.split(seps, str_param)
        str_list = [item.strip() for item in str_list]
        self.file_extension = str_list[-1]
        str_list.remove(str_list[-1])
        return str_list

    @staticmethod
    def convert_list_str2int(str_):
        for idx, val in enumerate(str_):
            str_[idx] = int(val)
        return str_

    @staticmethod
    def create_empty_list(len_):
        list_ = []
        for i in range(len_):
            list_.append('')
        return list_

    def save_files(self):
        self.files = [f for f in os.listdir(self.path) if isfile(join(self.path, f))]

    def save_path(self):
        self.path = input('Please enter full path to directory >')
        if self.path.find('\\'):
            self.path = self.path.replace('\\', '\\\\')
        os.chdir(self.path)

    def save_seperator(self):
        self.file_name_seperator = input('Enter seperator >') + '|°'

    def save_num_index(self):
        self.num_index = int(input('Enter index of number to sort >'))

    def save_num_start(self):
        self.num_start = len(input('Enter chars in front of number >'))

    def save_num_len(self):
        self.max_len = 0
        for file in self.files:
            current_len = len(file.split(self.file_name_seperator))  # [self.num_index].strip()[self.num_start:])
            if self.max_len < current_len:
                self.max_len = current_len

    def save_fill_with_zeros(self):
        self.fill_with_zeros = bool(input('Fill space before number with zeros? >'))

    def get_formatted_number(self, splitted_file_name):
        if self.fill_with_zeros:
            return splitted_file_name[self.num_index][self.num_start:].zfill(self.max_len)
        else:
            return splitted_file_name[self.num_index][self.num_start:]

    def save_process_index_order(self):
        new_order_raw = input('Sort indexes to new indexes >')
        for idx, no in enumerate(re.split('->|,', new_order_raw)):
            self.new_order.append(int(no))

    def sort_new_name(self, file_name_splitted):
        name_list = self.create_empty_list(len(self.new_order) // 2)
        for idx_old, idx_new in zip(self.new_order[::2], self.new_order[1::2]):
            if idx_old == self.num_index and self.fill_with_zeros:
                name_list[idx_new] = file_name_splitted[idx_old][self.num_start:].zfill(self.max_len)
            else:
                name_list[idx_new] = file_name_splitted[idx_old]
        return name_list

    def format_new_name(self, splitted_file_name):
        new_name = ''
        for idx, nol in enumerate(self.sort_new_name(splitted_file_name)):
            new_name += f'{nol}' if idx == 0 else f'**{nol}'
        return new_name + '.' + self.file_extension

    def save_new_name_seperator(self):
        self.new_name_seperator = input('Enter seperator instead of \'**\' >')

    def replace_new_name_stars(self, new_name):
        return new_name.replace('**', self.new_name_seperator)

    def ask_user_data(self):
        self.save_path()
        self.save_files()
        first_file_name = self.files[0]
        print(f'name of first file is \'{first_file_name}\'')
        first_file_name = first_file_name.replace('.', '°')
        self.save_seperator()
        first_file_name = self.split_strip_user(first_file_name, self.file_name_seperator)
        idx_output = ''
        for idx, fns in enumerate(first_file_name):
            idx_output += f'\'{fns}\' [{idx}]' if idx == 0 else f' | \'{fns}\' [{idx}]'
        print(idx_output)
        self.save_num_index()
        self.save_num_start()
        self.save_fill_with_zeros()
        self.save_num_len()
        print(f'The first number is {self.get_formatted_number(first_file_name)}')
        self.save_process_index_order()
        new_name = self.format_new_name(first_file_name)
        print(new_name)
        self.save_new_name_seperator()
        new_name = self.replace_new_name_stars(new_name)
        print(new_name)

    def rename_(self, file_name):
        orig_file_name = file_name
        file_name = file_name.replace('.', '°')
        splitted_file_name = self.split_strip(file_name, self.file_name_seperator)
        new_name = self.format_new_name(splitted_file_name)
        new_name = self.replace_new_name_stars(new_name)
        os.rename(orig_file_name, new_name)

    def rename_all(self):
        for file in self.files:
            self.rename_(file)


if __name__ == '__main__':
    ren = Renamer()
    ren.ask_user_data()
    ren.rename_all()
    print(f'Renamed {len(ren.files)} files!')
