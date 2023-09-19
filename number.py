'''

This class is a blueprint for a Binary number object. The prototype
accepts a binary number, and converts it to a 



'''


from power import pwr

class Number:

    # Default constructor
    def __init__(self, binary):
        
        self.binary = binary
        self.octal = '0'
        self.decimal = 0
        self.hex = "0"
    
    # Accepts a binary string; convert it to decimal
    def toDecimal(self):
        index = len(str(self.binary))-1
        for arrIndex, arrItem in enumerate(str(self.binary)):
            if str(self.binary)[index] == '1':
                self.decimal += pwr(2, arrIndex)
            index -= 1
        return self.decimal
    
    # Accepts a segment of a binary string and converts the segment to decimal to be formatted to the
    # returned number system's string
    def toDecimalSegment(self, seg):
        
        index = len(str(seg))-1
        result = 0
        for i, k in enumerate(str(seg)):
            if k == '1':
                result += pwr(2, index)
            index -= 1
        
        return result

    # Converts the Number's binary string to its octal counterpart
    def toOctal(self):
        result = '' 
        multiplier = 3      # Group bits in threes (2^3 = 8)
        string = str(self.binary)
        if len(string) % 3 == 2:
            string = "0" + string
        elif len(string) % 3 == 1:
            string = "00" + string
        index = len(string)-1
        print('The octal with padding: ' + string)
        stack = list()
        while index > 0:
            octalSeg = string[index-2:index+1]
            print('start index: ' + str(index-2))
            print('end index: ' + str(index))
            decimalSeg = str(self.toDecimalSegment(octalSeg))
            print('segment: ' + octalSeg)
            stack.append(decimalSeg)
            index -= 3
        while (stack):
            item = stack.pop()
            print('The popped item: ' + item)
            self.octal += item
        return self.octal
            
    # Unique segment convert method; accept 4-digit binary string and convert it to the hex
    # counterpart
    def toHexSegment(self, seg):
        
        decTest = self.toDecimalSegment(seg)
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

    # Convert a binary string to a hexadecimal number, format it with leading zeroes for parsing as necessary
    def toHex(self):
        
        string = str(self.binary)
        if len(string) % 4 == 3:
            string = "0" + string
        elif len(string) % 4 == 2:
            string = "00" + string
        elif len(string) % 4 == 1:
            string = "000" + string

        for i in range (0, len(string), 4):
            sub = string[i:i+4]
            hexSeg = self.toHexSegment(int(sub))
            self.hex += str(hexSeg)
            
        
    # Represent the Number as a String
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
        print (prompt)
        result = input()
        try:
            result = int(result)
            break
        except:
            if (result == "q"):
                return "q"
            print ("Must be an integer")

    return result
    
if __name__ == "__main__":
    
    while (1):
        decimal = getInt("Enter a binary number to be converted to decimal (enter \"q\" to quit):")
        if (decimal == "q"):
            break
        var = Number(decimal)
        var.toDecimal()
        var.toHex()
        var.toOctal()
        print(var)


