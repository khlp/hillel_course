input_data = [(1,'cm'), (2,'ft'), (4,'inch'), (0.5, 'sm')]

def Conversion(measure_obj):
    types = measure_obj[1]
    meters = measure_obj[0]
    result = 0
    if types == 'cm':
        result = f'{meters*100} cm'
    elif types == 'ft':
        result = f'{meters*3.28} ft'
    elif types == 'inch':
        result = f'{meters*39.37} inch'
    elif types == 'sm':
        result = f'{round(((meters*3.28)/6),2)} sm'
    return result

result = map(Conversion,filter(lambda itm_in: True if itm_in[0]>=1 else False,input_data))
for itm in result:
    print(itm)