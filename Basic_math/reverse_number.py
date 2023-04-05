import argparse


def func(n):
    n = int(n)
    reversed_digit = 0
    while n != 0:
        digit = n % 10
        n = n//10
        reversed_digit = reversed_digit*10 + digit

    return reversed_digit

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit')
    args = parser.parse_args().digit
    print(func(args))
# time complexity = O(n)
