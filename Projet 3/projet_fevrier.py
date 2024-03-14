import binascii
import uu

print(bin(int.from_bytes('hello'.encode(), 'big')))


print(bytes("11101001", "ascii"))

n = int('0b01001111', 2)
print(n)
print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())