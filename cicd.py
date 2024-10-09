import sys

def write():
    with open('file.txt', 'w') as f:
        f.write('Hello from GitHub Actions!!')

def main():
    print("Hello from GitHub Actions!")
    print('Python version: ', sys.version)
    write()

if __name__ == "__main__":
    main()