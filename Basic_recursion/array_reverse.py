import argparse

def func(n , i=[]):
    n = list(n)
    i = list(i)
    if len(n) == 0:
        print(i)
        return i
    i.append(n.pop())
    func(n, i)

def func2(arr, start= 0, end = 5):
    start = int(start)
    end = int(end)
    if start > end:
        arr[start] = arr[end]
        arr[end] = arr[start]
        func2(arr, start + 1, end - 1)

    print(arr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', nargs='+')

    n = parser.parse_args().n

    print(func2(n))
