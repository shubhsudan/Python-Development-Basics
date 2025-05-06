num_list = []
#position marker
i = 0
#Helps in while condition
playing = True

while (playing == True):
    
    num = int(input("Enter an int"))
    
    if (num == -1):
        playing = False
    else:
        num_list.append(num)
        i +=1
#get the sum of all entered numbers
num_sum = 0
for num in num_list:
    num_sum += num
    
#calculate the average
num_avg = num_sum/i

print("avg",num_avg)
    