import argparse

# def func(arr):
#     """ brute force solution"""
#     nums =[int(num) for num in arr]
#     leaders = []
#     for i in range(len(nums)):
#         leader = True
#         for j in range(i + 1, len(nums)):
#             if nums[j] > nums[i]:
#                 leader = False
#         if leader:
#             leaders.append(nums[i])
#     return leaders
def func(arr):
    """optimal solution O(n)"""
    nums =[int(num) for num in arr]
    i = len(nums) -1
    max_ele = nums[i]
    leaders =[max_ele]

    while i > 0:
        if nums[i] > max_ele:
            max_ele = nums[i]
            leaders.append(nums[i])
        i -= 1
    return leaders


    pass
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
