import argparse

def func(arr):
    """ """
    arr =[int(num) for num in arr]
    sorted = True
    min_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            sorted = False
            break
        min_val = arr[i]
    return sorted

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
