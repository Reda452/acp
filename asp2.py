def find_fiste_set_bit(n):
    if n == 0:
        return -1  # no set bit in 0
    position = 0
    while = (n & 1) == 0:
        n >>= 1
        position += 1
    return position

#example usage:
number = 8  #binary representation is 10010
first_set_bit = find_first_set_bit(number)
print (f"first set bit position: {first_set_bit_position}")