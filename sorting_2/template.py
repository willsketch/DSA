import argparse

def func(arr):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit', nargs='+')
    args = parser.parse_args().digit
    print(func(args))
