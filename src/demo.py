#! /usr/bin/python3

from woma_demo import womain

if __name__ == '__main__':
    args = ['foo', 'bar', 'baz']
    print(womain('woo', args))
    print(womain(1, args))
    print(womain(0.01, args))
    