#The program checks if the ticket is lucky or not, but how to calculate count of lucky tickets within a given range I don't know
def isLucky(n):
    arr = [int(x) for x in str(n)]
    middle = int(len(arr) / 2)

    return sum(arr[0:middle]) == sum(arr[middle:])

print(isLucky(160700))
