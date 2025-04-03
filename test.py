def sas_packed_decimal(num: str) -> str:
    """
    Converts a numeric string to SAS $HX16. Packed Decimal (BCD) format.
    """
    # Ensure input is a string and pad to an even length
    num = str(num)
    if len(num) % 2 != 0:
        num = "0" + num  # Ensure even number of digits

    packed_bytes = bytearray()

    # Convert two digits at a time into a single packed byte
    for i in range(0, len(num) - 1, 2):
        packed_byte = (int(num[i]) << 4) + int(num[i + 1])
        packed_bytes.append(packed_byte)

    # Handle the last digit with the sign nibble (C for positive, D for negative)
    last_digit = int(num[-1]) | 0xC0  # 0xC0 for positive, 0xD0 for negative
    packed_bytes.append(last_digit)

    return packed_bytes.hex().upper()


# Test case
liabnum = "11267834931775462689"
hex_result = sas_packed_decimal(liabnum)

print(hex_result)  # Expected Output: "F9C3F5C6F6F4F2C2"
