#!/asr/bin/python3
def new_in_list(my_list, idx, element):
    # my_list2 = list.copy(my_list)
    my_list2 = []
    for item in my_list:
        my_list2.append(item)
    if idx < 0:
        return my_list2
    elif idx > len(my_list2) - 1:
        return my_list2
    else:
        my_list2[idx] = element
        return my_list2
