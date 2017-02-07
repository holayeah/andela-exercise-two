

def prime_numbers(end, start=2):
   """
   A function that returns prime numbers in range
   start and end
   """
   if not(isinstance(end, int) and isinstance(start, int)): # halt if one of start and end is not integer
       raise TypeError
   
   if end < 2:
       raise ValueError

   if start > end:
       raise ValueError("Starting point can not be greater than ending point")
       

   prime_numbers = []
   for num in range(start, end):
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
