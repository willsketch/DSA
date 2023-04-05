import argparse

def func(n):
    n = int(n)
    divisors =[]
    for i in range(1, n +1):
        if n % i == 0:
            divisors.append(i)


    return divisors

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit')
    args = parser.parse_args().digit
    print(func(args))

   #time complexity is O(n)
