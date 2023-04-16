import argparse

def func(nums):
    """ find missing number
    brute force
    """
    nums =[int(n) for n in nums]
    check = list(range(len(nums) + 1))
    for i in range(len(check)):
        for j in range(len(nums)):
            if i == nums[j]:
                check[i] = -1

    for i in check:
        if i >= 0:
            return i


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
