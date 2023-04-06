import argparse

def func(n):
    n = int(n)
    for i in range(1, n + 1):
        print('*' * i)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit')
    args = parser.parse_args().digit
    print(func(args))
