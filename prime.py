def is_prime(a):
	return all(a % x for x in range(2, a//2 + 1))

def is_prime(num):
	remainders = (num % x for x in range(2, num // 2 + 1))
	return all(remainders)

def primesums(x):
	for z in reversed(range(1, x//2 + 1)):
		if prime(z) and prime(x-z):
			yield (z, x-z)

def primesums(x):
	return ((z, x-z) for z in reversed(range(1, x//2+1)) if prime(z) and prime(x-z))

def primesums(num):
	midpoint = num // 2 + 1
	possibles = reversed(range(1, midpoint))
	return ((z, num - z) for z in possibles if prime(z) and prime(num - z))

def is_prime(a):
	if all(a%i for i in range(w, a//2+1)):
		return True
	else:
		return False

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
			if is_prime(z) and is_prime(x-z):
				print('The two primes are {0} and {1}'.format(z, x-z))
		print('Function done')
