def create_matrix():
    print("matrix creation:\n enter row and col ")
    row=int(input("row:"))
    col=int(input("col"))
    matrix=[[0]*col for _ in range(row)]

    return matrix,row,col

def matrix_multiply():                                                 #matrix multiplication function 
    print("matrix multiplication boyyy")
    print("enter dimesions for first ")

    row1=int(input("row :"))                                      #taking row and colomn inputs from user 
    col1=int(input("col :"))

    print("enter dimensions for matrix second")

    row2=int(input("row :"))
    col2=int(input("col :"))

    if(col1!=row2):                                               #check condition for matrix mltiplication
        print("multiplication not possible")
    else:
        right_matrix=[[0]*col1 for _ in range(row1)]              #Allocating memory for matrix
        left_matrix=[[0]*col2 for _ in range(row2)]
    
        print("enter values for matrix 1  row wise ")               #taking elements as an input from user
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
        display_Matrix(left_matrix,row1,col1)                       #displaying the matrix
        print("matrix 2")
        display_Matrix(right_matrix,row2,col2)
    
        r2=0
        c1=0
        final=[[0]*col2 for _ in range(row1)]
        for row in range(row1):                                       #iterating throw rows of first matrix
            for col in range(col2):                                    #then coloumns of second matrix                 
                r2=0
                c1=0 
                while(c1<col1 and r2 <row2):
                    final[row][col]+=right_matrix[row][c1]*left_matrix[r2][col]
                    #print("final[",row,"][",col,"]=",final[row][col],"\t",end='')
                    #print("c ",row,col ,"= a ",row,c1," * b",r2,col)
                    r2+=1
                    c1+=1
                    #print("")
                    #print("final",final)
             

        print("result")
        display_Matrix(final,row1,col2)

def insert_matrix(matrix,row,col):
    #print("rows :",row,"\t coloumns",col)
    for rows in range(row):
        for cols in range(col):
            matrix[rows][cols]=int(input())


def initialize_matrix():
    row=int(input("row: "))
    
    col=int(input("col: "))
    
    return ([[0]*col for _ in range(row)]),row,col

def sum_of_diagonal():
    ##print("u have enterd into diagonal function")
    matrix,row,col=create_matrix()
    print("input element values")
    insert_matrix(matrix,row,col)
    sum=0;
    for rows in range(row):
        for cols in range(col):
            if(rows==cols):
                sum+=matrix[rows][cols]
    print("entered matrix :")
    display_Matrix(matrix,row,col)
    return sum       

    
def display_choices():
    print(" \n 1.Matrix Muliplication \n s.Sum of diagonals \n 3.insert into matrix\n 4.initialize matrix \n 5.exit \n\n")

def display_Matrix(matrix,row,col):
    print("\n")
    for rows in range(row):
        for cols in range(col):
            print(matrix[rows][cols], "\t",end='')
        print("\n")

def input_choices():
    choice =int(input("Enter your choice \t :"))
    while choice <1 or choice>5:
        print("enter a valid choice from 1-5")
        choice=int(input())
    return choice

display_choices()
choice=input_choices()
arr=[matrix_multiply,sum_of_diagonal,insert_matrix,initialize_matrix]



while choice!=5:

    if(choice==5):
        break
    elif choice==1:
       matrix_multiply()
    elif choice == 2:
        print("sum of diagonal",sum_of_diagonal())
    elif choice ==3:
        insert_matrix()
    display_choices()
    choice=input_choices()    