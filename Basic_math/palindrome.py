import argparse

def func(n):
    input = int(n)
    reversed_digit = 0
    while input != 0:
        digit = input % 10
        input = input//10
        reversed_digit = reversed_digit*10 + digit
    if int(n) == reversed_digit:
        return 'Palindrome Number'
    else:
        return 'Not Palindrome Number'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit')
    args = parser.parse_args().digit
    print(func(args))
