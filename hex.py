'''

This class is a blueprint for a Binary number object. The prototype
accepts a binary number, and converts it to a 



'''


from power import pwr

class Number:

	def __init__(self, binary):
		
		self.binary = binary
		self.octal = 0
		self.decimal = 0
		self.hex = "0"
	
	def toDecimal(self):
		
		index = len(str(self.binary))-1
		for i, k in enumerate(str(self.binary)):
			if k == '1':
				self.decimal += pwr(2, index)
			index -= 1
			print i, k
	
	def toDecimalSegment(self, seg):
		
		index = len(str(seg))-1
		result = 0
		for i, k in enumerate(str(seg)):
			if k == '1':
				result += pwr(2, index)
			index -= 1
		
		return result

	def toOctal(self):
	
		multiplier = 3		# Group bits in threes (2^3 = 8)
		loopCount = int(len(str(self.binary))/multiplier)
		string = str(self.binary)
		
		for i in range (0, loopCount):
			self.octal += i
			
	def toHexSegment(self, seg):
		
		decTest = self.toDecimalSegment(seg)
		print "Hex segment to be tested: " + str(decTest)
		if decTest == 10:
			return "A"
		elif decTest == 11:
			return "B"
		elif decTest == 12:
			return "C"
		elif decTest == 13:
			return "D"
		elif decTest == 14:
			return "E"
		elif decTest == 15:
			return "F"
		else:
			return decTest
	def toHex(self):
		
		string = str(self.binary)
		if len(string) % 4 == 3:
			string = "0" + string
		elif len(string) % 4 == 2:
			string = "00" + string
		elif len(string) % 4 == 1:
			string = "000" + string

		print "Formatted hex string: " + string
		arrCount = len(string) / 4
		hexArr = [None] * arrCount
		for i in range (0, len(string), 4):
			sub = string[i:i+4]
			hexSeg = self.toHexSegment(int(sub))
			self.hex += str(hexSeg)
			
			print sub
		
			

	def __str__(self):
		
		s = ""
		s += "Decimal: " + str(self.decimal)
		s += "\nBinary: " + str(self.binary)
		s += "\nOctal: " + str(self.octal)
		s += "\nHex: " + str(self.hex)
		return s

def getInt(prompt):

	result = ""	
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
#		var.toDecimal()
		var.toHex()
		print var


