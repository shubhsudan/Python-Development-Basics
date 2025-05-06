# # a = 5
# # while (a>0):
# #     print("a is being decremented: ",a)
# #     a -= 1
    
    
# x = 4
# while (x<128):
#     x = 2*x
#     print("x is now ",x)
# print("You have reached the end")

# inp = input("Hi please say hello ")
# while inp != "hello":
#     inp = input("Please say hello ")
    
# print("It\'s about time ")

# password = ""
# while password != "secret":
#     password = input("Please enter the password ")
#     if password == "secret":
#         print("Welcome!")
#     else:
#         print("Please try again - Wrong password ")


# x = int(input("Please enter the number"))
# while x <=10:
#     if x == 5:
#         print(x)
#         break
#     print(x)
#     x +=1
    

# for number in range(1,21):
#     #test for odd nums
#     if(number % 2 != 0):
#         if(number % 3 == 0):
#             continue
#         print(number)

# for i in range(1,4):
#     print('i:',i)
#     for j in range(1,3):
#         print( '\t','j:', j)

for i in range(1,11):
    for j in range(1,11):
        print("{} * {} = {}".format(i, j, i * j))