import argparse

def func(arr):
    """ """
    nums =[int(num) for num in arr]
    pos = []
    neg = []
    for i in nums:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    n = 0
    for i, j in zip(pos, neg):
        nums[n] = i
        nums[n + 1] = j
        n += 2

    return nums

def optimalfunc(arr):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
