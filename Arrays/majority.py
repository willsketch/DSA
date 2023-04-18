import argparse

def func(arr):
    """Given an array of N integers, write a program
    to return an element that occurs more than N/2 times
    in the given array.
    O(2N) , the commented answer is O(N)
    """

    nums =[int(num) for num in arr]
    d = {}
    for val in nums:
        d[val] = d.get(val, 0)  + 1
       #this is also a correct solution that is space optimized
        # if d.get(val, 0) > 0:
        #     if d[val] > len(nums)//2:
        #         return val

    for k, v in d.items():
        if v > len(nums)//2:
            return k

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
