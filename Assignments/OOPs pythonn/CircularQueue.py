"""
Created a Circular Queue having attributes :
front("pointer to current firs element ")
rear("pointer to current last element")
size (Max size of Queue)
list data structure 
"""


class CircularQueue:
    def __init__(self,size=10):
        self.__size=size
        self.__front=-1
        self.__rear=-1
        self.__array=list(range(size))

    """
    is full checks the condition wether queue is full or not that is 
    1.when front=0 and rear =size -1 
    2.when rear is just one away from front 

    """
    def isFull(self):
        if (self.__front==0 and self.__rear==self.__size-1) or (self.__rear==self.__front-1):
            return True
        return False
    """
    Empty Condition of Queue
    1.when rear and front having value -1 

    """
    def isEmpty(self):
        if self.__rear==-1:
            return True
        return False
    """
    Inserting Elements in Queue :
    condition to be taken care of :
    1.wether my queue is full 
    2.rear reached at last and if front is not on zero that means rear can come to 0 
    3.Initially is queue is empty then simply make rear and front to 0
    4.if these are not the case then simply increment front and insert the element 

    """
    def enqueue(self,element):
        # print("enque front : ",self.__front," rear :",self.__rear)
        if self.isFull():
            raise Exception("Queue is full!")
        elif self.isEmpty():
                self.__front=self.__rear=0
        elif(self.__rear==self.__size-1):
                self.__rear=0
        else:
            self.__rear+=1        
        # print(" after enqueue \n front : ",self.__front,"\n rear :",self.__rear)        
        self.__array[self.__rear]=element
    """
    Removing elements from queue 
    Points to be taken care of
    1.if queue is empty (removal not possible)
    2.if queue has only one element 

    returns the dequeued element 
    """
    def dequeue(self):
        # print("d front : ",self.__front," rear :",self.__rear)
        if self.isEmpty():
            raise Exception("Queue is empty")
        
        element=self.__array[self.__front]
        if self.__rear==self.__front:
            self.__rear=self.__front=-1
        elif self.__front ==self.__size-1 :
            self.__front=0
        else:
            self.__front+=1

        # print("after dequeue  \nfront : ",self.__front," rear :",self.__rear)    
        
        return element
        
    
    """
    Overloaded the str function for displaying object 
    """
    def __str__(self):
        iterator=self.__front
        # print("iterator ",iterator)
        if self.isEmpty():
            return "oops queue is empty "
        string=""
        while(iterator!=self.__rear):
            string+=str(self.__array[iterator])+" "
            if(iterator==self.__size-1):
                print("itetator =0")
                iterator=0
                continue
            iterator+=1
        string+=str(self.__array[self.__rear])+" "
        
        return string

    def total_elements(self):
        if self.isEmpty():
            return 0
        iterator=self.__front
        count=0
        while(iterator!=self.__rear):
            count+=1
            if iterator==self.__size-1:
                iterator=0
                continue
            iterator+=1
        return count+1        
    def get_current_size(self):
        return self.__size

    def increase_size(self,increase):
        self.__size+=increase
        self.__array+=list(range(increase))




def dynamicOptions():
    count=0                  
    print(f"------------------------------------------")
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
    
    count+=1
    options[count]="Total Elements"
    print(count,"->",options[count])
    
    count+=1
    options[count]="Delete Queue"
    print(count,"->",options[count])
    
    count+=1
    options[count]="Current Size"
    print(count,"->",options[count])

    count+=1
    options[count]="Increase Current Size"
    print(count,"->",options[count])
    
    print(f"------------------------------------------")
    print("\n")
    return options
    
def main():
    """
    Menu Driven program 
    Using diictionary to hold options 
    Declaring a default Queue with size 10
    """
    queue=CircularQueue()
   
                                             
    while True:
        
        try:
        
            valid_choices=dynamicOptions()
            try:
                choice=int(input("select your choice :"))
            except:
                print("\n enter a valid integer \n")
                continue
            if choice in valid_choices.keys():
                if valid_choices[choice]=="Exit":
                    break
                elif(valid_choices[choice]=="Create Queue"):
                
                    size=int(input("enter queue size ( default 10) :"))
                    if size<=0:
                        raise Exception("\n size cannot be zero or negative\n")
                    queue=CircularQueue(size)
                                                            
                    # print("size :",queue.get_size())
                elif valid_choices[choice]=="Enqueue":
                    element=input("element :")
                    queue.enqueue(element)
                    
                elif valid_choices[choice]=="Dequeue":
                    
                    element=queue.dequeue()
                    print("dequeued Element  :",element,"\n")
                    
                elif valid_choices[choice]=="Display Queue":
                    print(queue)
                elif valid_choices[choice]=="Total Elements":

                    print("\nTotal elements :",queue.total_elements(),"\n")
                elif valid_choices[choice]=="Delete Queue":
                    
                    del queue
                    print("\nqueue deleted successfully\n")
                    
                elif valid_choices[choice]=="Current Size":
                    print("\ncurrent size :",queue.get_current_size(),"\n")
                else:
                    increase=int(input(" enter the increment value "))
                    if increase<=0:
                        raise Exception("\n increment value cannot be  zero or negative\n")
                    queue.increase_size(increase)
                    print("size increased \n current size :",queue.get_current_size(),"\n")
            else:
                print("\nenter a valid choice !!\n")

        except UnboundLocalError as e:
            print("queue is deleted cannot perform the operation \n Creating a default queue ")
            queue=CircularQueue()
            continue
        except Exception as e:
            print("\n error ::",e,"\n")
            
if __name__ == '__main__':
    main()



            
                            

