string = 'pasta'
rev = ''

#iterate over a sequence, counting backward
#-1,-1,-1 
'''
-1 = START FROM REVERSE
-1 = NOT INCLUSIVE SO 0
-1 = MOVE BACKWARDS
'''
for j in range(len(string)-1,-1,-1):
    #concatenate character at index j
    rev += string[j]
    
print(rev)