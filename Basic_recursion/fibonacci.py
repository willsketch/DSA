import argparse

def func(n , i =[0, 1]):
    n = int(n)
    if len(i) ==  n + 1:
        print(i)
        return i
    i.append(i[-1] + i[-2])
    func(n, i)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n')

    n = parser.parse_args().n

    print(func(n= n))
