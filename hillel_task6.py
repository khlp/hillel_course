#Doesn't work with text value, despite of using raw_input,
# with integer works ok

dictionary2 = {'ford': [1, 3, 4, 8, 20],
            'fiat'  : [3, 10, 15, 7, 9],
             'renault' : [5, 3, 7, 8, 1]
             }
while True:
    value = input('Enter car model: ')
    if value == 0:
        break
    list_of_keys = [key
                    for key, list_of_values in dictionary2.items()
                    if value in list_of_values]
    if list_of_keys:
        print(list_of_keys)
    else:
        print('Car model does not exist in the list')