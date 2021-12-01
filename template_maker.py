from distutils.dir_util import copy_tree
import os

day = input("Enter Day: ")
os.mkdir(f'day{day}')
copy_tree('template', f'day{day}')
os.rename(f'day{day}/template.py', f'day{day}/day{day}.py')
