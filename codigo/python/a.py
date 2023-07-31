import struct
import sys

buffer = bytearray(1024)

var1 = 1
var2 = 2
var3 = 3


format = ">ddd"

vars = [var1, var2, var3]

msg = struct.pack(format, *vars)

with open("telemetria.bin", "ab") as f:
    f.write(msg)
    f.write(msg)
    f.write(msg)

with open("telemetria.bin", "rb") as f:
    while (chunk := f.read(struct.calcsize(format))):
        print(struct.unpack(format, chunk))

print(sys.getsizeof(buffer))
