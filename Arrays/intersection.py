import argparse

def func(arr1, arr2):
    """ find intersection nbetween 2 sorted arrays
    O(n2)
    """
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


# def func(arr1, arr2):
#     """ using pointers
#     keep a pointer in each array
#     """
#     ans =[]

#     i, j = 0,0
#     while i < len(arr1) -1 and j < len(arr2) -1:
#         if arr1[i] == arr2[j]:
#             ans.append(arr1[i])
#             i += 1
#             j += 1
#         print(i, j)
#         if arr1[i] < arr2[j]:
#             i += 1
#         if arr1[i] > arr2[j]:
#             j += 1
#         print(ans)
#     return ans



if __name__ == '__main__':
    arr1 = [1 ,2, 3 ,4 ,5, 6, 11]
    arr2 = [1 ,3 ,3 ,10 ,11 ]
    print(func(arr1, arr2))
