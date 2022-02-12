def swap_case(s):
    Str=""
    for a in s:
        if(a.isupper()):
            Str+=a.lower()
        else:
            Str+=a.upper()
    return Str

s = input()
result = swap_case(s)
print(result)