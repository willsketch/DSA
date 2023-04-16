import argparse

def func(nums):
    """ return a number that has a frequency of one"""
    nums =[int(num) for num in nums]
    freq = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                # print(nums[i], nums[j])
                freq += 1
        # print(freq, nums[i], 'freq')
        if freq == 1:
            return nums[i]
        freq = 0
    return 0



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
