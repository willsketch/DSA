import argparse


def func(n):
    n = list(n)
    n = [int(num) for num in n]
    for i in range(1, len(n)): #going through all elements

        for j in range(i, 0, -1):
           #if the element in current position (i) is less than element in
           #previous position (i -1) , swap them
            if n[j] < n[j -1]:
                n[j], n[j -1] = n[j -1], n[j]


    return n

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit', nargs='+')
    args = parser.parse_args().digit
    print(func(args))
