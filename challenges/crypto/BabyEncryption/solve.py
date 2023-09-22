def string_to_2d_array(s):
    if len(s) % 2 != 0:
        return "String length must be even to create pairs."
    return [[s[i:i+2]] for i in range(0, len(s), 2)]

def char_to_encrypted_hex(ascii_val):
    encrypted_val = (123 * ascii_val + 18) % 256
    encrypted_hex = bytes([encrypted_val]).hex()
    return encrypted_hex

def find_positions_in_2d_array(value, array_2d):
    return [(row_index, col_index) for row_index, sublist in enumerate(array_2d) for col_index, item in enumerate(sublist) if item == value]

def print_values(array_2d):
    for sublist in array_2d:
        print(sublist[0], end='')

cypher = "aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
cypher_arr = string_to_2d_array(cypher)

for i in range(256):
    hex_val = char_to_encrypted_hex(i)
    positions = find_positions_in_2d_array(hex_val, cypher_arr)
    for position in positions:
        row, col = position
        cypher_arr[row][col] = chr(i)

print_values(cypher_arr)