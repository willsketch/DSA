import argparse

def count_digits(digit):
    return len(str(digit))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digit')
    args = parser.parse_args().digit
    print(count_digits(args))
## time complexity --> O(1)
