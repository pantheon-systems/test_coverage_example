def fib(n):
	seq = []
	a,b = 0,1
	for i in range(n):
		a,b = b,a+b
		seq.append(a)
	return seq