def two():
	fib_one = 1
	fib_two = 2
	ret = fib_one + fib_two
	while fib_two < 4000000:
		holder = fib_one
		fib_one = fib_two
		fib_two += holder
		ret += fib_two
	return ret

if __name__ == '__main__':
	ans = two()
	print ans