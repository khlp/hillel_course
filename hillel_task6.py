#Doesn't work with text value despite of using raw_input, with integer works ok (check my comments it's works correct with integer)

#dictionary2 = {'ford': [1, 3, 4, 8, 20],
#            'fiat'   : [3, 10, 15, 7, 9],
#             'renault' : [5, 3, 7, 8, 1]
#             }

ford = ['mondeo', 'focus', 'kuga']
fiat = ['tipo', 'panda', '500']
renault = ['clio', 'megan', 'duster']
dictionary = {
   'ford':   ['mondeo', 'focus', 'kuga'],
   'fiat':   ['tipo', 'panda', '500'],
   'renault':['clio', 'megan', 'duster']}

value = raw_input("Enter car model")
#value = input("Enter car model")
list_of_keys = [key
                for key, list_of_values in dictionary.items()
                #for key, list_of_values in dictionary2.items()
                if value in list_of_values]
if list_of_keys:
    print(list_of_keys)
else:
    print('Car model does not exist in the list')