import argparse

def func(arr):
    """ """
    arr =[int(num) for num in arr]
    low = 0
    maxProfit = 0
    for i in range(len(arr)):
        if arr[i] >= arr[low]:
            maxProfit = max(arr[i] - arr[low], maxProfit)
        else:
            low = i


    return maxProfit

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
