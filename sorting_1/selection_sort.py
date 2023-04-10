import argparse

def func(n:list):

    n = list(n)
    n = [int(num) for num in n]
   # loop to keep track of sorted index
    for i in range(len(n)):
        min_index = i
        #loop to check if an index is bigger than min index
        for j in range(i +1, len(n)):
            if n[min_index] > n[j]:
                min_index = j

        n[i], n[min_index]  = n[min_index], n[i]
    return n

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit', nargs='+')
    args = parser.parse_args().digit
    print(func(args))

# time complesity = O(n2)
