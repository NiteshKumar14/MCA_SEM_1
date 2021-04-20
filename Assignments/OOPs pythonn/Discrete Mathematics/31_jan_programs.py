"""
1. Write a program to implement Binary search (Recursive and Iterative).
2. Write a program to implement tower of Hanoi (Recursive and Iterative).
3. Write a program to generate a Pascal’s triangle.
4. Write a program to implement the following laws:

a. Identity laws
b. Domination laws
c. Double negation laws
d. Demorgan’s laws
e. Associative laws

5. Write a program to implement the tautology, Contradiction/Absurdity and Contingency.
6. Write a program to implement Modus ponens and Modus Tollens.
7. Write a program to implement .
8. Write a program to find the Union and Intersection of two sets.
9. Write a program to find the power set of the given set.
10. Write a program to find the permutation of the given set.
"""

"""
Binary Search using recursion 
"""
# 1 2 3 4 5 6 7 8 9 10
def binarySearch(array,left ,right,num):
    mid=(left+right)//2
    
    if array[mid]==num:
        return True    

    elif (left==right):
        print("what")
        return False
    
  
    
    elif num>array[mid]:
        # print("occured")/
        return binarySearch(array,mid+1,right,num)
    else:
        return binarySearch(array,left,mid-1,num)    


"""
Binary Search using iteration 
"""
def binarySearch_iterative(array,number):
    left =0
    right=len(array)-1
    
    while(left<=right):
        mid=left + (right-left)//2
        if array[mid]==number:
            return True
        elif array[mid]<number:
            left=mid+1
        else:
            right=mid-1   

    return False
 
print("enter size of array ")

size=int(input())
array=input().split(" ")
array=[int(x) for x in array]
print("array ",array)
# ?\num=int(input("enter a number to find in the array"))
# # print("length ",len(array))
# # if (binarySearch(array,0,len(array)-1,num)):
# #     print("number found ")
# # else:
# #     print("not found")    



test_case=int(input("test cases"))

while( test_case):
    num=int(input("num :"))
    if (binarySearch(array,0,len(array)-1,num)):
        print("number found ")
    else:
        print("not found")    
    test_case-=1


"""
2. Write a program to implement tower of Hanoi (Recursive and Iterative).
Recursive

"""
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B') 


"""
3. Write a program to generate a Pascal’s triangle.
"""

def main():
      x=int(input("Enter row number"))
      pascal(x)


#r-1
#  C
#   c-1
def pascal(num):
    list1=[]
    for i in range(num):
        templist=[]
        for j in range(i+1):
            if j==0 or j==i:
                templist.append(1)
            else:
                templist.append(list1[i-1][j-1]+list1[i-1][j])
        list1.append(templist)
    print(list1)
    for x in range(num):
        for y in range(x+1):
          print(list1[x][y],end=" ")
        print()


main()




"""
4. Write a program to implement the following laws:

a. Identity laws
b. Domination laws
c. Double negation laws
d. Demorgan’s laws
e. Associative laws

taking p and q as our propostions 
equivalence: eqv
complement: neg
"""

p=input("enter a statement")
q=input("another statement")
print("p:: ",p)

print("Identity laws \n p and True eqv p \n p or False eqv p  ")

print(p,"and True eqv to p::",p)
print(p,"or  False eqv to p::",p)

print(" Domination laws \n False and p eqv :: False \n True or p eqv:: True" )
print(" True or ",p,"eqv ::",True)
print(" False and ",p,"eqv ::",False)

print("Double negation laws \n neg(neg(p)) eqv p")
print("neg(neg(",p,"))eqv ::",p)


print("Demorgan’s laws \n neg(p and q) eqv neg(p) or neg(q)\n neg(p or q) eqv neg(p) and neg(q)" )
print("neg(",p," and" ,q,") eqv:: neg(",p,") or(",q,")")


print("Associative laws\n (p and q) and r eqv p and (q and r)")
print("(",p,"and",q ,") and ","r eqv::",p,"and(",q,"and r)")

"""
5. Write a program to implement the tautology, Contradiction/Absurdity and Contingency.
"""
#Tautology
print("-"*20,"Tautology","-"*20)
p=list(map(bool,map(int,input("Enter the no. separated by space").strip().split())))
print("Truth Table for Pv(~P)=True\n  P\t ~P\tPv~P\n","-"*20)
for i in p:
    print(i,"\t",not(i),"\t",i|(not(i)))

#Contradiction
print("-"*20,"Contradiction","-"*20)
p=list(map(bool,map(int,input("Enter the no. separated by space").strip().split())))
print("Truth Table for P^(~P)=True\n  P\t ~P\tP^~P\n","-"*20)
for i in p:
    print(i,"\t",not(i),"\t",i&(not(i)))

#Contigency
print("-"*20,"Contigency","-"*20)
p=list(map(bool,map(int,input("Enter the no. separated by space").strip().split())))
q=list(map(bool,map(int,input("Enter the no. separated by space").strip().split())))
r=list(map(bool,map(int,input("Enter the no. separated by space").strip().split())))
print("Truth Table for (PvQ)vR=Pv(QvR)\nP\t Q\t R\t(PvQ)\t(PvQ)^R\n","-"*50)
for i,j,k in zip(p,q,r):
    print(i,"\t",j,"\t",k,"\t",i|j,"\t",(i|j)&k)

"""
6. Write a program to implement Modus ponens and Modus Tollens.
"""
#Modus ponen
print("-"*20,"Modus Ponen","-"*20)
p=[0,0,1,1]
q=[0,1,0,1]
print("Truth Table for ( (P => Q) ^ P) => Q\nP\t Q\tP=>Q\t(P=>Q)^P\t((P=>Q)^P)=>Q\n","-"*50)
for i,j in zip(p,q):
    r=((not(i))|j)&i
    print(i,"\t",j,"\t",(not(i))|j,"\t ",r,"\t\t",(not(r))|j)

#Modus tollen
print("-"*20,"Modus Tollen","-"*20)
p=[0,0,1,1]
q=[0,1,0,1]
print("Truth Table for (~Q ^ (P => Q) ) => ~P\nP\t Q\tP=>Q\t~Q^(P=>Q)\t(~Q^(P=>Q))=>~P\n","-"*50)
for i,j in zip(p,q):
    r=(not(i))|j
    s=(not(j))&r
    t=(not(s))|(not(i))
    print(i,"\t",j,"\t",r,"\t ",s,"\t\t",int(t))

"""
8. Write a program to find the Union and Intersection of two sets.

"""
def main():
    A={1,2,3,4}
    B={2,4,6,8,10}
    union=A|B
    intersection=A&B
    print("Intersection of Set A and B:",intersection)
    print("Union of Set A and B:",union)

main()
"""
9. Write a program to find the power set of the given set.

"""
def main():
    string="ABC"
    x=constructSubSet("",0,string)
    print(x)
  

result=[]
def constructSubSet(subSet, index,string):
    if(index >= len(string)) :
      result.append(subSet)
      return
    
    constructSubSet(subSet, index + 1,string)
    constructSubSet(subSet + string[index], index + 1,string)

    return result
if __name__=="__main__":
    main()

"""
10. Write a program to find the permutation of the given set.

"""
def permutation(lst): 
  
  
    if len(lst) == 0: 
        return [] 
  
    if len(lst) == 1: 
        return [lst] 
  
  
    l = [] # empty list that will store current permutation 
  
    for i in range(len(lst)): 
       m = lst[i] 
  
       remLst = lst[:i] + lst[i+1:] 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  
  
# Driver program to test above function 
data = list('123') 
for p in permutation(data): 
    print(p) 