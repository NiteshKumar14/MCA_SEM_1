





def display_Matrix(matrix,rows,cols):
    for row in range(rows):
        for col in range(cols):
            print(matrix[row][col]," ",end='')
        print("")    







print("matrix multiplication boyyy")
print("enter dimesions for first ")

row1=int(input("row :"))
col1=int(input("col :"))

print("enter dimensions for matrix second")

row2=int(input("row :"))
col2=int(input("col :"))

if(col1!=row2):
    print("multiplication not possible")
else:
    right_matrix=[[0]*col1 for _ in range(row1)]
    left_matrix=[[0]*col2 for _ in range(row2)]
    
    print("enter values for matrix 1  row wise ")
    for row in range(row1):
        for col in range(col1):
            right_matrix[row][col]=int(input())
            #print("\t")
        #print("\n")
    
    print("enter values for matrix 2 row wise ")
    for row in range(row2):
        for col in range(col2):
            #print("a[",row,"][",col,"] :" )
            left_matrix[row][col]=int(input())
        
    print("matrixes ")
    print("matrix 1")    
    display_Matrix(left_matrix,row1,col1)
    print("matrix 2")
    display_Matrix(right_matrix,row2,col2)
    
    r2=0
    c1=0
    final=[[0]*col2 for _ in range(row1)]
   


    for row in range(row1):
        for col in range(col2):
            r2=0
            c1=0 
            while(c1<col1 and r2 <row2):
                final[row][col]+=right_matrix[row][c1]*left_matrix[r2][col]
               # print("final[",row,"][",col,"]=",final[row][col],"\t",end='')
                print("c ",row,col ,"= a ",row,c1," * b",r2,col)
                r2+=1
                c1+=1
                #print("")
                #print("final",final)
             

    print("result")
    display_Matrix(final,row1,col2)
        

       
