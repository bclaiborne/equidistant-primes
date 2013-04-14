def is_prime(a):
	for i in range(2, a//2 + 1):
#		print(a, i, a%i)
		if not a%i:
			return False
	return True

if __name__ == "__main__":
	while True:
		x = int(input('Enter any integer greater than 1: '))

		for z in reversed(range(1, x//2 +1)):
#			print(z, x-z, type(z), type(x-z))
			if is_prime(z) and is_prime(x-z):
				print('The two primes are {0} and {1}'.format(z, x-z))
		print('Function done')
