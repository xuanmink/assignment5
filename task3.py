def sum_numbers(text):
    total = 0
    current_num = ""
    for char in text:
        if char.isdigit():
            current_num = current_num +char
        else:
            if current_num != "":
                total = total + int(current_num)
                current_num = ""
    if current_num != "":
        total = total + int(current_num)
    return total