#First variant - The program count lucky tickets
counter = 0
for ticket in range (0,1000000):
    num6 = ticket % 10
    tmp = ticket // 10

    num5 = tmp % 10
    tmp = tmp //10

    num4 = tmp % 10
    tmp = tmp // 10

    num3 = tmp % 10
    tmp = tmp // 10

    num2 = tmp % 10
    tmp = tmp // 10

    num1 = tmp % 10
    tmp = tmp // 10

    if num1+num2+num3==num4+num5+num6:
        counter= counter +1

print (counter)

#Second variant - The program checks if the ticket is lucky or not
def isLucky(n):
    arr = [int(x) for x in str(n)]
    middle = int(len(arr) / 2)

    return sum(arr[0:middle]) == sum(arr[middle:])

print(isLucky(160700))