'''

Programmer: Golossos@github.com

This class is a blueprint for a Number object. The prototype
accepts a binary number, and converts it to a 



'''


from power import pwr

class Number:

	def __init__(self, binary):
		
		self.binary = binary
		self.octal = 0
		self.decimal = 0
	
	def toDecimal(self):
		
		index = len(str(self.binary))-1
		for i, k in enumerate(str(self.binary)):
			if k == '1':
				self.decimal += pwr(2, index)
			index -= 1
			print i, k

	def toOctal(self):
	
		multiplier = 3		# Group bits in threes (2^3 = 8)
		loopCount = int(len(str(self.binary))/multiplier)
		string = str(self.binary)
		
		for i in range (0, loopCount):
			self.octal += i
			

	def __str__(self):
		
		s = ""
		s += "Decimal: " + str(self.decimal)
		s += "\nBinary: " + str(self.binary)
		s += "\nOctal: " + str(self.octal)

		return s

def getInt(prompt):

	result = ''	
	while (1):
		print prompt
		result = raw_input()
		try:
			result = int(result)
			break
		except:
			if (result == "q"):
				return "q"
			print "Must be an integer"

	return result
	
if __name__ == "__main__":
	
	while (1):
		decimal = getInt("Enter a binary number to be converted to decimal (enter \"q\" to quit):")
		if (decimal == "q"):
			break
		var = Number(decimal)
		var.toDecimal()
		print var


