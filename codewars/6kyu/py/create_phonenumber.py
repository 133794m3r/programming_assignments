def create_phone_number(n):
    b=''.join(str(x) for x in n)
    return '('+b[0:3]+')'+' '+b[3:6]+'-'+b[6:
