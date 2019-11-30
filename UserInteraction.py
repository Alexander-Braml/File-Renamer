import re
from os import chdir, listdir
from os.path import isfile, join
import Utils
from Variables import Variables


class UserInteraction:
    def __init__(self):
        self.vals = Variables()
        self.help = '''HELP
-
Steps to automated renaming:
    1. Enter path
        Enter the full path to all the files.
    2. Enter delimiter
        Enter the delimiter you want to use to split the file name.
    3. Enter index of number in file name
        Enter the index (shown in square brackets) of the number to sort the files.
    4. Enter fill with zeros
        Enter \'y\' or \'n\' if you want to either fill the number with zeros or you dont.
    5. Sort indexes to new indexes
        Syntax: oldIndex->newIndex, oldIndex2->newIndex2
        Use \'->\' to separate old and new indexes.
        Use \',\' to separate blocks of new and old indexes.
    [ 6. Enter delimiter of new file name ]
    [   The new name is shown above separated with \'**\'. ]
    [   You can the change delimiter or, if you leave it blank, no delimiter will be used. ]        
'''

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
        self.save_num_index(first_file_name)
        self.save_num_start(first_file_name)
        self.save_fill_with_zeros()
        self.save_num_len()
        print(f'The first number is {Utils.get_formatted_number(self.vals, first_file_name)}')
        self.save_process_index_order()
        new_name = Utils.format_new_name(self.vals, first_file_name)
        print(new_name)
        if '**' in new_name:
            self.save_new_name_delimiter()
            new_name = Utils.replace_new_name_stars(self.vals, new_name)
            print(new_name)

    def save_path(self):
        tmp = ''
        valid = False
        while not valid:
            tmp = input('Please enter full path to directory >')
            if tmp.upper() == 'H' or tmp == '?' or tmp.upper() == 'HELP':
                print(self.help)
                valid = False
                continue
            else:
                try:
                    chdir(tmp)
                    if not [f for f in listdir(tmp) if isfile(join(tmp, f))]:
                        print('No files in directory! Try another path!')
                        continue
                    valid = True
                except (FileNotFoundError, OSError):
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

    def save_num_index(self, file_name_splitted):
        tmp = ''
        valid = False
        while not valid:
            tmp = input('Enter index of number to sort >')
            try:
                tmp_int = int(tmp)
            except ValueError:
                print('Enter a number!')
                valid = False
                continue
            if tmp_int >= len(file_name_splitted) or tmp_int < 0:
                print('Index is out of range!')
                valid = False
                continue
            correct_index = False
            for i in range(10):
                if str(i) in file_name_splitted[tmp_int]:
                    correct_index = True
                    valid = True
                    break
                else:
                    correct_index = False
                    valid = False
            if not correct_index:
                print('Part of file name does not contain a number!')
                valid = False
                continue

        self.vals.num_index = int(tmp)

    def save_num_start(self, file_name):
        start_index = 0
        part = file_name[self.vals.num_index]
        valid = False
        while not valid:
            try:
                int(part[start_index:])
                valid = True
            except ValueError:
                valid = False
                start_index += 1
        self.vals.num_start = start_index

    def save_fill_with_zeros(self):
        valid = False
        while not valid:
            tmp = input('Fill space before number with zeros? (y/n) >')
            if tmp == 'y':
                self.vals.fill_with_zeros = True
                valid = True
            elif tmp == 'n':
                self.vals.fill_with_zeros = False
                valid = True
            else:
                print('Enter \'y\' or \'n\'!')
                valid = False

    def save_num_len(self):
        self.vals.max_len = len(str(len(self.vals.files)))

    def save_process_index_order(self):
        tmp = []
        valid = False
        while not valid:
            new_order_raw = input('Sort indexes to new indexes >')
            tmp = []
            splitted = re.split('->|,', new_order_raw)
            len_ = len(splitted)
            if len_ % 2 != 0:
                print('Length is not even!')
                valid = False
                continue
            for idx, no in enumerate(splitted):
                try:
                    num = int(no)
                    if num >= int(len_ / 2):
                        print('Indexes can\'t be greater than length of new name!')
                        valid = False
                        break
                    else:
                        valid = True
                except ValueError:
                    print('All indexes need to be numbers!')
                    valid = False
                    break
                tmp.append(int(no))
        self.vals.new_order = tmp

    def save_new_name_delimiter(self):
        self.vals.new_name_delimiter = input('Enter delimiter instead of \'**\' >')
