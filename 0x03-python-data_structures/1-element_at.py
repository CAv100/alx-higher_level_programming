#!/usr/bin/python3
def element_at(my_list, idxy):
    if idxy < 0 or idxy > len(my_list) - 1:
        return 'None'
    else:
        return my_list[idxy]
