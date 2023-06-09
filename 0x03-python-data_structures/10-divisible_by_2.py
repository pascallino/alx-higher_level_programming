#!/usr/bin/python3
def divisible_by_2(my_list=[]) -> list:
    lstTF = []
    for i in my_list:
        if i % 2 == 0:
            lstTF.append(True)
        else:
            lstTF.append(False)
    return lstTF
