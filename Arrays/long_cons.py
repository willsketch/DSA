import argparse

def func(arr):
    """ O(n)"""
    nums =[int(num) for num in arr]
    i = 0
    long_cons = 1
    current_cons= [nums[i]]
    while i < len(nums) -1:
        if nums[i + 1] == nums[i] + 1:
            # print(long_cons, current_cons, 1)
            current_cons.append(nums[i + 1])
        else:
            # print(long_cons, current_cons, 2)

            long_cons = max(long_cons, len(current_cons))
            current_cons = [nums[i + 1]]
        i += 1
    long_cons = max(long_cons, len(current_cons))
    return long_cons

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
