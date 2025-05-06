bill = float(input("How much is your meal?"))
tax = float(input("What is the sales tax(percentage)"))
tip = float(input("How much of a tip(percentage)?"))

#Calculate and add tax
tax_amount = (bill + tax) / 100 #calculate the tax
total = bill + tax

#calculate and add tip
tip_amount = (total * tip) / 100

total = total + tip_amount

#ROUND FUNCTION - NEW FOR US!
total = round(total,2)

print("The total bill is $",total)

