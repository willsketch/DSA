import argparse

def func(nums):
    """  find maximum consecutive ones in an array"""
    nums =[int(num) for num in nums]
    best = 0
    c = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            c += 1
        if nums[i] != 1:
            c = 0
        best = max(c, best)

    return best


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
