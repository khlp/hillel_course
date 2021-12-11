input_data = raw_input()
list = list(map(int,input_data.split(' ')))
n = len(list)

def printFirstRepeating(a, n):
    for i in range(len(a)):
        if a.count(a[i]) > 1:
            return a[i]
    return "there is no repetition number"

print(printFirstRepeating(list, n))