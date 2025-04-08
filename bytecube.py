
class ByteCube:
	def __init__(self, size):
		self.size = size
		self.bytes = bytearray(0 for n in range(self.size * self.size * self.size))
	
	def getBytes(self):
		return self.bytes
	
	def getSliceXY(self, x, y):
		return bytearray([(self.bytes[x + y * self.size + z * self.size * self.size]) for z in range(self.size)])
	
	def getSliceXZ(self, x, z):
		return bytearray([(self.bytes[x + y * self.size + z * self.size * self.size]) for y in range(self.size)])
		
	def getSliceYZ(self, y, z):
		return bytearray([(self.bytes[x + y * self.size + z * self.size * self.size]) for x in range(self.size)])
	
	


if __name__ == "__main__":

	size = 3
	byte_cube = ByteCube(size)
	print(byte_cube.bytes)
	#print(len(byte_cube))
	#for n in range(len(byte_cube)):
	#	print(byte_cube[n])

	x = 0
	y = 0
	print(byte_cube.getSliceXY(x,y))

	y = 0
	z = 0
	print(byte_cube.getSliceYZ(y,z))


	#y=2
	#z=2
	#temparray = [(byte_cube[x + y * size + z * size * size]) for x in range(size)]
	#shift = -1
	#print([(byte_cube[x + y * size + z * size * size]) for x in range(size)])

	#for n in range(size):
	#	byte_cube[(n+shift)%size + y * size + z * size * size] = temparray[n]

	#print(byte_cube)
	#print([(byte_cube[x + y * size + z * size * size]) for x in range(size)])


	
