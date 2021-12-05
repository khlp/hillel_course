string = 'aaa bbb ccc ddd bbb rrr eee ddd bbb bbb'
new_data = 'bbb'
count=0

while string.find(new_data) != -1:
    string = string.replace(new_data,'xxx', 1)
    count = count + 1

print (string.replace('bbb','xxx'))
print count