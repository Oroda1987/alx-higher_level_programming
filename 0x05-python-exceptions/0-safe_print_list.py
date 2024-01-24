#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print an integer with "{:d}".format().

    Args:
        my_list (list): The list containing integers.
        x (int): The index of the element to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        If the index is out of range - False.
        Otherwise - True.
    """
    try:
        if 0 <= x < len(my_list):
            print("{:d}".format(my_list[x]))
            return True
        else:
            return False
    except (TypeError, ValueError):
        return False


