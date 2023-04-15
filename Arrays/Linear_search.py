import argparse

def func(arr, num =3, start=0):
    """ search for num in an array """
    arr =[int(num) for num in arr]
    if start == len(arr):
        return
    if arr[start] == num:
        print(start)
    else:
        print(-1)
    func(arr, num, start + 1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
