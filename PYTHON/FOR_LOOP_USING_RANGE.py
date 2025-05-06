for x in range(10):
    print(x)
print("")

for x in range(0,10):
    print(x)
#"" = PAGE BREAK    
print("")
for x in range(1,7):
    print(x)
print("")

for x in range(0,30,7):
    print(x)
print("")

for x in range(5,-1,-1):
    print(x)
    
odd_numbers = []
for number in range(1,1201):
    if (number%2!=0):
        odd_numbers.append(number)
        print(odd_numbers)
    