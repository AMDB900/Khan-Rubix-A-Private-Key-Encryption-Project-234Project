import re

#fibonacci numbers starting from 1,2
fibonacciNum = [1,2]

#get or calculate the nth fibonacci number
def getFibonacciNum(n):
	'''
	returns the nth fibonacci number
	Args: n: integer to get fibonacci number for
	Returns: the nth fibonacci number
	'''
	while(len(fibonacciNum)<=n):
		fibonacciNum.append(-1)
	if(fibonacciNum[n]==-1):
		fibonacciNum[n] = getFibonacciNum(n-1) + getFibonacciNum(n-2)
	return fibonacciNum[n]

#generate a fibonacci code for an interger n
def getFibonacciCode(n):
	'''
	generates a fibonacci code for an integer n
	Args: n: integer to be encoded
	Returns: a string with the fibonacci code for n
	'''
	codeLength = 0;
	#calculate the length of the code
	#find the first fibonacci number greater than n
	while getFibonacciNum(codeLength) <= n:
		codeLength = codeLength + 1
	#get the fibonacci number before that one
	codeLength = codeLength - 1
	#start with end code
	output = "1"
	#start from the largest number less than n
	for i in range(codeLength, -1, -1):
		#if it's less than or equal to n
		if getFibonacciNum(i)<=n:
			#subtract it from n
			n = n - getFibonacciNum(i)
			#prepend a 1
			output = "1" + output
		#if it's greater than n
		else:
			#prepend a 0
			output = "0" + output
	return output

#calculate integer value from fibonacci code fibonacci
def decodeFibonacciCode(f):
	'''
	decodes a fibonacci code into an integer
	
	Returns: integer value of fibonacci code
	'''
	assert(f[-2:]) == "11"
	return sum([getFibonacciNum(i) for i in range(len(f)-1) if f[i]=="1"])

#get the length of string s and prepend fibonacci code of length	
def fibonacciEncodeLength(s):
	'''
	Returns: a string with the length of s encoded in fibonacci code
	'''
	return getFibonacciCode(len(s)) + s
	
#read fibonacci coded length from the start of string s and shorten the string to that length
def fibonacciUnpad(s):
	'''
	Returns: a string with the length of s encoded in fibonacci code
	'''
	m = re.match(r'(0|10)*11', s)
	return m.string[m.end(0):m.end(0)+decodeFibonacciCode(m[0])]
	
if __name__ == "__main__":
	#for i in range(10, 0 ,-1):
	#	print(getFibonacciNum(i))
	
	#for i in range(1,100):
	#i=100
	if(True):
		string = "CHECK THIS OUT"
		#fcode = getFibonacciCode(len(string))
		
		encodedString = fibonacciEncodeLength(string) + "PADDING"
		print(encodedString)
		#print(decodeFibonacciCode(fcode))
		#splitTest = "" + fcode + str(i)
		#m = re.match(r'(0|10)*11', encodedString)
		#print(m.string[m.end(0):m.end(0)+decodeFibonacciCode(m[0])])
		decodedString = fibonacciUnpad(encodedString)
		print(decodedString)
		
