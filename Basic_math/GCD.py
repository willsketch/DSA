import argparse

def func(n, m):
    n = int(n)
    m = int(m)
    factors=[]
    for i in range(1, min(n, m) + 1):
        if n%i == 0 and m%i == 0:
            factors.append(i)
    return max(factors)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit_1')
    parser.add_argument('digit_2')
    args_1 = parser.parse_args().digit_1
    args_2 = parser.parse_args().digit_2
    print(func(args_1, args_2))
    #time complexity is O(N)
