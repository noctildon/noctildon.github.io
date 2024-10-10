def write():
    with open('output.txt', 'w') as f:
        f.write('Hello from GitHub Actions!!')

if __name__ == "__main__":
    write()
    print('Written to output.txt')