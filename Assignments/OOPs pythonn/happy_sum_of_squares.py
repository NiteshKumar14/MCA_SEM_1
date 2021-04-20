
def sum_of_squares(sqdnumber):                         #defining a function that take a string and return its elements sum 
    sqdNumber_result=0                                 #initializing sum array for storing sum
    iteratator=len(sqdnumber)-1                        #iterating till the length of string in descending order
    if not iteratator:                                 #if the length of string is 1(here iterator will be zero)
        return int(sqdnumber[0])**2

    while iteratator:                                      #looping digits
        sqdNumber_result+=int(sqdnumber[iteratator])**2     
        iteratator-=1
        if(iteratator==0):                                  #for the last index(0) as loop will exit now
            sqdNumber_result+=int(sqdnumber[iteratator])**2
    return sqdNumber_result                                     

def happy_number(number):                                   #happy function determines whether a number is happy or not 
    iterator=10                                             #performing 10 iteration to prevent infinite loop.
    if sum_of_squares(number)==1:                           #edge case if the number sum of squares is 1 
        return True
    while iterator:                                         
        number=sum_of_squares(str(number))                   #storing the sum of squares of the number 
        if sum_of_squares(str(number))==1:                   #condition for happy number 
            return True
        iterator-=1
    return False










# test_case=int(input("test_cases:\t"))                                            #taking input as string 
number=input()
print("sum of squares :",sum_of_squares(number))                        #invoking sum of squares function 
if happy_number(number) :                                                          
    print("Its a Happy Number")
else:
    print("Not a Happy Number ")    















#     number=input("enter a number:\t")
    
#         if happy_number(str(iterator)):
#             print(sum_of_squares(str(iterator)),"\t",end='')
#             print(iterator)
#             # print("Its a Happy Number\t")
#     # else:
#     #     print("Not a Happy Number\t")
#     test_case-=1

