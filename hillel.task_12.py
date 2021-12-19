import datetime

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

def timer(func, *args, **kwargs):
    t1 = datetime.datetime.now()
    value=func(*args, **kwargs)
    t2 = datetime.datetime.now()
    print(t2-t1)
    return value

timer(Conversion,2)