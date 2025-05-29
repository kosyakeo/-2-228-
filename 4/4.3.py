def calculate_(a, b, code):
    match code:
        case 1:
            return a+b
        case 2:
            return a-b
        case 3:
            return a*b
        case 4:
            return a/b

print(calculate_(2,3,3))