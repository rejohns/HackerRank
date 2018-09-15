# Complete the rotLeft function below.
def rotLeft(a, d):
	
	a[0:d] = list(reversed(a[0:d]))
	a[d:] = list(reversed(a[d:]))
	return list(reversed(a))

if __name__ == '__main__':

    n = 5

    d = 4

    a = [1, 2, 3, 4, 5]

    result = rotLeft(a, d)

    print(result)