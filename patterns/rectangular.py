import argparse

def func(n):
    n = int(n)
    for i in range(n):
        print('*' * n)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit')
    args = parser.parse_args().digit
    print(func(args))
