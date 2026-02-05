# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
# x = 10 / 0 

# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
# try:
#   x = 10 / 0
# except:
#   print("Well that didn't work")

# You can also catch specific exceptions
try:
  answer = input('What to divide by 10? ')
  num = int(answer)
  print(10/num)
except ZeroDivisionError as e:
  print('Zero? Really?')
except ValueError as e:
  print('Not a number')
  print(e)
finally: #always excute regardless of the error that occurs. 
  print('Finally always runs.')

