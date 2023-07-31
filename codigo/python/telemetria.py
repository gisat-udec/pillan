import struct
import time

filename = "telemetria.bin"
chunk_format = ">dd"
chunks = 100

chunk_size = struct.calcsize(chunk_format)
array = bytearray(chunk_size * chunks)
buffer = memoryview(array)
buffer_size = len(buffer)
	
c = 0
while True:
	buffer[c:c+chunk_size] = struct.pack(chunk_format, 1, 2)
	c = c + chunk_size
	if c >= buffer_size:
		with open(filename, "ab") as f:
			f.write(buffer)
		c = 0