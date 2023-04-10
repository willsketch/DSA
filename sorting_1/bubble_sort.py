import argparse

def func(n):
    n = list(n)
    n = [int(num) for num in n]
    for j in range(len(n)):# loop traversing through the array
        # loop for swaps
        n_swaps = 0
        for i in range(len(n) -j - 1):
            if n[i + 1] < n[i]:
                n[i], n[i + 1]  = n[i + 1] , n[i]
                n_swaps += 1

        if n_swaps == 0:
            break
    return n

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit', nargs='+')
    args = parser.parse_args().digit
    print(func(args))

#time complexity is O(n2)
