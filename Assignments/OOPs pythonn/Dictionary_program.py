
size=int(input("list size "))
iterator=0
ele=0
list=[]
for iterator in range(size):
    ele=int(input())
    list.append(ele)
print(list)

list.sort()
print("sorted list",list)

count = 0
freq = []
iterations = len(list)
print("iterations",iterations)
current_element = list[0]
for iterator in range(iterations):
    if list[iterator] == current_element:
        count += 1  
    elif list[iterator] != current_element:
        freq.append(current_element)
        freq.append(count)
        count = 1
        current_element=list[iterator]
        if((iterations-iterator)==1):
            print("this occured")
            freq.append(current_element)
            freq.append(count)

    
    
print("iterator",iterator)
print("freq list",freq)
print("item \t freq ")

# freq_size=len(freq)
# for items in range(freq_size):
#     print("items ",items)
#     print(freq[items],"\t",freq[items+1])
    


    

        
    

