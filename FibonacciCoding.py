#fibonacci numbers starting from 1,2
fibonacciNum = [1,2]

#get or calculate the nth fibonacci number
def getFibonacciNum(n):
	while(len(fibonacciNum)<=n):
		fibonacciNum.append(-1)
	if(fibonacciNum[n]==-1):
		fibonacciNum[n] = getFibonacciNum(n-1) + getFibonacciNum(n-2)
	return fibonacciNum[n]

#generate a fibonacci code for an interger n
def getFibonacciCode(n):
	codeLength = 0;
	#calculate the length of the code
	#find the first fibonacci number greater than n
	while getFibonacciNum(codeLength) <= n:
		codeLength = codeLength + 1
	#get the fibonacci number before that one
	codeLength = codeLength - 1
	#end code
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
	
if __name__ == "__main__":
	for i in range(10, 0 ,-1):
		print(getFibonacciNum(i))
	
	for i in range(1,100):
		print(""+str(i)+": "+getFibonacciCode(i))
