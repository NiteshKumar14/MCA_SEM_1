'''
1. Write a function that takes a list of values as input parameters and returns another list without any duplicates.
'''
def distinct(lists):
    hashmap={}
    for items in lists:
        # print("items :",items)
        found=hashmap.get(items,2)
        # print("found: ",found)
        if(type(found)==int):
            # print("nahi mila")
            hashmap[items]=""
            # print(hashmap)
    return list(hashmap.keys())   

input_list=input().split()
print("entered list: ",input_list)
print("after removing duplicates",distinct(input_list))


'''
2. Write a function that takes a list of numbers as input from the user and produce the corresponding cumulative list where each element in the list at the index i is the sum of elements at index j<=i.
'''
def commulative_sum(lists):
    sum=0
    commulative_list=[]
    for items in lists:
        sum+=int(items)
        commulative_list.append(sum)
    return commulative_list

print("commulative sum: ",commulative_sum(input_list))


'''
3. Write a function that takes a number as an input and creates a list of n lists such that ith list contains first five multiples of i.

'''
def first_five_multiples(n):
    list_n=[int(input()) for x in range(n)]
    multiple_five=[]
    for items in list_n:
        list_m=[int(items)*x for x in range(1,6)]
        multiple_five.append(list_m)    
    return multiple_five            

print("multiple of five of each i in list n :",first_five_multiples(int(input("enter size of list "))))
