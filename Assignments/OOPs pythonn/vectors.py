class Vector:   
    count=0                     #defining vector class
                                                #defining two components x and y
    def __init__(self,_x=0,_y=0,_z=0):
        Vector.count+=1     
        #print("current count :",Vector.count)              
        self._x=str(_x)+"i"
        self._y=str(_y)+"j"
        self._z=str(_z)+"k"
                                                #addition of two vectors adding both the respective components and returning a vector object 
    def __add__(self,_vector):
        _x=int(self._x[:-1])+int(_vector._x[:-1])
        _y=int(self._y[:-1])+int(_vector._y[:-1])
        _z=int(self._z[:-1])+int(_vector._z[:-1])
        
        return Vector(_x,_y,_z)
    
    def __sub__(self,_vector):                   #subtracting thier components and returning a vector object
        _x=int(self._x[:-1])-int(_vector._x[:-1])
        _y=int(self._y[:-1])-int(_vector._y[:-1])
        _z=int(self._z[:-1])-int(_vector._z[:-1])
        
        return Vector(_x,_y,_z)

    
    def __mul__(self,_vector):                    #multiplying two vectors component wise 
        _x=int(self._x[:-1])*int(_vector._x[:-1])
        _y=int(self._y[:-1])*int(_vector._y[:-1])
        _z=int(self._z[:-1])*int(_vector._z[:-1])
        
        return Vector(_x,_y,_z)
    
    def __str__(self):                              #defing its __str__() for  customising its printing.
        return self._x + " + " + self._y+ "+ " + self._z
    def total_objects(self):
        return Vector.count
    def get_x(self):
        return self._x[:-1]   
    def get_y(self):
        return self._y[:-1]    
    def get_z(self):
        return self._z[:-1]    

vector_1=Vector(input("x component :"),input("y component: "),input("z component:"))  #declaring two vectors 
print("vector 1 :",vector_1)
print("x component is",vector_1.get_x())

print("y component is",vector_1.get_y())

print("z component is",vector_1.get_z())
vector_2=Vector(input("x component :"),input("y component: "),input("z component:"))
print("vector 2 :",vector_2)

print("x component is",vector_1.get_x())

print("y component is",vector_1.get_y())

print("z component is",vector_1.get_z())
print("addition of v1 and v2 ",vector_1+ vector_2)
print("substraction  of v1 and v2 ",vector_1- vector_2)
print("multiplication of v1 and v2 ",vector_1*vector_2)
print("number of objects ",vector_1.total_objects())
