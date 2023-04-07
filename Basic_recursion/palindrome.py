import argparse

def func(n, i = '', end = -1):
    if end* -1 == len(n) + 1:
        if i == n:

            print('Palidnrome')
        else:

            print('Not palindrome')
        return
    i += n[end]
    func(n, i, end -1)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n')
    n = parser.parse_args().n
    print(func(n= n))
