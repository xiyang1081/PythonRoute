# -*- coding: utf-8 -*-
"""
使用生成器创建新的迭代模式
""" 

def frange(start, end, ement):
    x = start
    while x < end:
        yield x
        x += ement

def main():
    tmp = list(frange(1, 10, 0.2))
    print(tmp)

    for i in frange(0, 5, 0.5):
        print(i)

if __name__ == '__main__':
    main()