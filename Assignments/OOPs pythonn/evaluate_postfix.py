from stack import Stack

"""
this function performs operation based on operator on given 2 operands 
returns the result after operation
"""
def perform_operation(operator,operand1,operand2):          
    if operator=="/":
        return operand1/operand2
    elif operator=="*":
        return operand1*operand2
    elif operator=="+":
        return operand1+operand2
    return operand1-operand2            

"""
this function checks whether the given character is counter or not that is  for ->'[' this ->']' for ->'(' this->')'   
INPUT:charater
OUTPUT:returns true or false 
"""
def isCounter(bracket1,bracket2):
    if (bracket1=="[" and bracket2=="]") or (bracket1=="{" and bracket2=="}") or (bracket1=="(" and bracket2==")"):
        return True
    return False
    
"""
this function checks whether the given character is operator or not 
INPUT:charater
OUTPUT:returns true or false 
"""

def is_operator(character):
    if character=="+" or character=="-" or character=="/" or character=="*" or character=="**" or character=="(":
        return True
    return False     
"""
takes a postfix expression and evalates based on that .
INPUT:postfix expression as string
OUTPUT:returns the expected output 
"""
def evaluate_postfix(expression):
    post_Stack=Stack()
    for chars in expression:
        if not is_operator(chars) and chars not  in "{[()]}":
            post_Stack.push(int(chars))
            continue
        operand2=post_Stack.pop()
        operand1=post_Stack.pop()
        # print("operand 1 : ",operand1,": operand2",operand2)
        post_Stack.push(perform_operation(chars,operand1,operand2))
    return post_Stack.pop()        
"""
OPERATION:checks validity of an expression
INPUT:expreesion as string 
OUTPUT:true for valid and false for invalid 
"""
def valid_expression(expression):
    # print(expression)
    brackets_stack=Stack()
    opening_brackets ="[{("
    closing_brackets="]})"                              
    is_missing=False
    for chars in expression:
        if chars in opening_brackets:
            brackets_stack.push(chars)
            # print("pushed ",chars)
        elif chars in closing_brackets:
                
            if isCounter(brackets_stack.peek(),chars):
                brackets_stack.pop()
                # print(" popped ",chars )
            else:
            # print("unwanted closing bracket \"",chars,"\"")

                is_missing=True
                break
            
    if brackets_stack.isEmpty():
        return True
    missing=[]
    print(missing)
    while(not brackets_stack.isEmpty() and  is_missing):
        if brackets_stack.peek()=="{":
            missing.append("}")
            brackets_stack.pop()
        elif brackets_stack.peek()=="[":
            # print(" s ")
            missing.append("]")
            brackets_stack.pop()
        else:
            # print(" p ")
            missing.append(")")
            brackets_stack.pop()
        
    # print("missing ones ",missing) 
    return False       

"""
OPERATION:Converts infix to postfix
INPUT:expreesion as string 
OUTPUT:a postfix expression  
"""

def infix_to_postfix(expression):
    stack=Stack()
    operators={}
    operators["+"]=2
    operators["-"]=2
    operators["*"]=3
    operators["/"]=3
    operators["("]=1
    operators["**"]=4
    output=""
    for char in expression:                                 #looping thought input character by character 

        # print(char ," :: ",output)                        #checking wether closing bracket is found or not based on that 
                                                            #poping util opening is not found on stack as bracket has highest priority 

        if char==")":
            # print("closing found")
            while(stack.peek()!="("):
                output+=stack.pop()+" "
            # print("peek befo",stack.peek())
            stack.pop()
            # print("peek afer ",stack.peek())

        elif  not is_operator(char):                        #if it is not operator that is a operand then simply append in the output 

            # print("not operator :",char)
            output+=char+" "
        
        else:                                               # if it is operator than check for previous element in stack 
                                                            # if empty simply push else if not empty check for precedence 
                                                            #if stack element is higher than pop and push the current operator 
                                                            # if no condition met simply push that operator                                      
            # print("operator :",char)
            current_op=stack.peek()
            # print("current op ",current_op)
            if(current_op is None):
                stack.push(char)
                # print("pushed op",char)
                continue
            elif(operators[current_op]>=operators[char] and char!="("):
                output+=stack.pop()+" "
                # print("pushed op in dict",char)
                stack.push(char)
            else:
                # print("pushed anyway::",char)
                stack.push(char)    

    while(not stack.isEmpty()):
        output+=stack.pop()+" "
    return output    

expression=input(" expression  to check its validity space seperated !!!! :")
if valid_expression(expression.split(" ")):
    print(expression," is valid ")
    print("postfix :",end='')
    expression=infix_to_postfix(expression.split(" "))
    print(expression)
    # expression= expression.split(" ")
    # post=""
    # for i in expression:
    #     post+=i 
    # print(post)    
    expression=expression.split(" ")
    # print(expression[:-1])
    result=evaluate_postfix(expression[:-1])
    print("result: ",result)    
else:
    print(expression," is Invalid ")    
# expression=input(" expression  infix:")
