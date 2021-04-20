def pyramid(row):
    k=1
    for rows in range(1,row+1):
                                            # this function takes rows and prints pyramid 
        for elements in range(1,rows+1):
            print(k*k," ",end='')
            k+=1
        print()    
pyramid(3)     

def right_triangle(row):                        #this takes input rows and prints the row number the times the row is 

    for rows in range(1,row+1):
        for elements in range(1,rows+1):
            print(rows,end='')
        print()

right_triangle(5)            