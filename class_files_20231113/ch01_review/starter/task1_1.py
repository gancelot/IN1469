"""
    task1_1.py

    This file is the main driver for Task 1-1.  It should be run directly (either from the
    command line or from within PyCharm) with one argument provided: the name of the module
    to display the contents of.

"""
import argparse

from utils import list_module_contents


def get_module_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('module')
    return parser.parse_args()


args = get_module_name()

for entry in list_module_contents(args.module):
    print(entry)
