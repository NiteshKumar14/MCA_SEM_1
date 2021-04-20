class Matrix:
    
    def __init__(self,*args):
        if(len(args)==0):
            print("Dimension(M,N):\t",end='')
            self.row,self.coloumn =int(input()),int(input())
            self.row,self.coloumn =self.check_input(self.row,self.coloumn)
            self.space=[[0]*self.coloumn for _ in range(self.row)]
            print("\n")
        else:
            self.row=args[0]
            self.coloumn=args[1]
            self.row,self.coloumn=self.check_input(self.row,self.coloumn)
            self.space=[[0]*self.coloumn for _ in range(self.row)]

    def display(self):
        #print("__",""*(self.row+2),"__")
        for rows in range (self.row):    
            print("|",end='')      
            for cols in range(self.coloumn):
                if (self.coloumn-cols==1):
                    print(self.space[rows][cols],end='')
                else:
                    print(self.space[rows][cols]," "*2,end='')
            print("|")
        #print("__",""*(self.row+2),"__")

    def insert(self):
        for rows in range(self.row):

            for cols in range(self.coloumn):
                
                print("M(",rows,",",cols,")\t:",end='')

                self.space[rows][cols]=int(input())

            print("")
            
    def multiply(self,matrix_second):

        if(self.coloumn!=matrix_second.row):
            print("multiplication not possible")
        else:
            print("matrixes ")
            print("matrix 1")    
            self.display()
            print("matrix 2")
            matrix_second.display()
        
            r2=0
            c1=0
            result_matrix=Matrix(self.row,matrix_second.coloumn)

    
            for row in range(self.row):
                for col in range(matrix_second.coloumn):
                    r2=0
                    c1=0     
                    while(c1<self.coloumn and r2 <self.coloumn):
                        result_matrix.space[row][col]+=self.space[row][c1]*matrix_second.space[r2][col]
                        # print("final[",row,"][",col,"]=",final[row][col],"\t",end='')
                        #print("c ",row,col ,"= a ",row,c1," * b",r2,col)
                        r2+=1
                        c1+=1
                        #print("")
                        #print("final",final)
                

            
            return result_matrix

    def trace(self):
        # print("trace:")
        trace=0
        for rows in range(self.row):
            for cols in range(self.coloumn):
                if(rows==cols):
                    trace+=self.space[rows][cols]
        return trace

    def hadamard_product(self,second_matrix):
        
        if(self.row!=second_matrix.row or self.coloumn!=second_matrix.coloumn):
            return []
        else:
            resultant_matrix=Matrix(self.row,self.coloumn)
            for rows in range(self.row):
                for cols in range(self.coloumn):
                    resultant_matrix.space[rows][cols]=self.space[rows][cols]+second_matrix.space[rows][cols]
            return resultant_matrix        

    def check_input(self,row ,col):
        if row>0 and col >0:
            return row,col
        else:
            temp_list=[row,col]
        for ele in range(len(temp_list)):
            while temp_list[ele]<=0:
                if(ele==0):
                    print("row cannot be zero")
                else:
                    print("coloumn cannot be zero")
                temp_list[ele]=int(input())      

        return temp_list

# outer vector product = matrix multiplication where first matrix is coloumn(mx1) matrix and the other one is:
# row (1Xn)
    def  outer_vector_product(self,second_matrix):
        if(self.coloumn!=1 or second_matrix.row!=1 ):
            return -1
        return self.multiply(second_matrix)
            
def determinant_2x2(matrix):
        return (matrix.space[0][0]*matrix.space[1][1])-matrix.space[1][0]*matrix.space[0][1]

first_matrix=Matrix()
first_matrix.insert()
first_matrix.display()
print(determinant_2x2(first_matrix))

second_matrix=Matrix()
second_matrix.insert()
second_matrix.display()

first_matrix.multiply(second_matrix)

product_hadamard=first_matrix.hadamard_product(second_matrix)
if type(product_hadamard)==list:
    print("hadamard product not possible must be same size")
else:
    print("hadamard product\t",product_hadamard.display())
print("trace : First Matrix",first_matrix.trace())

result_outer_product=first_matrix.outer_vector_product(second_matrix)
print("outter product : ")
if type(result_outer_product)==int:
    print("not possible must me coloumn and row vectors ")
else:
    result_outer_product.display()    



