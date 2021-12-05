#First variant calculator
list = []
list_element = ''
while list_element != '=':
    list_element = raw_input()
    if list_element == '=':
        break
    list = list + [list_element]
print(list)

current_operator = '+'
result = 0
for element in list:
    if element.isdigit():
        element=int(element)
        if current_operator == '+':
            result = result + element
        elif current_operator == '-':
            result = result - element
        elif current_operator == '*':
            result = result * element
        else:
            result = result / element
    else :
        current_operator = element

print(result)


#Second variant - Works with unlimited count of numbers but only 1 operator
def calculator():
    total = 0

    while True:
        number = raw_input('enter a number: ')
        if number == 'finish':
            break
        try:
            total += float(number)
        except ValueError:
            continue
    print 'the total is', total

calculator()