import argparse

def func(arr, target):
    """ Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
"""
    nums =[int(num) for num in arr]
    # O(n2)  solution
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i, j]

    # optimal O(n) if the d.get() is O(1)
    d ={}
    for i in range(len(nums)):
        if d.get(target -nums[i], 'notfound' ) != 'not found':
            return [d[target-nums[i]], i]
        else:
            d[nums[i]] = i

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
