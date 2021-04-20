"""
1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

"""
for line in range(1,6):
    for digits in range(1,line+1):
        print(digits,end='')
    print("")    


"""
                    1
                2   1   2
            3   2   1   2   3
        4   3   2   1   2   3   4
                   
        

"""
count=5
digit=1
left=1
right=1
limit=1
while count:
    print("\t"*count,end='')
    # print("count: ",count)
    left=digit
    right=1
    while left>1:
        print(left,"\t",end='')
        left-=1
    while right<=digit:     
        print(right,"\t",end='')
        right+=1
    digit+=1
    print("")
    count-=1    
    


"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1 
"""
count=5
while count:
    digits=count
    while digits:
        print(digits,end='')
        digits-=1
    print("")
    count-=1  


"""
1
2 2
3 3 3
4 4 4 4 
5 5 5 5 5
 
"""    
for lines in range(1,6):
    times=lines
    while times:
        print(lines,end='')
        times-=1
    print("")

'''
1 2 3 4 5
  2 3 4 5
    3 4 5
      4 5
        5
'''

for lines in range(5):
    print(" "*lines,end='')
    digits=lines+1
    while digits<=5:
        print(digits,end='')
        digits+=1
    print("")    



'''
*   *   *   *   *

*               *                              

*               *

*               *

*   *   *   *   *

'''    

for lines in range(1,6):
    if(lines==1 or lines ==5):
        print("*\t"*5,end='')
    else:
        print("*",end='')
        print("\t"*4,end='')
        print("*",end='')
    print("")    

print("")
'''
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
'''
for lines in range(1,6):
    print("*\t"*5)




"""
                    *
                *   *   *
            *   *   *   *   *
        *   *   *   *   *   *   *
    *   *   *   *   *   *   *   *   *                
"""

count=5
digit=1
left=1
right=1
limit=1
while count:
    print("\t"*count,end='')
    # print("count: ",count)
    left=digit
    right=1
    while left>1:
        print("*","\t",end='')
        left-=1
    while right<=digit:     
        print("*","\t",end='')
        right+=1
    digit+=1
    print("")
    count-=1    


print("\n")

"""
    *   *   *   *   *   *   *
        *               * 
            *       *
                *     
"""

lines=7
real_lines=7
spaces=0
while lines>=1:
    if(spaces==0):
        print("*\t"*lines,end='')
    else:
        
        
        print("\t"*spaces,end='')
        stars=real_lines-2*spaces
        # print("stars :",stars)
        for i in range(stars):
            if(i==0 or i==(stars-1)):
                print("*\t",end='')
            else:
                print("\t",end='')
    print("")
    lines-=2    
    spaces+=1








    """
    *   *   *   *   *   *   *
        *   *   *   *   * 
            *   *   *
                *     
    """

lines=7
real_lines=7
spaces=0
while lines>=1:
    if(spaces==0):
        print("*\t"*lines,end='')
    else:
        print("\t"*spaces,end='')
        stars=real_lines-2*spaces
        # print("stars :",stars)
        for i in range(stars):
                print("*\t",end='')
            
    print("")
    lines-=2    
    spaces+=1


print("\n")
"""
            *
        *       *
    *               *
*                       *
    *               *
        *       *
            *                           

"""
spaces=7//2
lines=1
while lines<9:
    print("\t"*spaces,end='')
    if(lines==1):
        print("*",end='')
    else:
        # print("lines",lines)
        for i in range(1,lines+1):
            if(i==1 or i==lines):
                print("*\t",end='')
            else:
                print("\t",end='')    
    print("")
    spaces-=1
    lines+=2
lines=5

spaces=1
while lines>=1:
    print("\t"*spaces,end='')

    for i in range(1,lines+1):
        if(i==1 or i==lines):
            print("*\t",end='')
        else:
            print("\t",end='')    
    print("")
    lines-=2    
    spaces+=1



print("\n")



"""
                *
            *   *   *
        *   *   *   *   *
    *   *   *   *   *   *   *
        *   *   *   *   *
            *   *   *            
                *
"""






    

spaces=7//2
lines=1
while lines<9:
    print("\t"*spaces,end='')
    if(lines==1):
        print("*",end='')
    else:
        # print("lines",lines)
        for i in range(1,lines+1):
            print("*\t",end='')
    spaces-=1
    lines+=2
    print("")
lines=5

spaces=1
while lines>=1:
    print("\t"*spaces,end='')

    for i in range(1,lines+1):
        print("*\t",end='')
        
    print("")
    lines-=2    
    spaces+=1

print("\n")

"""
$
$$
$$$
$$$$
$$$$$
"""


for lines in range(5):
    print(" "*lines,end='')
    digits=lines+1
    while digits<=5:
        print("$",end='')
        digits+=1
    print("")    
"""
     #
    ##
   ###
  #### 
######
           
"""
print("\n")
spaces=4
for lines in range(5):
    print(" "*spaces,end='')
    digits=lines+1
    while digits>=1:
        print("#",end='')
        digits-=1
    print("")
    spaces-=1
