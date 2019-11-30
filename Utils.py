def split_strip(str_param, sep):
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
        # str_list.remove(str_list[-1])
        return str_list
    else:
        str_list = str_param.split(sep)
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
    val = str(int(splitted_file_name[obj.num_index][obj.num_start:]))
    if obj.fill_with_zeros:
        return val.zfill(obj.max_len)
    else:
        return val


def format_new_name(obj, splitted_file_name):
    new_name = ''
    for idx, nol in enumerate(sort_new_name(obj, splitted_file_name)):
        new_name += f'{nol}' if idx == 0 else f'**{nol}'
    return new_name + '.' + obj.file_extension


def replace_new_name_stars(obj, new_name):
    return new_name.replace('**', obj.new_name_delimiter)


def sort_new_name(obj, file_name_splitted):
    name_list = create_empty_list(int(len(obj.new_order) / 2))
    for idx_old, idx_new in zip(obj.new_order[::2], obj.new_order[1::2]):
        if idx_old == obj.num_index:
            val = str(int(file_name_splitted[idx_old][obj.num_start:]))
            if obj.fill_with_zeros:
                name_list[idx_new] = val.zfill(obj.max_len)
            else:
                name_list[idx_new] = val
        else:
            name_list[idx_new] = file_name_splitted[idx_old]
    return name_list
