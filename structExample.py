'''Implement struct pack-unpack function
to convert data to and from byte format'''
from struct import *

#store as bytes data
packet_data = pack('iif', 6,19,4.75)
print (packet_data)

#It shows the size an integer/float and packet_data holds
print(calcsize('i'))
print(calcsize('iif'))

#use unpack to get data to human readable format
original_data = unpack('iif',packet_data)
print (original_data)

