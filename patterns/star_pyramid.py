import argparse

def func(n):
    n = int(n)
    for i in range(n):
        for s in range(n-i-1):
            print(' ', end='')
        for j in range(2*i + 1):
            print('*', end='')
        for p in range(n-i-1):
            print(' ', end='')
        print('\r')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit')
    args = parser.parse_args().digit
    print(func(args))
