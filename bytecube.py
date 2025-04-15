import copy


class ByteCube:
	def __init__(self, size):
		self.size = size
		self.bytes = bytearray(0 for n in range(self.size * self.size * self.size))
	
	def getBytes(self):
		return self.bytes
	
	def setBytes(self, _bytes):
		self.bytes[0:len(_bytes)] = _bytes
	
	def getSliceXY(self, x, y):
		return bytearray([(self.bytes[x + y * self.size + z * self.size * self.size]) for z in range(self.size)])
	
	def getSliceXZ(self, x, z):
		return bytearray([(self.bytes[x + y * self.size + z * self.size * self.size]) for y in range(self.size)])
		
	def getSliceYZ(self, y, z):
		return bytearray([(self.bytes[x + y * self.size + z * self.size * self.size]) for x in range(self.size)])
	
	def shiftXY(self, x, y, n):
		temparray = self.getSliceXY(x,y)
		for i in range(self.size):
			self.bytes[x + y * self.size + ((i+n)%self.size) * self.size * self.size] = temparray[i]
	
	def shiftXZ(self, x, z, n):
		temparray = self.getSliceXZ(x,z)
		for i in range(self.size):
			self.bytes[x + ((i+n)%self.size) * self.size + z * self.size * self.size] = temparray[i]

	def shiftYZ(self, y, z, n):
		temparray = self.getSliceYZ(y,z)
		for i in range(self.size):
			self.bytes[((i+n)%self.size) + y * self.size + z * self.size * self.size] = temparray[i]
	


if __name__ == "__main__":

	size = 3
	byte_cube = ByteCube(size)
	print(byte_cube.bytes)
	#print(len(byte_cube))
	#for n in range(len(byte_cube)):
	#	print(byte_cube[n])
	
	byte_cube.setBytes([3,2,1,6,5,4,9,8,7,12,11,10,15,14,13,18,17,16,21,20,19,24,23,22,27,26,25])

	x = 0
	y = 0

	print(byte_cube.bytes)	
	
	print(byte_cube.getSliceXY(x,y))
	
	byte_cube.shiftXY(x,y,1)
	
	print(byte_cube.bytes)
	
	print(byte_cube.getSliceXY(x,y))
	
	byte_cube.shiftXY(x,y,-1)
	
	print(byte_cube.bytes)
	
	print(byte_cube.getSliceXY(x,y))

	y = 0
	z = 0
	
	print(byte_cube.getSliceXZ(x,z))
	
	byte_cube.shiftXZ(x,z,1)
	
	print(byte_cube.bytes)
	
	print(byte_cube.getSliceXZ(x,z))
	
	print(byte_cube.getSliceYZ(y,z))
	
	byte_cube.shiftYZ(y,z,1)
	
	print(byte_cube.bytes)
	
	print(byte_cube.getSliceYZ(y,z))
	#print(byte_cube.getSliceYZ(y,z))
	


	#y=2
	#z=2
	#temparray = [(byte_cube[x + y * size + z * size * size]) for x in range(size)]
	#shift = -1
	#print([(byte_cube[x + y * size + z * size * size]) for x in range(size)])

	#for n in range(size):
	#	byte_cube[(n+shift)%size + y * size + z * size * size] = temparray[n]

	#print(byte_cube)
	#print([(byte_cube[x + y * size + z * size * size]) for x in range(size)])


	
