import argparse

def func(arr):
    """ """
    nums =[int(num) for num in arr]
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[min_idx] > nums[j]:
                nums[min_idx], nums[j] = nums[j], nums[min_idx]
    return nums


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
