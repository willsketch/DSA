import argparse

def func(n , i):
    n = int(n)
    i = int(i)
    if i > n:
        return
    print(n)
    func(n -1, i)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n')
    parser.add_argument('i')
    n = parser.parse_args().n
    i = parser.parse_args().i
    print(func(n= n, i= i))
