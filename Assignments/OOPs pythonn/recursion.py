
#1.This function finds factorial of a number using iteration:

#input :
    #integer
#output: 
    #factorial in integer values 
  
#
def factorial_without_recursion(integer):                                                                          
    if integer<0:                                                       #factorial is not defined for negative number so returning -1 
        return -1

    if(integer==0 or integer==1):                                     #edge cases as factorial of both "1" and "0" is "1" and -ve numbers 
        return 1
   
    fact=1                                                            #  taking a variable with value 1 as factorial starts with 1
    i=1                                                               #initializing iterator from  1 and iterating till the number   
                                                                      
    while i<=integer:
        fact*=i                                                     #performing the factorial operation and incrementing iterator 
        i+=1
    return fact




#2.This function finds factorial  using recursion:

#input :an positive integer 
#output : factorial of number in integer value
def factorial_with_recursion_asc(integer):
    if integer<0:                            #factorial is not defined for negative number so returning -1                
        return -1                           


    if integer==0 :                             #terminating condition for recursive call
                                                        
        return 1

    else:
        factorial=factorial_with_recursion_asc(integer-1)*integer       #f(n)=f(n)*n  recurrence relation that evaluates factorial by calling n-1 subtree until terminating condition meets 
         
        
        print(integer," : ",factorial)                                  #print in order 1-N
        
        return factorial

#2.This function finds factorial  using recursion and prints in descending order of their consective numbers
# like 1:1,2:2,3:6 and so on 

#input :an positive integer and empty list to store factorial values  
# like f(1) then f(2) and so on till the number 
#output : factorial of number in integer value and a list 


def factorial_with_recursion_dsc(integer,list):                         
    # print(" : ",integer)
    if integer<0:                                                        #factorial is not defined for negative number so returning -1 
        return -1,[]
    if integer==0 :                                                      #terminating condition for recursive call
            
        return 1,[]

    else:
        
        factorial=factorial_with_recursion_dsc(integer-1,list)[0]*integer           #accessing the 2nd returned value of funtion 
        
        list.append(factorial)                                                      #adding evaluated value in the list 
        
        return factorial,list        


integer=int(input("enter a number: "))     
                                           #taking input from the user 

print("without recursion","\n",factorial_without_recursion(integer),"\n1.with recursion 1-N") # invoking  functions 

factorial_with_recursion_asc(integer)

print("2.with recursion,N-1")

list=factorial_with_recursion_dsc(integer,[])[1]

iterator=len(list)-1

while iterator>-1:                                                  #iterating list from end to start and then printing 
    print(iterator+1," : ",list[iterator])
    iterator-=1
