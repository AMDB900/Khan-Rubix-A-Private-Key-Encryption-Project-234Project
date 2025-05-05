class ByteCube:
    def __init__(self, size):
        self.size = size
        self.bytes = bytearray(size * size * size)

    def getBytes(self):
        return self.bytes

    def setBytes(self, _bytes):
        if len(_bytes) > len(self.bytes):
            raise ValueError("Input data is larger than cube capacity.")
        self.bytes[:len(_bytes)] = _bytes

    def getSliceXY(self, x, y):
        """Get a vertical slice along Z-axis at (x,y)."""
        idx = x + y * self.size
        return bytearray([self.bytes[idx + z * self.size * self.size] for z in range(self.size)])

    def getSliceXZ(self, x, z):
        """Get a vertical slice along Y-axis at (x,z)."""
        idx = x + z * self.size * self.size
        return bytearray([self.bytes[idx + y * self.size] for y in range(self.size)])

    def getSliceYZ(self, y, z):
        """Get a vertical slice along X-axis at (y,z)."""
        idx = y * self.size + z * self.size * self.size
        return bytearray([self.bytes[idx + x] for x in range(self.size)])

    def shiftXY(self, x, y, n):
        """Shift along Z direction at fixed (x,y)."""
        temp = self.getSliceXY(x, y)
        for i in range(self.size):
            idx = x + y * self.size + ((i + n) % self.size) * self.size * self.size
            self.bytes[idx] = temp[i]

    def shiftXZ(self, x, z, n):
        """Shift along Y direction at fixed (x,z)."""
        temp = self.getSliceXZ(x, z)
        for i in range(self.size):
            idx = x + ((i + n) % self.size) * self.size + z * self.size * self.size
            self.bytes[idx] = temp[i]

    def shiftYZ(self, y, z, n):
        """Shift along X direction at fixed (y,z)."""
        temp = self.getSliceYZ(y, z)
        for i in range(self.size):
            idx = ((i + n) % self.size) + y * self.size + z * self.size * self.size
            self.bytes[idx] = temp[i]
