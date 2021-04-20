class Student:
    def __init__(self,*vargs):
        self.__name=vargs[0]
        self.__roll_no=vargs[1]
        self.__age=vargs[2]
        # self.__subjects=list(vargs[2:])
        # if(len(self.__subjects)<5):
        #     self.__subjects+=[0]*(5-len(self.__subjects))

    def __str__(self):
        return "Name :"+self.__name+"\n Roll_no:"+str(self.__roll_no)+"\n age:"+str(self.__age)  
        
    # def percent(self):
    #     x=0
    #     for subjects in self.__subjects:
    #         x+=subjects
    #     return float(x)/5
    # def get_subjects(self):
    #     return self.__subjects
    # def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no    
    # def get_disc(self):
    #     desc=[]
    #     desc.append(self.__name)
    #     desc.append(self.__roll_no)
    #     desc+=self.__subjects
    #     return desc
