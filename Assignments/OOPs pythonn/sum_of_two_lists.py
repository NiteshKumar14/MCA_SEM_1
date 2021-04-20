def sumTwoNum(x,y):
    z=x+y
    return z
    
def sunList(list1,list2):
    sum=[0]*row                     #initializing list to length of upcoming list

    for row in range(len(list2)):       #looping till the length  of list (same length expected )

        sum[row]+=list1[row]+list[row]  #taking elements from both list and adding and saving in resultant list
    return sum                          #returing list


    