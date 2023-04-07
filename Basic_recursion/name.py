import argparse


def func(n, i):
    n = int(n)
    i = int(i)
    if i > n:
        return
    print('name', i)
    func(n, i+1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit_1')
    parser.add_argument('digit_2')
    args_1 = parser.parse_args().digit_1
    args_2 = parser.parse_args().digit_2
    print(func(args_1, args_2))
