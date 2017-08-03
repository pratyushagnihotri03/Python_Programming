from struct import *

# Store as bytes data

packed_data = pack('iif', 6, 9, 4.73)
print(packed_data)

print(calcsize('i'))  # function tells how many bits need to be stored.
print(calcsize('f'))  # function tells how many bits need to be stored.
print(calcsize('iif'))  # function tells how many bits need to be stored.

# To get bytes data back to normal
original_data  = unpack('iif', packed_data)
print(original_data)
