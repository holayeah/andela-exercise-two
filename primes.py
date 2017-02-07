

def prime_numbers(end, start=2):
   """
   A function that returns prime numbers in range
   start and end
   """
   if not(isinstance(end, int) and isinstance(start, int)): # halt if one of start and end is not integer
       raise TypeError
   
   if end < 2 or start < 2:
       raise ValueError

   if start >= end:
       raise ValueError("Starting point can not be greater or equal ot the ending point")
       

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


"""
Asymptotic analysis,
Basing tat the prime_numbes function checks for every value in the range 
and that the function in is_prime number checks that n can not be divible by any number less than it.

We can say that for a number n it takes approximately n^2 operation to get the result.

The result is that prime_numbers is (0)n^2
"""
