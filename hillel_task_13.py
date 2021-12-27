import datetime
import string

def decorator_logger (function_to_decorate):
    def wrapp(*args, **kwargs):
        print(*args, **kwargs)
        start_time = datetime.datetime.now()
        result = function_to_decorate(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(end_time- start_time)
        return result
    return wrapp

@decorator_logger
def lucky_ticket(*args, **kwargs):
    tickets = list(range(000000, 1000000, 1))
    counter = 0
    for x in range(len(tickets)):
        st = str(x)
        st = '0' * (6 - len(st)) + st
        if int(st[0]) + int(st[1]) + int(st[2]) == int(st[3]) + int(st[4]) + int(st[5]):
            counter += 1
    print ("Count lucky tickets:", counter)
print ('First function')
lucky_ticket()

@decorator_logger
def cesar(text, shift):
    alphabet = string.printable
    new_text = ''
    for itm in text:
        if itm in text:
            char_index = alphabet.index(itm)
            new_index = (char_index + shift) % len(alphabet)
            new_text = new_text + alphabet[new_index]
        else:
            new_text = new_text + itm
    return new_text

print ('Second function')
text_to = 'Hello world'
new_value = cesar(text_to, 5)
print(new_value)