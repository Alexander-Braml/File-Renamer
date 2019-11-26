import re

path = input('Please enter full path to directory >')

if path.find('\\'):
    path = path.replace('\\', '\\\\')

first_file_name = 'Python3! - ##!2 - ImportantStuff - DeleteThis - NotImportant'

print(f'name of first file is \'{first_file_name}\'')

file_name_seperator = input('Enter seperator >')

first_file_name = first_file_name.split(file_name_seperator)

for idx, fns in enumerate(first_file_name):
    first_file_name[idx] = first_file_name[idx].strip()

idx_output = ''
for idx, fns in enumerate(first_file_name):
    idx_output += f'\'{fns}\' [{idx}]' if idx == 0 else f' | \'{fns}\' [{idx}]'

print(idx_output)

number_idx = int(input('Enter index of number to sort >'))

len_chars_before_num = input('Enter chars in front of number >')

print(f'The first number is {first_file_name[number_idx][len_chars_before_num:]}')

new_order_raw = input('Sort indexes to new indexes >')

print(new_order := re.split('->|,', new_order_raw))

for idx, no in enumerate(new_order):
    new_order[idx] = int(no)

new_name_list = []
for i in range(len(new_order) // 2):
    new_name_list.append('')

for idx_old, idx_new in zip(new_order[::2], new_order[1::2]):
    new_name_list[idx_new] = first_file_name[idx_old]

new_name = ''
for idx, nol in enumerate(new_name_list):
    new_name += f'{nol}' if idx == 0 else f'^{nol}'

print(new_name)

sep_final = input('Any seperators instead of \'^\'? >')

new_name = new_name.replace('^', sep_final)

print(new_name)
