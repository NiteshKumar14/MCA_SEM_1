class Date :

    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    @property
    def day(self):
        print("getter of day")
        return self._day
    @property
        
    def month(self):
        return self._month
    @property

    def year(self):
        print("getter of year")
        return self.year
    @day.setter
    def day(self,day):
        self._day=day
    @month.setter 
    def month(self,month):
        self._month=month   

    @year.setter 
    def year(self,year):
        self._year=year

    def __str__(self):
        return "DD :"+str(self.day) + "MM"+str(self.month) + "YYYY"+str(self.year)    


class Employee:
    count=0
    def __init__(self,name,date_of_hiring,salary):
        self.name=name
        self.date_of_hiring=date_of_hiring
        self.salary=salary
        Employee.count+=1
    def __str__(self):
        return "name:"+str(self.name)+"\ndate_of_hiring:"+str(self.date_of_hiring)+"\nsalary:"+str(self.salary)    

em=Employee("anme","1:2:1999",2000)
print(em)
print(em.count)
date1=Date(12,12,1999)
print(date1)
