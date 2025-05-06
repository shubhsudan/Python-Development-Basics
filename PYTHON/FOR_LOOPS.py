# numbers = [1,2,3,4,5,6,7,8,9,10]

# even_number = []

# #to store count of even numbers
# even_count = 0

# for number in numbers:
#     #test if number is even
#     if (number % 2 == 0):
#         #append to even number list
#         even_number.append(number)
        
#         #increment count
#         even_count += 1
    
# print(even_number)
# print("There are ",even_count, "numbers even in the list")
# print("There are ",len(even_number), "numbers even in the list")

# #CHAPTER CHANGE
# #define list of numbers
# numbers = [5,3,8,-1,-2,2,0]
# #define min number variable
# min_number = numbers[0]
# #find the minimum value
# for number in numbers:
#     if number < min_number:
#         min_number = number
        
# print(min_number,"is the min number ")

#define list of strings
# planets = ['Sun','Mercury','Venus','Earth','Mars']
# for planet in planets:
#     if (planet == "Sun"):
#         print(planet," is not a planet")
#     else:
#         print(planet," is a planet")
        
#     if (planet == "Mercury"):
#         print(planet," is closest to the sun")

# month = "February"
# print(month,"is spelled:")
# # for char in month:
# #     print(char)
# for char in month:
#     print(char,end=' ')

user_name = input("What is your name?")
count = 0
print("The user's name is: ")
#task 1
for char in user_name:
    print(char,end = ' ')
    count += 1

print("")
print("There are",count, "letters in the name",user_name)