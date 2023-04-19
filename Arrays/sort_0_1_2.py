import argparse

def func(arr):
    """ sort an array that contains 0 1 and 2s
    solution runs in o(n2)
    """
    nums =[int(num) for num in arr]
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[min_idx] > nums[j]:
                nums[min_idx], nums[j] = nums[j], nums[min_idx]
    return nums

def func(arr):
    """ solution in o(n)"""
    nums =[int(num) for num in arr]

    a, b, c = 0,0,0
    for i in range(len(nums)):
        if nums[i] == 0:
            a += 1
        if nums[i] == 1:
            b += 1
        if nums[i] == 2:
            c += 1
    for i in range(a):
        nums[i] = 0
    for i in range(b):
        nums[i + a] = 1
    for i in range(c):
        nums[i + a + b] = 2

    return nums

def func(arr):
    """dutch flag algorithmm
    approach:
    keep 3 pointers low, mid, high
    if arr[mid] = 0 , swap low and mid and increment both
    if arr[miid] = 1 , increment mid
    if arr[mid]  = 2 , swap high & mid and decrement high
    """
    nums =[int(num) for num in arr]

    low, mid = 0,0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
            print(nums, low, mid, high, 0)
        elif nums[mid] == 1:
            mid += 1
            print(nums, low, mid, high, 1)
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            print(nums, low, mid, high, 2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
