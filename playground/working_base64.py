# print('💝')
# print('\U0001F49D')
# print('ї'.encode())


# 00101010000000000000000000000000000000000000001011101101010111
#
# 01011010 01011101 01011101
# 010110 100101 110101 011101
# hjhd
# 01011010 01011101 01011101 01011101
#
import base64

encoded = base64.b64encode(b"hello")
print(encoded)
decoded = base64.b64decode(encoded)
print(decoded)
