#!/usr/bin/python3
if __name__ == "__main__":
    import variable_load_5
#   from variable_load_5 import a
#    print(a);
    value = variable_load_5.__dict__['a']
    print("{}".format(value))
