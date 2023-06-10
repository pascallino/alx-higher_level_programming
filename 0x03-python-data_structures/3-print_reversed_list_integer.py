#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 1:
        print("{:d}".format(my_list[0]))
        #    my_list.reverse()
    else:
        my_list.reverse()
        for itm in range(0, len(my_list)):
            print("{:d}".format(my_list[itm]))
