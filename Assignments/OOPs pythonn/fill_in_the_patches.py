#Function to take input marks of students in list ‘marksList’ with total strength ‘numStudent’
def inputMarks(numStudent):
    marksList=[0]*numStudent
    for i in range(numStudent):
        marksList[i]=int(input("Enter marks for student "+str(i+1)+":"))   #marks  should int Statement 1: mi=int(m1)  
    return marksList


#Function to validate the input marks i.e. marks should be between 0 to 100.
#returns TRUE if list of marks is valid otherwise returns FALSE
def validateMarks(marks):
    for i in range(len(marks)): # Traverse each element 
	    if (marks[i]<0 or marks[i] >100):    #checking range of marks Statement 2: if (marks<0 or marks >100):
		    return False
    return True


#Main Script
TotalMarks=[]
numStudents=int(input("Enter Total Number of students:"))
print("Enter Marks for 1st subject")
marks1=inputMarks(numStudents)
print("Enter Marks for 2nd subject")
marks2=inputMarks(numStudents)
if not validateMarks(marks1) or not  validateMarks(marks2) :                           #checking both marks for validity 
	print("Invalid Marks")
else:
    for i in range(len(marks1)):        #iterate in marks length
        TotalMarks.append(marks1[i]+marks2[i])
print(TotalMarks)