def recursion_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursion_fibonacci(n-1) + recursion_fibonacci(n-2))

nterms = int(input("How many terms? "))

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recursion_fibonacci(i))