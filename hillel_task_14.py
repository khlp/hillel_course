a = input("Input a number: ")
b = input("Input another number: ")

def devisor(a, b):
    if (b == 0):
        return a
    else:
        return devisor(b, a % b)

print(devisor(a, b))