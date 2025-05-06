list1 = ['1','dog','cat',789]


# list1.append("hello")
# print(list1)
#
# list1.pop(0)
# print(list1)

print(list1.index(789))

list1.append("Yoyoyo")
print(list1)

#removes last item
list1.pop()
#removes 2nd item from the list
list1.pop(1)
print(list1)
list1.insert(2,'inserted_item')
print(list1)
#Specify if there is a certain item in a list
print('dog' in list1)