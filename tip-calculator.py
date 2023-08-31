#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator!")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
bill = float(input("What is the totall bills? $"))
tip = int(input("How much tip would you like to give? 10,12,or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill

bill_per_person = bill_with_tip/people

#Format the result to 2 decimal places = 33.60
final_amnt_each = "{:.2f}".format(bill_per_person)
#round(bill_per_person,2) this doesn't work if the end number is 0 it would show up as 27.5 not 27.50

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print(final_amnt_each)