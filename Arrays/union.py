import argparse

def func(arr1, arr2):
    """ return union of 2 arrays"""
    arr = arr1 + arr2

   #remove duplicates
    arr = set(arr)

    return arr
if __name__ == '__main__':
    arr1 = [1 ,2, 3 ,4 ,5, 6 ]
    arr2 = [1 ,2 ,3 ,10 ,11 ]
    print(func(arr1, arr2))
