import argparse

def func(arr):
    """ """
    arr =[int(num) for num in arr]
    no_dup =[arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i -1]:
            no_dup.append(arr[i])


    return len(no_dup)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arr',nargs='+')
    args = parser.parse_args().arr
    print(func(args))
