# how i'm about to ace cms 270

def dec_bin(dec: str) -> bin:
    return bin(int(dec))


def dec_hex(dec: str) -> hex:
    return hex(int(dec))


def dec_oct(dec: str) -> oct:
    return oct(int(dec))


def bin_dec(input_bin: str) -> int:
    dec = 0
    exponent = 0
    for i in range(len(bin) - 1, -1, -1):
        x = int(bin[i])
        if x == 0 or x == 1:
            dec += x * pow(2, exponent)
            exponent += 1
    return dec


def bin_hex(input_bin: str) -> hex:
    pass


def bin_oct(input_bin: str) -> oct:
    pass


def hex_dec(input_hex: str) -> int:
    pass


def hex_bin(input_hex: str) -> bin:
    pass


def hex_oct(input_hex: str) -> oct:
    pass


def oct_dec(input_oct: str) -> int:
    pass


def oct_bin(input_oct: str) -> bin:
    pass


def oct_hex(input_oct: str) -> hex:
    pass


def ascii_dec(input_ascii: str) -> int:
    pass


def dec_ascii(dec: str) -> str:
    pass
