import re


def split_strip(str_param, seps):
    str_list = re.split(seps, str_param)
    str_list = [item.strip() for item in str_list]
    return str_list


def create_empty_list(len_):
    list_ = []
    for i in range(len_):
        list_.append('')
    return list_


def convert_list_str2int(str_):
    for idx, val in enumerate(str_):
        str_[idx] = int(val)
    return str_


def get_formatted_number(obj, splitted_file_name):
    if obj.fill_with_zeros:
        return splitted_file_name[obj.num_index][obj.num_start:].zfill(obj.max_len)
    else:
        return splitted_file_name[obj.num_index][obj.num_start:]


def format_new_name(obj, splitted_file_name):
    new_name = ''
    for idx, nol in enumerate(sort_new_name(obj, splitted_file_name)):
        new_name += f'{nol}' if idx == 0 else f'**{nol}'
    return new_name + '.' + obj.file_extension


def replace_new_name_stars(obj, new_name):
    return new_name.replace('**', obj.new_name_seperator)


def sort_new_name(obj, file_name_splitted):
    name_list = create_empty_list(len(obj.new_order) // 2)
    for idx_old, idx_new in zip(obj.new_order[::2], obj.new_order[1::2]):
        if idx_old == obj.num_index and obj.fill_with_zeros:
            name_list[idx_new] = file_name_splitted[idx_old][obj.num_start:].zfill(obj.max_len)
        else:
            name_list[idx_new] = file_name_splitted[idx_old]
    return name_list
