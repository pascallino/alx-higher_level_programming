#!/usr/bin/python3
import hidden_4

def print_module_names():
    module_names = dir(hidden_4)
    filtered_names = [name for name in module_names if not name.startswith('__')]
    filtered_names.sort()
    for name in filtered_names:
        print(name)

if __name__ == '__main__':
    print_module_names()
