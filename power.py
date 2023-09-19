

def pwr(n, p):
	
	result = 1
	for i in range(0,p):
		result *= n

	return result

if __name__ == "__main__":
	print (pwr(2,2))
