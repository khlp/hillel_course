#Works with unlimited count of numbers but only 1 operator
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