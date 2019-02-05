'''
Shannon Sprague
sspragu2@binghamton.edu
A54 and Vladimir Malcevic
Assignment #1
'''

'''
ANALYSIS

Create a program that outputs the total amount in dollars that the user has
in change. 

OUTPUT to monitor:
  total_dollars (float) - amount of change in dollars
  . . .

INPUT from keyboard:
  quarter_count (int) - number of quarters entered by user
  dime_count (int) - number of dimes entered by user
  nickel_count (int) - number of nickels entered by user
  penny_count (int) - number of pennies entered by user
  . . .

GIVENS:

  ONE_HUNDRED (int) - 100
  QUARTER (int) = 25
  DIME (int) = 10
  NICKEL (int) = 5
  PENNY (int) = 1

PROCESSING:
  Get input, Convert str input to int values
  Find total value of each type of coin:  coin_type_value * coin_type_count
    (substitute actual coin_type:  quarter_value, quarter_count, etc.)
  Convert int value to dollar value (will be float):  total_value / 100
  Display output

  
'''

# CONSTANTS 
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1
ONE_HUNDRED = 100


# This program outputs the total amount of change that a user has in dollars
# given the count of each type of coin

def main():

  # Explain purpose of program to user
  print("This program will print out the total amount of change " +
        "you have in dollars when you provide a count of each type of coin")

  # Ask user for number of coins they have
  ## Start with quarters, end with pennies
  # Note constraints: no dollar, half-dollar coins
  quarter_count_str = input("Please enter the number of quarters you have:  ")
  # Ask user for number of dimes
  dime_count_str = input("Please enter the number of dimes you have:  ")
  # Ask user for number of nickels
  nickel_count_str = input("Please enter the number of nickels you have:  ")
  # Ask user for number of pennies
  penny_count_str = input("Please enter the number of pennies you have:  ")
  

  # Convert str data to int
  quarter_count = int(quarter_count_str)
  dime_count = int(dime_count_str)
  nickel_count = int(nickel_count_str)
  penny_count = int(penny_count_str)

  # Multiply the value of each type of coin by it's count and sum each result
  total_cents = (QUARTER * quarter_count) + (DIME * dime_count) + \
  (NICKEL * nickel_count) + (PENNY * penny_count)

  # Convert to dollars (float)
  total_dollars = total_cents / ONE_HUNDRED

  # Display labeled and formatted amount in dollars
  print("The total amount of change you have in dollars is $%.2f" %
        total_dollars)
  

main()
