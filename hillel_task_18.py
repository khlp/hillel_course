class Temperature:
    dict = {'K': 273.15, 'F': 5 / 9, 'C': 1}

    def __init__(self, input_temp, measure):
        self.Kc = input_temp + Temperature.dict[measure]
        self.Kf = Temperature.kelvin_to_fahrenheit(input_temp, measure)
        self.Fc = Temperature.celsius_to_fahrenheit(input_temp, measure)
        self.Fk = Temperature.kelvin_to_fahrenheit(input_temp, measure)
        self.Ck = Temperature.celsius_to_kelvin(input_temp, measure)
        self.Cf = Temperature.celsius_to_fahrenheit(input_temp, measure)

    @staticmethod
    def kelvin_to_celsius(my_temp, measure):
        k_to_c = (my_temp - Temperature.dict['K']) * Temperature.dict[measure]
        return k_to_c

    @staticmethod
    def kelvin_to_fahrenheit(my_temp, measure):
        k_to_f = (my_temp - Temperature.dict['K']) * (Temperature.dict[measure] ** (-1)) + 32
        return k_to_f

    @staticmethod
    def celsius_to_kelvin(my_temp, measure):
        c_to_k = my_temp + Temperature.dict[measure]
        return c_to_k

    @staticmethod
    def celsius_to_fahrenheit(my_temp, measure):
        c_to_f = (my_temp * (Temperature.dict[measure] ** (-1))) + 32
        return c_to_f

    @staticmethod
    def fahrenheit_to_kelvin(my_temp, measure):
        f_to_k = (my_temp - 32) * Temperature.dict['F'] + Temperature.dict[measure]
        return f_to_k

    @staticmethod
    def fahrenheit_to_celsius(my_temp, measure):
        f_to_c = ((my_temp - 32) * Temperature.dict['F']) * Temperature.dict[measure]
        return f_to_c

    def __gt__(self, additional):
        if self.celsius_to_fahrenheit > additional.celsius_to_fahrenheit or \
                self.celsius_to_kelvin > additional.celsius_to_kelvin or \
                self.kelvin_to_fahrenheit > additional.kelvin_to_fahrenheit or \
                self.kelvin_to_celsius > additional.kelvin_to_celsius or \
                self.fahrenheit_to_celsius > additional.fahrenheit_to_celsius or \
                self.fahrenheit_to_kelvin > additional.fahrenheit_to_kelvin:
            return True
        else:
            return False

    def __lt__(self, additional):
        if self.celsius_to_fahrenheit < additional.celsius_to_fahrenheit or \
                self.celsius_to_kelvin < additional.celsius_to_kelvin or \
                self.kelvin_to_fahrenheit < additional.kelvin_to_fahrenheit or \
                self.kelvin_to_celsius < additional.kelvin_to_celsius or \
                self.fahrenheit_to_celsius < additional.fahrenheit_to_celsius or \
                self.fahrenheit_to_kelvin < additional.fahrenheit_to_kelvin:
            return True
        else:
            return False

    def __le__(self, additional):
        if self.celsius_to_fahrenheit <= additional.celsius_to_fahrenheit or \
                self.celsius_to_kelvin <= additional.celsius_to_kelvin or \
                self.kelvin_to_fahrenheit <= additional.kelvin_to_fahrenheit or \
                self.kelvin_to_celsius <= additional.kelvin_to_celsius or \
                self.fahrenheit_to_celsius <= additional.fahrenheit_to_celsius or \
                self.fahrenheit_to_kelvin <= additional.fahrenheit_to_kelvin:
            return True
        else:
            return False

    def __ge__(self, additional):
        if self.celsius_to_fahrenheit >= additional.celsius_to_fahrenheit or \
                self.celsius_to_kelvin >= additional.celsius_to_kelvin or \
                self.kelvin_to_fahrenheit >= additional.kelvin_to_fahrenheit or \
                self.kelvin_to_celsius >= additional.kelvin_to_celsius or \
                self.fahrenheit_to_celsius >= additional.fahrenheit_to_celsius or \
                self.fahrenheit_to_kelvin >= additional.fahrenheit_to_kelvin:
            return True
        else:
            return False

    def __eq__(self, additional):
        if self.celsius_to_fahrenheit == additional.celsius_to_fahrenheit or \
                self.celsius_to_kelvin == additional.celsius_to_kelvin or \
                self.kelvin_to_fahrenheit == additional.kelvin_to_fahrenheit or \
                self.kelvin_to_celsius == additional.kelvin_to_celsius or \
                self.fahrenheit_to_celsius == additional.fahrenheit_to_celsius or \
                self.fahrenheit_to_kelvin == additional.fahrenheit_to_kelvin:
            return True
        else:
            return False

    def __add__(self, additional):
        return Temperature(self.celsius_to_fahrenheit + additional.celsius_to_fahrenheit or
                           self.celsius_to_kelvin + additional.celsius_to_kelvin or
                           self.kelvin_to_fahrenheit + additional.kelvin_to_fahrenheit or
                           self.kelvin_to_celsius + additional.kelvin_to_celsius or
                           self.fahrenheit_to_celsius + additional.fahrenheit_to_celsius or
                           self.fahrenheit_to_kelvin + additional.fahrenheit_to_kelvin)

    def __sub__(self, additional):
        return Temperature(self.celsius_to_fahrenheit - additional.celsius_to_fahrenheit or
                           self.celsius_to_kelvin - additional.celsius_to_kelvin or
                           self.kelvin_to_fahrenheit - additional.kelvin_to_fahrenheit or
                           self.kelvin_to_celsius - additional.kelvin_to_celsius or
                           self.fahrenheit_to_celsius - additional.fahrenheit_to_celsius or
                           self.fahrenheit_to_kelvin - additional.fahrenheit_to_kelvin)

print(Temperature.celsius_to_fahrenheit(20, 'F'))
print(Temperature.celsius_to_kelvin(20, 'K'))

print(Temperature.kelvin_to_fahrenheit(20, 'F'))
print(Temperature.kelvin_to_celsius(20, 'C'))

print(Temperature.fahrenheit_to_kelvin(20, 'K'))
print(Temperature.fahrenheit_to_celsius(20, 'C'))
print('First:')
temp_1 = (Temperature.fahrenheit_to_kelvin(20, 'K'))
temp_2 = (Temperature.fahrenheit_to_kelvin(10, 'K'))
print(temp_2 < temp_1)
print(temp_2 >= temp_1)
print(temp_2 + temp_1)

print('Second:')
temp_3 = (Temperature.kelvin_to_celsius(20, 'C'))
temp_4 = (Temperature.kelvin_to_celsius(10, 'C'))
print(Temperature.kelvin_to_celsius(20, 'C'))
print(Temperature.kelvin_to_celsius(10, 'C'))
print(temp_3 < temp_4)
print(temp_3 >= temp_4)
print(temp_3 + temp_4)