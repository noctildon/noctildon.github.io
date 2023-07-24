"""
Purpose of self-made modules: modulize the code
Write the code to a file, use import to import the file

Module ~ python file ~ package ~ library
"""


e_num = 2.7
def circle(r):
    return 3.14 * r**2

print('Can you see me? - mod1.py')
print(f'__name__ in mod1.py: {__name__}')

if __name__ == '__main__':
    # mod.py can't see this
    print("You cant see me - mod1.py")