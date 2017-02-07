

def prime_numbers(n):
   """
   A function that returns prime numbers in range
   0 to n
   """
   if not isinstance(n, int):
       raise TypeError
   
   if n < 2:
       raise ValueError

   prime_numbers = []
   for num in range(2, n):
       if is_prime(num):
           prime_numbers.append(num)
  
   return prime_numbers

def is_prime(num):
   """
   Return true if a number is a 
   prime number
   """
   for i in range(2, num-1):
       if num % i == 0:
           return False

   return True
