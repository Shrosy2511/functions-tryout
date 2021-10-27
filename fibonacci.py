def myFunction(num):
	a, b = 1, 1
	for c in range(num - 1):
		a, b = b, a + b
	return a

print(myFunction(6))
