#file name & data
filename = "a.bin"
data = 100

#write
with open(filename,"wb") as f:
    f.write(bytearray([data]))