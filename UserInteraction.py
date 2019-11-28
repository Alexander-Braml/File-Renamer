import re
from os import chdir, listdir
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
        self.save_delimiter(first_file_name)
        first_file_name = first_file_name.replace('.', self.vals.file_name_delimiter)
        first_file_name = self.split_strip(first_file_name, self.vals.file_name_delimiter)
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
        self.save_new_name_delimiter()
        new_name = Utils.replace_new_name_stars(self.vals, new_name)
        print(new_name)

    def save_path(self):
        tmp = ''
        valid = False
        while not valid:
            tmp = input('Please enter full path to directory >')
            try:
                chdir(tmp)
                if not [f for f in listdir(tmp) if isfile(join(tmp, f))]:
                    print('No files in directory! Try another path!')
                    continue
                valid = True
            except FileNotFoundError:
                print('No valid path! Try another path!')
                valid = False
        else:
            self.vals.path = tmp
            if self.vals.path.find('\\'):
                self.vals.path = self.vals.path.replace('\\', '\\\\')
            chdir(self.vals.path)

    def save_files(self):
        tmp = [f for f in listdir(self.vals.path) if isfile(join(self.vals.path, f))]
        self.vals.files = tmp

    def save_delimiter(self, first_file_name):
        tmp = ''
        valid = False
        while not valid:
            tmp = input('Enter delimiter >')
            if first_file_name.find(tmp) == -1:
                print('Could not find delimiter in String! Try another delimiter!')
                valid = False
            elif tmp == '':
                print('Delimiter can\'t be empty! Try another delimiter!')
                valid = False
            else:
                valid = True
        else:
            self.vals.file_name_delimiter = tmp

    def split_strip(self, str_param, sep):
        str_param += ' '
        if sep == '+':
            str_list = []
            index = 0
            while index < len(str_param):
                prev_index = index
                index = str_param.find('+', index)
                str_list.append(str_param[prev_index:index])
                if index == -1:
                    break
                index += 1
            str_list = [item.strip() for item in str_list]
            print(str_list)
            self.vals.file_extension = str_list[-1]
            str_list.remove(str_list[-1])
            return str_list
        else:
            str_list = str_param.split(sep)
            str_list = [item.strip() for item in str_list]
            self.vals.file_extension = str_list[-1]
            str_list.remove(str_list[-1])
            return str_list

    def save_num_index(self):  # stopped implementing failsaife
        self.vals.num_index = int(input('Enter index of number to sort >'))

    def save_num_start(self):
        self.vals.num_start = len(input('Enter chars in front of number >'))

    def save_fill_with_zeros(self):
        self.vals.fill_with_zeros = bool(input('Fill space before number with zeros? >'))

    def save_num_len(self):
        self.vals.max_len = len(str(len(self.vals.files)))

    def save_process_index_order(self):
        new_order_raw = input('Sort indexes to new indexes >')
        for idx, no in enumerate(re.split('->|,', new_order_raw)):
            self.vals.new_order.append(int(no))

    def save_new_name_delimiter(self):
        self.vals.new_name_delimiter = input('Enter delimiter instead of \'**\' >')
