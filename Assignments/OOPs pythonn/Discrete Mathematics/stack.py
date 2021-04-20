
class Stack:   
    def __init__(self,size=20):
        self.size=size
        self.array=[0]*size
        self.top=-1

    def isFull(self):
        if self.top==self.size-1:
            return True
        return False        
    def isEmpty(self):
        if self.top==-1 :
            return True
        return False
    def push(self,element):
        if(self.isFull()):
            print("Stack Overflow !!\n ")
            return
        self.top+=1
        self.array[self.top]=element
        
    def pop(self):
        if(self.isEmpty()):
            print("Stack Under flow !! \n")
            return None
        element=self.array[self.top]                
        self.top-=1
        # print(element)
        return element
    def peek(self):
        if(self.isEmpty()):
            return None
        return self.array[self.top]
    def total_elements(self):
        return self.top+1    

    def display(self):
        print(self.array)

# choice=1
# while(choice!=6):
#     print("1.Create Stack\n2.Push object\n3.Pop object\n4.Peek\n5.total elements\n6.exit")
#     try:

#         choice=int(input())
#         while(choice not in range(1,7)):
#             choice=int(input("enter a valid choice: "))
#     except:
#         print("invalid choice try again \n")
#         continue
#     if(choice==1):
#         stack_size=int(input("enter stack size :"))
#         stack_name=Stack(stack_size)
#         print("Stack is create with size:",stack_size)
#     elif(choice==2):
#         stack_name.push(Student(input("enter name :\n"),int(input("roll no:\n")),int(input("age:\n"))))    
#     elif(choice==3):
#         print("\n\nelement:\n",stack_name.pop(),"\n")
#     elif(choice==4):
#         print("\n\npeek element:\n",stack_name.peek(),"\n")
#     elif(choice==5):
#         print("total elements:",stack_name.total_elements(),"\n")        



# Student_record=Stack(30)
# obj=Student("Nitesh",21,21)
# Student_record.push(obj)
# print("peek\n",Student_record.peek(),"empty ",Student_record.isEmpty())
# print("\npopped element\n",Student_record.pop())
# Student_record.pop()