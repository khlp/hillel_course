import re
number = '+380(63)-3329804'
correct_number = re.sub("[^0-9]",'',number)
result = re.match(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$', correct_number)
print(bool(result))