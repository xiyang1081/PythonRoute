# -*- coding: utf-8 -*-
"""
手动遍历可迭代对象，
使用next()函数，
并捕获StopIteration异常
"""

def manual_iter():
	with open('test.txt') as f:
		try:
			while True:
				line = next(f)
				if line is None:
					break
				print(line, end='')
		except StopIteration:
			print('StopIteration!')
		finally:
			print('finally!')

def main():
	manual_iter()

if __name__ == '__main__':
	main()