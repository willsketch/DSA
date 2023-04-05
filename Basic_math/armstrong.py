import argparse

def func(n):
    n = str(n)
    check = 0
    length = len(n)
    for i in n:
        check += int(i)**length
    if int(n) == check:
        return 'Yes, it is an Armstrong Number'
    else:
        return 'No, it is not  an Armstrong Number'
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit')
    args = parser.parse_args().digit
    print(func(args))
#Time complexity is O(n)
