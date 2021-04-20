class Queue:
    def __init__(self,size=20):             #Creating a Queue class with default size 20 
                                            #using list data structure and using two pointer approach rear and front
                                            # and initializing list with the provided size
        self.__rear=-1
        self.__front=-1
        self.__size=size
        self.__array=[0]*size
        
    def get_size(self):                     # function to get the current size of the queue 
        return self.__size
    def isFull(self):                       # To check wether a list is full or not returns true or false                  
                                            
        if(self.__rear==self.__size-1):
            return True
        return False
    def isEmpty(self):                      #Empty function to check wether function is empty or not 
                                            #Returns true or flase based on the conditions                  
        if(self.__rear==-1 or self.__front>self.__rear  ) :
            return True
        return False

    def enqueue(self,element):              #Enqueue function that add elements in the queue and check for feasible condition 
        if self.isFull():
            print("queue is full !! \n")
            return
        if self.__rear==-1:
            self.__rear=0
            self.__front=0
        else:
            self.__rear+=1
        self.__array[self.__rear]=element
        return 
    def dequeue(self):                       #Dequeue function that removes the front element and returns that element again check all neccessary conditions 

        if self.isEmpty():
            print("queue is empty")
            return None
        element=self.__array[self.__front]  
        if(self.__front==self.__size-1):
            self.__front=-1
            self.__rear=-1

        else:
            self.__front+=1
        # print("array :",self.__array)
            
        return element
    def display(self):                      #display function that displays elements in the stack 
        # print("elements: ")
        # print("array: ",self.__array)
        # print("f :",self.__front," rear:",self.__rear)
        if self.isEmpty():
            print("[]")
            return
       
        for element in range(self.__front,self.__rear+1):
            print(self.__array[element], " ",end="")
        print("\n")


# choices Create queue , dequeue,enqueue,displayy queue 
def dynamicOptions(queue,count=0):                  
    options={0:"Exit"}
    print(count,"->",options[count])
    count+=1
    options[count]="Create Queue"
    print(count,"->",options[count])
    # if not queue.isFull():
    count+=1
    options[count]="Enqueue"
    print(count,"->",options[count])

    # if not queue.isEmpty():
    count+=1
    options[count]="Dequeue"
    print(count,"->",options[count])
    count+=1
    options[count]="Display Queue"
    print(count,"->",options[count])
    print("\n")
    return options
    
"""
Menu Driven programs 
Using diictionary to hold options 
"""
# queue=Queue()
# dy=True                                         
# while True:
#     if(dy):
#         valid_choices=dynamicOptions(queue)
#     try:
#         choice=int(input("select your choice :"))
#     except:
#         print("enter a valid interger ")
#         continue
#     if choice in valid_choices.keys():
#         if valid_choices[choice]=="Exit":
#             break
#         elif(valid_choices[choice]=="Create Queue"):
#             size=int(input("enter queue size ( default 20) :"))
#             queue=Queue(size)
#             # print("size :",queue.get_size())
#         elif valid_choices[choice]=="Enqueue":
#             element=input("element ")
            
#             queue.enqueue(element)
#         elif valid_choices[choice]=="Dequeue":
#             element=queue.dequeue()
#             print("dequeued Element  :",element)
#         elif valid_choices[choice]=="Display Queue":
#             queue.display()
#     else:
#         print("enter a valid choice")
#         dy=False





    
   

    
    


                












            