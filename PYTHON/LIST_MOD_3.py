#ls1 = [2,3,4]
# ls2 = [7,8,9]
# ls3 = ls1 + ls2
# print(ls3)
#
# ls4 = ls3 * 3
# print(ls4)
#
# ls1.extend(ls2)
# for l in ls1:
#     print(l)

#SLICING LIST
my_list = ['b','a','n','a','n','a','s']
print(my_list[2:5])

print(my_list[4:])

print(my_list[:])

print(my_list[:-4])
print(my_list[:-1])

#true copy of my list
copy_my_list = my_list[:]

print(copy_my_list)
print(copy_my_list == my_list)

odd_numbers =[2,4,6,8]
odd_numbers[0] = 1
print(odd_numbers)

#update multiple elements
odd_numbers[1:4] = [3,5,7]
print(odd_numbers)


