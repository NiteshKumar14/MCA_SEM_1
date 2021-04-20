def sumTwoNum(x,y):
    z=x+y
    return z
    
def sunList(list1,list2):
    sum=[0]*(len(list2))                    #initializing list to length of upcoming list

    for row in range(len(list2)):       #looping till the length  of list (same length expected )

        sum[row]+=list1[row]+list2[row]  #taking elements from both list and adding and saving in resultant list
    return sum                          #returing list


length=int(input("enter the length of list "))
print("enter values in list")
list1=[int(x) for x in input().split()]
list2=[int(x) for x in input().split()]
print("sum is ",sunList(list1,list2))

