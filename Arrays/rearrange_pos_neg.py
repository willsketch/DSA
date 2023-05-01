import argparse

def func(arr):
    """ """
    arr =[int(num) for num in arr]
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
