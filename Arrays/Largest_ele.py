import argparse

def func(arr):
    """ returns the largest element in an array
    O(n)
    """
    arr =[int(n) for n in arr]
    max_ele = arr[0]
    for i in range(1, len(arr)):
        print(max_ele, arr[i] )
        if arr[i] > max_ele:
            max_ele = arr[i]
    return max_ele

# def func(arr:list):
#     """ returns largest ele in array"""
#     arr =[int(n) for n in arr]
#    # sorting array
#     arr.sort()
#     print(arr)
#     return arr[-1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
