import argparse

def func(arr1, arr2):
    """ find intersection nbetween 2 arrays"""
    temp =[]
    if len(arr1) > len(arr2):
        small = arr2
        big = arr1
    else:
        small = arr1
        big = arr2

    for i in range(len(small)):
        for j in range(len(big)):
            if small[i] == big[j]:
                temp.append(arr1[i])

    return temp
if __name__ == '__main__':
    arr1 = [1 ,2, 3 ,4 ,5, 6, 1 ]
    arr2 = [1 ,2 ,3 ,10 ,11 , 1]
    print(func(arr1, arr2))
