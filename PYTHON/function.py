def numeric_to_letter_grade():
    if grade >=90:
        print("A")
    if grade >=80:
        print("B")
    if grade >=70:
        print("C")
    if grade >=60:
        print("D")
    else:
        print("F")

#get user input of a numerical grade
grade = int(input("Enter your grade: "))

#cast to an int
grade = int(grade)
        
#call the numeric_to_letter grade function defined above
numeric_to_letter_grade()


#BUILT IN FUNCTIONS 
#print,input,int,str,float,round(float,int)
'''
max(arg1,arg2,argN)
'''
