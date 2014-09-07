#In class Exercises

#EXERCISE 1: BILL CALCULATOR
#Ask user to enter in the cost of meal and change it into a floating type number
meal = raw_input('Enter the cost of your meal: ')
meal = float(meal)

tax = 0.0675
tip = 0.15
total_bill = meal * (1 + tip + tax)

#print total_bill up to 2 decimal digits (to cents).
print "Your total bill is %.2f dollars." %(total_bill)






#EXERCISE 2: TIME AND DATE
#First import the current time and date.
from datetime import datetime
now = datetime.now()

#print the time and date by calling on the strings using %s.
print 'The current time is %s:%s.' %(now.hour, now.minute)
print 'The current date is %s/%s/%s.' %(now.month, now.day, now.year)





#EXERCISE 3: BOOLEANS
MakeMeTrue = 3 >= (1239 % 7)
print MakeMeTrue

