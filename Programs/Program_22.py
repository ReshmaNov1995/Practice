# Fibonacci series

# 0,1,1,2,3,5,8,13,21,34...
# Working
# 0,1,1
# 0,1,1,2
# 0,1,1,2,3

def fibonacci(n):
  first = 0
  second = 1
  print(first,second,end=' ') #printing initial values 0 & 1

  for i in range(2, n): # 2,3,4
      next_number = first + second # 0+1, 1+1, 1+2
      first = second # 1, 1, 2
      second = next_number # 1, 2, 3
      print(next_number,end=' ') # 1, 2, 3

n = int(input("Enter the Value of n: ")) # 5
fibonacci(n)# function call


