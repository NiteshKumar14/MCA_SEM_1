"""
Student data Creation using random function 
where marks are randomly generated between 33 to 100
and student names are based on number provided by user
"""
import random
def fetch(number_of_records):
    string="Student Name,Roll_No,Maths,Science,Social_Science,EVS,Music,\n"         
    for students in range(1,number_of_records+1):
        string+="Student_"+str(students)+","+str(students)+","
        for subjects in range(5):
            string+=str(random.randrange(33,101))
            if(subjects!=4):
                string+=","
            else:
                string+=",\n"
    return string







"""
1.generate 10 students names with marks in 5 subjects
"""


record=fetch(int(input("enter number of students to generate test data ")))
"""
trying to open file Students\Student_records\Student_record.txt if it exits then we gonna simply write the record generated 
else
we will create a file for the same using 'x' mode in open function
And then finally we gonna read its content 
"""
import os
try:
    if not os.path.exists("Students/Student_records/"):
        os.makedirs("Students/Student_records/")
    file=open("Students\Student_records\Student_record.txt",'x')
        # print("generated data :\n",record)
    file.close()
    file=open("Students\Student_records\Student_record.txt",'w')
    file.write(record)
    print("contents in files:\n",file.read())
except:
       file=open("Students\Student_records\Student_record.txt",'w')
    #    print("generated data :\n",record)
       file.write(record)
       file.close()
       file=open("Students\Student_records\Student_record.txt",'r')
       format_content=str(file.read()).split("\n")
       format_content.pop()
    #    print("format",format_content)
       
       var=format_content[0].split(",")
       length=[0]*len(var)
       for i in range(len(var)):
           length[i]=len(var[i])
    #    print("length",length)   
       for lines in range(len(format_content)):
           
             
           texts=format_content[lines].split(",")
           texts.remove('')
           for elements in range(len(texts)):
               if lines==0:
                   print(texts[elements]+"|",end='')
               else:
                   print(texts[elements]+" "*(length[elements]-len(texts[elements]))+"|" ,end='')
               
           print("")   


finally:
    file.close()
    


"""

generate marksheets of each student students 
"""    
"""
Maths,Science,Social Science,EVS,Music

"""
file=open("Students\Student_records\Student_record.txt",'r')                 
record=str(file.read())
# print("record:",record)
Student_data={}
attributes=record.split("\n")           #by fetching each line of student record roll no wise 
attributes.remove('')

# print("attribtes:",attributes)
# for lines in file:

list_heading=attributes[0].split(",")       #extracting the heading part 
first_one=attributes[1].split(",")          #extracting the first record and setting it to the highest marks initially 

highest_marks={x:first_one[x] for x in range(2,len(list_heading)-1)}
# print("highest",highest_marks)




print("list:",list_heading)
dict_subject={2:[],3:[],4:[],5:[],6:[]} #saving the names of highest scoring students

for lines in range(len(attributes)):
    
    
    if(lines==0 ):
        continue
    student_info="::::Marksheet ::::\n"
    entries=attributes[lines].split(",")
    entries.remove('')
    print("ent",entries)
    # print(len(entries))
    for marks in range(2,len(entries)):
        # print("entries:",entries[marks])
        # print("higehst",highest_marks[marks])
        # print("marks",marks)
        # print(int(entries[marks]),":::",int(highest_marks[marks]))
        if(int(entries[marks]) == int(highest_marks[marks]) ):
            # print("swapped")
            # print("equal")
            dict_subject[marks].append(entries)
            # print(dict_subject[marks])
        elif(int(entries[marks]) > int(highest_marks[marks]) ):
            # print("swapped")
            dict_subject[marks]=[]
            dict_subject[marks].append(entries)
            highest_marks[marks]=entries[marks]
            # print("diciici",dict_subject)
    for items in range(len(entries)):
        student_info+=list_heading[items]+":"+entries[items]+"\n"
        
    try:
        if not os.path.exists("Students\Marksheets\ "):
            os.makedirs("Students\Marksheets\ ")
        file=open("Students\Marksheets\ "+entries[0]+"_"+entries[1]+".txt","x")
        print("file not found creating a new one"+entries[0]+"_"+entries[1]+".txt")
    except:
       print("file found opening ....")
    finally:
        file.close()
        file=open("Students\Marksheets\ "+entries[0]+"_"+entries[1]+".txt","w")
        print("generating marksheet"+entries[0]+"_"+entries[1]+".txt")
        file.write(student_info)
        file.close()
        

subject_wise=""
for keys in dict_subject:
    subject_wise+="\nSUBJECT NAME:"+list_heading[keys]+"\n"
    for i in range(len(dict_subject[keys])):
        if(i==0):
            subject_wise+="MARKS:"+dict_subject[keys][0][keys]+"\n"
            subject_wise+="Student Names:\n"
        subject_wise+=dict_subject[keys][i][0]+"\n"    


try:
    if not os.path.exists("Students\ topper_subject_wise\ "):
            os.makedirs("Students\ topper_subject_wise\ ")

    file=open("students\ topper_subject_wise\subject_wise_highest.txt","x")
    file.write(subject_wise)
except:
    file=open("students\ topper_subject_wise\subject_wise_highest.txt","w")
    file.write(subject_wise)
finally:
    
    file.close()
    file=open("students\ topper_subject_wise\subject_wise_highest.txt","r")
    print("\nsubject wise highest Marks::\n",file.read())
    file.close()
# for key,value in dict_subject.items():
#     print("\n",key,"::")
#     for i in value:
#         print(i)
    
print("check Student folder for all information in your current directory ")

         



