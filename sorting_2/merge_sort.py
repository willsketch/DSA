import argparse

def merge(arr, low, mid, high):
    left, right = low, mid + 1
    temp = []

    while left <= mid and  right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low , high + 1):
        arr[i] = temp[i - low]


def mergeSort(arr, low , high):
    if low == high:
        return arr
    mid = (low + high)//2

    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high )
    merge(arr, low , mid, high)

    return arr

if __name__ == '__main__':
    arr = [12,13, 78, 2, 14, 46]
    low , high = 0, len(arr) -  1
    print(mergeSort(arr, low, high))
