import re
from os import listdir
from os.path import isfile, join


path = input('Please enter full path to directory >')

if path.find('\\'):
    path = path.replace('\\', '\\\\')

files = [f for f in listdir(path) if isfile(join(path, f))]

# --------------------------------------------------------- #

first_file_name = files[0]

print(f'name of first file is \'{first_file_name}\'')

# --------------------------------------------------------- #

file_name_seperator = input('Enter seperator >')

first_file_name = first_file_name.split(file_name_seperator)

for idx, fns in enumerate(first_file_name):
    first_file_name[idx] = first_file_name[idx].strip()

# --------------------------------------------------------- #

idx_output = ''
for idx, fns in enumerate(first_file_name):
    idx_output += f'\'{fns}\' [{idx}]' if idx == 0 else f' | \'{fns}\' [{idx}]'

print(idx_output)

# --------------------------------------------------------- #

number_idx = int(input('Enter index of number to sort >'))

len_chars_before_num = len(input('Enter chars in front of number >'))

fill_with_zeros = bool(input('Fill space before number with zeros? >'))

# --------------------------------------------------------- #

if fill_with_zeros:
    max_len = 0
    for file in files:
        current_len = len(file.split(file_name_seperator)[number_idx].strip()[len_chars_before_num:])
        if max_len < current_len:
            max_len = current_len
    print(f'The first number is {first_file_name[number_idx][len_chars_before_num:].zfill(max_len)}')
else:
    print(f'The first number is {first_file_name[number_idx][len_chars_before_num:]}')

# --------------------------------------------------------- #

new_order_raw = input('Sort indexes to new indexes >')

print(new_order := re.split('->|,', new_order_raw))

for idx, no in enumerate(new_order):
    new_order[idx] = int(no)

# --------------------------------------------------------- #

new_name_list = []
for i in range(len(new_order) // 2):
    new_name_list.append('')

for idx_old, idx_new in zip(new_order[::2], new_order[1::2]):
    new_name_list[idx_new] = first_file_name[idx_old] if idx_old != number_idx else first_file_name[idx_old][len_chars_before_num:].zfill(max_len)

# --------------------------------------------------------- #

new_name = ''
for idx, nol in enumerate(new_name_list):
    new_name += f'{nol}' if idx == 0 else f'**{nol}'

print(new_name)

# --------------------------------------------------------- #

sep_final = input('Enter seperator instead of \'**\' >')

new_name = new_name.replace('**', sep_final)

print(new_name)
