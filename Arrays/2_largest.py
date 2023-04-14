import argparse

def func(arr):
    """ returns second largest element without
    sorting
    O(n)
    """
    arr =[int(num) for num in arr]
    if arr[0] >= arr[1]:
        max_ele, sec_max = arr[0], arr[1]
    else:
        max_ele, sec_max = arr[1] , arr[0]

    for i in range(2, len(arr)):
        if arr[i] > sec_max:
            sec_max = arr[i]
        if sec_max > max_ele:
            max_ele, sec_max = sec_max, max_ele

    return sec_max




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
