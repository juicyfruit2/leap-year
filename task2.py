# write a program to input a year and a number of years.

# asking the user to enter the year they would like to start with 
start = int(input("What year do you want to start with ?:"))
num_of_years = int(input("How many years do you want to check:"))

# made use oof for loops and if statements 
for leap in range ( start, num_of_years + start):
  if leap % 4 == 0: 
   print(f"{leap} is a leap year")
  else:
   print(f"{leap} is not leap year")
   


    