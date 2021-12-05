#заменить в строке искомое слово на слово-замену и вывески колличество замен
string = 'aaa bbb ccc ddd bbb rrr eee ddd bbb'
new_data = 'bbb'
count=0

while string.find(new_data) != -1:
    string = string.replace(new_data,'xxx', 1)
    count = count + 1

print (string.replace('bbb','xxx'))
print count