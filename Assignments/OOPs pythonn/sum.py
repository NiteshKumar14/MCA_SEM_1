n=int(input())
list1=[-20,-199,-2,3,1,-1,-6,-1,0,5]
j=0

# for i in range(n):
#     list1.append(int(input()))
print(list1)
for i in range(10**6):
    print("i: ",i)
    sum = i
    j=0
    while j<len(list1):

        sum += list1[j]
        print("sum: ",sum)
        j+=1
        if sum < 1:
            break
        else:
            continue
    print("j: ",j)    
    if j == len(list1):
        print("x:",i)
        break