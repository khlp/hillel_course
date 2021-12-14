def Conversion(meters, type = 'cm'):
    if type == 'cm':
        result = f'{meters*100} cm'
    elif type == 'ft':
        result = f'{meters*3.28} ft'
    elif type == 'inch':
        result = f'{meters*39.37} inch'
    elif type == 'fathom':
        result = f'{round(((meters*3.28)/6),2)} fathom'
    return result

print(Conversion(1))
print(Conversion(1, 'ft'))
print(Conversion(1, 'inch'))
print(Conversion(1, 'fathom'))