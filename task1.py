def check_course_code(code):
    if len(code) == 5:
        if code[0].isupper() and code[1].isupper() and code[2].isdigit() and code[3].isdigit()and code[4].isdigit():
            return True
        else:
            return False
    elif len(code) == 6:
        if code[0].isupper() and code[1].isupper() and code[2].isupper()and code[3].isdigit() and code[4].isdigit() and code[5].isdigit():
            return True
        else:
            return False
    else:
        return False