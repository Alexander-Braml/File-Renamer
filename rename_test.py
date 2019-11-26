file_names = []
for i in range(20):
    file_names.append(f'Python3! - ##!{i} - ImportantStuff - DeleteThis - NotImportant')
new_order_ = ['2', '1', ' 1', '0', ' 0', '2']
sep_final_ = ' - '


def split_strip(str_param, sep):
    str_list = str_param.split(sep)
    str_list = [item.strip() for item in str_list]
    return str_list


def convert_list_str2int(str_):
    for idx, val in enumerate(str_):
        str_[idx] = int(val)
    return str_


def create_empty_list(len_):
    list_ = []
    for i in range(len_):
        list_.append('')

    return list_


def create_new_name(file_name, new_order, sep_final):
    file_name_splitted = split_strip(file_name, sep_final)

    new_order = convert_list_str2int(new_order)

    new_name_list = create_empty_list(len(new_order) // 2)

    for idx_old, idx_new in zip(new_order[::2], new_order[1::2]):
        new_name_list[idx_new] = file_name_splitted[idx_old]

    new_name = ''
    for idx, nol in enumerate(new_name_list):
        new_name += f'{nol}' if idx == 0 else f'^{nol}'

    return new_name.replace('^', sep_final)


for file_name_ in file_names:
    print(create_new_name(file_name_, new_order_, sep_final_))
