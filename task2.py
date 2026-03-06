def check_hex_color(color):
    if len(color) != 7:
        return False
    if color[0] != "#":
        return False
    valid_chars = "0123456789abcdefABCDEF"
    for i in range(1, 7):
        if color[i] not in valid_chars:
            return False
    return True