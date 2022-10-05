open_num = 3.14
def squ(x):
    return x**2

print('Can you see me? - mod1.py')
print(f'__name__ in mod1.py: {__name__}')

if __name__ == '__main__':
    # mod.py can't see this
    print("You cant see me - mod1.py")