import argparse

def func(arr, k=1):
    """ """
    arr =[int(num) for num in arr]
    return arr[-k:] + arr[:-k]
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
