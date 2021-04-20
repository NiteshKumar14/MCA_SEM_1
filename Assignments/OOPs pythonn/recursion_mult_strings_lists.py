'''
recursive function that takes two operands and performs multiplication 
using approach that is :
multiplication is equivalent to repetitive addition of any operand times the other 

'''


def mult(operand_one,operand_second,accumulator=0):                     #defining function with three arguments with one as accumulator having default value 0

    if operand_one==0 or operand_second==0:                             #terminating condition if anyone of the operand is 0 then return 
        return accumulator
    if operand_one>operand_second:                                       #reducing computation by finding the bigger number 
        return mult(operand_one,operand_second-1,accumulator+operand_one)   
    else:
        return mult(operand_one-1,operand_second,accumulator+operand_second)        #decrementing the smaller number 

def length_string(string,count=0):
    # print("string :",string,": ",count)
    if string=="":                                 #terminating condition when string gets empty
        return count
    else:
        return length_string(string[1:],count+1)    #else again calling fuction with string excluding its first character  



def reverse(string,rev_string=""):
    # print("string ",string," rev ",rev_string)

    if string=="":                                  #terminating condition when string gets empty
        return rev_string
    else:
        # print(" after : ",string[:-1])
        return reverse(string[:-1],rev_string+string[-1])    #appending the last element of string and slicing string excluding its last one



def palindrome(string):
    if string=="":                                      #terminating condition if string is empty return true 
        return True
    if string[-1]!=string[0]:                           #if any coresponding char for last to first are unequal that means its not a palindrome 
        return False
    else:
        return palindrome(string[1:-1])    



'''
input : a list 
output: returns a list without any nesting 
'''

def flatten_list(listt,out=[]):                         #performs:it flattens the list recursively by checking elements type 
    # print("out : ",out)
    # print("list : ",listt)
    if listt==[]:                                       #terminating condition if list is empty 
       return out
    else:
        try:                                            #if its list perform the same operation recursively
                                                        #else append in out list 
            element=listt[0]
            # print("element : ",element)
            if type(element)!=type(list()):
                out.append(element)
            else:
                return flatten_list(element,out)
        except:
            # print("not a list")
            out.append(element)
        finally:
            return flatten_list(listt[1:],out)          #call the function again with list excluding its first element 

'''
shallow copy function
input: a list ,its length 
output: a list 
'''


def copy_list(listt,length,replica=[],count=0):
    if count==0:                                        #initializing output list with zeroes equal to length of input list            
        replica=[0]*(length)
        # print("replica: ",replica)
    if count==length:                                   #if its reaches to the end of list return output list 
        return replica
    
    else:                                               #otherwise just make every corresponding element to that of input list 
        replica[count]=listt[count]
        
        return copy_list(listt,length,replica,count+1) #atlast return with updated count    
'''
deep copy function that makes copy of even the nested containers 
input : a list 
output: a list that  is copy of the input list 

'''

def deep_copy(listt,out=[]):                            
    # print("list:",listt)
    # print("out : ",out)
    if listt==[]:                                   #terminating condition if list is empty 
        return out
    else:
        element=listt[0]                            #picking the very first element 
        # print("element : ",element)
        if(type(element)!=type(list())):            #if its not a list simply append 
            out.append(element)
        else:
            new_list=list()                          #make a list and append its after its element gets copied 
            
            out.append(deep_copy(element,new_list))     
        return deep_copy(listt[1:],out)              #call again with list excluding its first element 

'''
performs insertion in list using recursion 
input : a list 
output: same list with values inserted 
'''
def list_insert(string ,listt=[]):
    # print("data type \n 1.int \n2.string \n ")
    print(string)
    if string=="":
        return "",listt
    
    if  string[0]=="]":                                                # if input is closing  brackets then its means current list has ended 
        # print("] closing mila ")
        return string[1:],listt
    
    if string[0]=="[":                                                # if its a opening brackets then simply create a list and call for that too and append its value in the current list 
        # print("[ opening mila ")
        new_list=list()
        string,new_list=list_insert(string[1:],new_list)
        # print("new list",new_list)
        listt.append(new_list)
        # print("after new list completion:",len(string),":",string)
        return list_insert(string,listt)
    else:                                                        # if its not string that means an integer value  
        listt.append(int(string[0]))                                      # append that in the list 
        return list_insert(string[1:],listt)                                       #simply return to the list 

problem_statement='''
1. Multiplication of two numbers without using multiplication operator

'''
print(problem_statement)
op1,op2=int(input("operand one : ")),int(input("operand second : "))
print(op1,"*",op2,"=",mult(op1,op2))

problem_statement='''
Related to Strings:
2. Count the number of elements in a string
3. Reverse of a string
4. To check whether a given string is palindrome or not

'''
print(problem_statement)
test_cases=int(input("test cases: "))


while test_cases:
    
    string= input("enter a string ")
    print("its length   :",length_string(string))
    print("reverse      : ",reverse(string))
    print("palindrome   : ",palindrome(string))
    test_cases-=1

problem_statement='''
Related to Lists

5. Flatten a list
'''

print(problem_statement)

# taking input from user recursively using list_insert function

#just for demo i am taking hardcoded list as [1, 2, 4, [5, [[7, 10, 'apple'], 8], 9], [1, [2, [3, ['spoon', [33, [1]]]]]]]
#can be made by user (refer at line 174) working of insert_list function 
string=input("enter list without any commas and spaces ")
string ,listt1=list_insert(string)
print(listt1)
listt=[1, 2, 4, [5, [[7, 10, 'apple'], 8], 9], [1, [2, [3, ['spoon', [33, [1]]]]]]]
length=len(listt)
print("Main List:\n\n",listt1)

flatten_list=flatten_list(listt1)
print("flatten : \n\n",flatten_list)

problem_statement='''
6. Copy a list

'''
print(problem_statement)

shallow_list=copy_list(listt,length)

print(id(listt[0])," \n",id(shallow_list[0]))       #testing wether same value integers have same memory address or not 

print(" Testing shallow copy by making change at list[3][1] using shallow_list reference to value  MANGO")

print("Main List:\n\n",listt)
print("shallow copy :\n\n",shallow_list)

shallow_list[3][1]="MANGO"

print("shallow copy :\n\n",shallow_list)
print("after changes :\n\n","main list :\n",listt)


problem_statement='''
deep_list=deep_copy(listt)

'''
print(problem_statement)
deep_list=deep_copy(listt)

print("deep copy :\n\n",deep_list)
print("testing deep copy by making change at list[3][1] using deep_list reference to value GRAPES")

deep_list[3][1]="GRAPES"

print("after changes :\n","main list :\n\n",listt)
print("deep copy:\n\n",deep_list)





# element type : 1 i
# element type : 2 i
# element type : 4 i
# element type : [ s
# [ opening mila
# element type : 5 i
# element type : [ s
# [ opening mila
# element type : [ s
# [ opening mila
# element type : 7 i
# element type : 10 i
# element type : apple s
# element type : ] s
# ] closing mila
# element type : 8 i
# element type : ] s
# ] closing mila
# element type : 9 i
# element type : ] s
# ] closing mila
# element type : [ s
# [ opening mila
# element type : 1 i
# element type : [ s
# [ opening mila
# element type : 2 i
# element type : [ s
# [ opening mila
# element type : 3 i
# element type : [ s
# [ opening mila
# element type : spoon s
# element type : [ s
# [ opening mila
# element type : 33 i
# element type : [ s
# [ opening mila
# element type : 1 i
# element type : ] s
# ] closing mila
# element type : ] s
# ] closing mila
# element type : ] s
# ] closing mila
# element type : ] s
# ] closing mila
# element type : ] s
# ] closing mila
# element type : ] s
# ] closing mila
# element type : ] s
# ] closing mila
# [1, 2, 4, [5, [[7, 10, 'apple'], 8], 9], [1, [2, [3, ['spoon', [33, [1]]]]]]]