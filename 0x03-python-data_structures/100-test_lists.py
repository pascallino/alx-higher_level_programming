import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
li = ['hello', 'World']
lib.print_python_list_info(li)
del li[1]
lib.print_python_list_info(li)
li = li + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(li)
li = []
lib.print_python_list_info(li)
li.append(0)
lib.print_python_list_info(li)
li.append(1)
li.append(2)
li.append(3)
li.append(4)
lib.print_python_list_info(li)
li.pop()
lib.print_python_list_info(li)
