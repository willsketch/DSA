import argparse

# def func(arr):
#     """ add zeros to the end of an array
#     my solution
#     """
#     arr =[int(num) for num in arr]
#     zeros = 0
#     temp =[]
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             zeros += 1
#         else:
#             temp.append(arr[i])
#     for i in range(zeros):
#         temp.append(0)
#     return temp


def func(arr):
    """ add zeros to the end of an array"""

    # approach
    # take to pointers l, r: l is first occurance of a 0 and r is l + 1
    # if ele at index  r is non zero, swap and increament l and r
    # if ele at r is 0 only increment r [ 1 2 0 3]
    arr =[int(num) for num in arr]
    l = 0
    while arr[l] != 0:
        l += 1
    r = l + 1

    for i in range(l, len(arr) - 1):
        if arr[r] != 0:
            arr[l], arr[r] = arr[r], arr[l]
            r += 1
            l += 1
        elif arr[r] == 0:
            r += 1
        # elif arr[l] != 0:
        #     l += 1

    return arr

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
