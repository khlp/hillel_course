dictionary2 = {'ford': ['mondeo', 'focus', 'kuga'],
            'fiat'  : ['tipo', 'panda','500'],
             'renault' : ['clio', 'megan', 'duster']
             }
while True:
    value = raw_input('Enter car model: ')
    if value == 'exit':
        break
    list_of_keys = [key
                    for key, list_of_values in dictionary2.items()
                    if value in list_of_values]
    if list_of_keys:
        print(list_of_keys)
    else:
        print('Car model does not exist in the list')