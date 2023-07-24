"""
Use import to import the module
You can import as many as you want
Be careful of the name conflict
"""

from mod_child import circle, e_num
# from mod1 import * # import all
# from folder.module import *  use . to access the module under a directory


print(f'variable from mod1: {e_num}')
print(f'function from mod1: {circle(3)}')