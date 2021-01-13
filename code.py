
def eqParser(equationItself):
    listFull = []
    for i in equationItself:
        listFull.append(i)
    for i, v in enumerate(equationItself):
        if v == "+":
            before = listFull[i - 1]
            after = listFull[i + 1]
            beforeIndex = i - 1
            afterIndex = i + 1
            added = int(before) + int(after)
            listFull[beforeIndex] = ''
            listFull[afterIndex] = str(added)
        if v == "-":
            before = listFull[i - 1]
            after = listFull[i + 1]
            beforeIndex = i - 1
            afterIndex = i + 1
            subtracted = int(before) - int(after)
            listFull[beforeIndex] = ''
            listFull[afterIndex] = str(subtracted)
        if v == "*":
            before = listFull[i - 1]
            after = listFull[i + 1]
            beforeIndex = i - 1
            afterIndex = i + 1
            multiplied = int(before) * int(after)
            listFull[beforeIndex] = ''
            listFull[afterIndex] = str(multiplied)
        if v == "/":
            before = listFull[i - 1]
            after = listFull[i + 1]
            beforeIndex = i - 1
            afterIndex = i + 1
            divided = int(before) / int(after)
            listFull[beforeIndex] = ''
            listFull[afterIndex] = str(divided)
        if v == "^":
            before = listFull[i - 1]
            after = listFull[i + 1]
            beforeIndex = i - 1
            afterIndex = i + 1
            xor = int(before) ** int(after)
            listFull[beforeIndex] = ''
            listFull[afterIndex] = str(xor) 

    joinMethodForReal = ''.join(listFull)
    joinMethodForReal = joinMethodForReal.replace('+', '')
    joinMethodForReal = joinMethodForReal.replace('-', '')
    joinMethodForReal = joinMethodForReal.replace('*', '')
    joinMethodForReal = joinMethodForReal.replace('/', '')
    joinMethodForReal = joinMethodForReal.replace('^', '')
		
print(joinMethodForReal)
		
#That is the whole function that you can copy. Edit the code however you want.
#There is an example below of how you could use it to make an equation parser
		
if __name__ == "__main__":
		  while True:
			eq = input("Enter an equation to parse with eqParser:")
			eqParser(eq)
						
#All this does is make a use of eqParser by taking user input(the equation), and then parsing that equation with eqParser.
		#Thank you for copying this code if you decide to do so.
