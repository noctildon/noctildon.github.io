import time

def write():
    with open('output.txt', 'w') as f:
        f.write(f'Hello from GitHub Actions!! @ {time.ctime()}')

if __name__ == "__main__":
    write()
    print('Written to output.txt')