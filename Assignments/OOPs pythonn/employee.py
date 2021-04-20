class Employee:
    
    __name=None
    __emp_id=None
    __designationet =None
    __salary=None
    __exp=None
    
    # constructor
    
    def __init__(self,name,emp_id,designation,salary,exp):
        self.__name=name
        self.__emp_id=emp_id
        self.__designation=designation
        self.__salary=salary
        self.__exp=exp
    # getters

    def get_name(self):
        return self.__name
    def get_emp_id(self):
        return self.__emp_id
    def get_designation(self):
        return self.__designation
    def get_salary(self):
        return self.__salary
    def get_exp(self):
        return self.__exp

    # setters


    def set_name(self,name):
        self.__name=name
    def set_emp_id(self,emp_id):
        self.__emp_id=emp_id
    def set_designation(self,designation):
        self.__designation=designation
    def set_salary(self,salary):
        self.__salary=salary                
    def set_exp(self,exp):
        self.__exp=exp
    
    def show(self):
        print("name :",self.__name,"\nemp_id :",self.__emp_id,"\ndesignation :",self.__designation,"\nsalary :",self.__salary,"\nexperience :",self.__exp)
    
    def __str__(self):
        return "name :"+ str(self.__name)+"\nemp_id :"+str(self.__emp_id)+"\ndesignation :"+str(self.__designation)+"\nsalary :"+str(self.__salary)+"\nexperience :"+str(self.__exp)


    def calc_base_salary(self):
        base_salary=20000;
        if(self.__designation=="Worker"):
            base_salary=10000
        elif(self.__designation=="Supervisor"):
            base_salary=15000
        return base_salary    

    def calc_Addsal(self):
        return (self.__exp)*(self.calc_base_salary())/100
    def calc_HRA(self):
        return 0.05*(self.calc_base_salary())    
         
    def calc_total_salary(self):
        return self.calc_base_salary()+self.calc_Addsal()+self.calc_HRA()


emp_1=Employee("Nitesh",1,"Manager",20000,5)
print(emp_1)
print(emp_1.calc_total_salary())
print(emp_1.calc_base_salary())
print(emp_1.calc_Addsal())
print(emp_1.calc_HRA())