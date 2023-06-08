from pattern_matching import match

def switch_case(argument):
    match argument:
        case 1:
            # case 1
            print("This is case 1")
        case 2:
            # case 2
            print("This is case 2")
        case 3:
            # case 3
            print("This is case 3")
        case _:
            # default case
            print("This is the default case")
