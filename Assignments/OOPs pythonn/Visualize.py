import random
import matplotlib.pyplot as plt
import numpy as np
# creating data  randomly structure Student Name,Roll_No,Maths,Science,Social_Science,EVS,Music,Fav\n
def fetch(number_of_records):
    string=""         
    for students in range(1,number_of_records+1):
        string+="Student_"+str(students)+","+str(students)+","
        for subjects in range(5):
            string+=str(random.randrange(33,101))
            if(subjects!=4):
                string+=","
            
            else:
                string+=","+str(random.randrange(0,5))
                string+=",\n"
    return string

# to process data
# fetch subject wise marks 

def process_data(data):
    data_set=[]
    hashmap={"Name":[],"Roll_no":[],"Maths":[],"Science":[],"Social_Science":[],"EVS":[],"Music":[],"Fav":[]}

    lines=data.split("\n")
    print("newline ",lines)
    lines.pop()
    for students in lines:
        students=students.split(",")
        students.pop()
        #print(students)
        hashmap["Name"].append(students[0])
        hashmap["Roll_no"].append(students[1])
        hashmap["Maths"].append(int(students[2]))
        hashmap["Science"].append(int(students[3]))
        hashmap["Social_Science"].append(int(students[4]))
        hashmap["EVS"].append(int(students[5]))
        hashmap["Music"].append(int(students[6]))
        hashmap["Fav"].append(int(students[7]))
        
    return hashmap
def show_records(format_content,**attributes):
    # printing title 
    var="Student Name,Roll_No,Maths,Science,Social_Science,EVS,Music,Fav,"
    var=var.split(",")
    var.remove('')
    #print("var ",var)
    format_content=format_content.split("\n")
    format_content.pop()
    for titles in var:
        print(titles,"|",end='')
    print("")
    values=format_content
    if("bound" in attributes.keys()):

        start_index=attributes["bound"][0]
        end_index=attributes["bound"][1]
        while(start_index not in range(1,len(records["Maths"]))):
            start_index=int(input("enter a valid start index "))
        while(end_index not in range(1,len(records["Maths"]))):
            end_index=int(input("enter a valid end index "))
        values=values[start_index:end_index+1]    
    
    #print("format",format_content)
    length=[0]*len(var)
    for i in range(len(var)):
           length[i]=len(var[i])
    for lines in range(len(values)):
           
             
        texts=values[lines].split(",")
        texts.remove('')
        for elements in range(len(texts)):
           
            
            print(texts[elements]+" "*(length[elements]-len(texts[elements])+1)+"|" ,end='')
            
        print("")   



def subject_highest(records,**attributes):
    highest_marks={"Maths":[],"Science":[],"Social_Science":[],"EVS":[],"Music":[]}
    start_index=0
    end_index=len(records["Maths"])
    print("end index ",end_index)
    if("bound" in attributes.keys()):
        
        start_index=attributes["bound"][0]
        end_index=attributes["bound"][1]
        while(start_index not in range(1,len(records["Maths"]))):
            start_index=int(input("enter a valid start index "))
        while(end_index not in range(1,len(records["Maths"]))):
            end_index=int(input("enter a valid end index "))

    for keys in records.keys():
        
        if keys=="Name" or keys=="Roll_no" or keys=="Fav":
            continue
        max=0
        for index in range(start_index,end_index):
          # print("::",records[keys][index],"::",max)
            if(records[keys][index]>max):
                highest_marks[keys]=[]
                highest_marks[keys].append(index)
               # print("list ",highest_marks[keys])
                max=int(records[keys][index])
            
            elif(records[keys][index]==max):
                highest_marks[keys].append(index)
                #print("list ",highest_marks[keys])
            
    return highest_marks            



def plot_subject_marks(records,student_name):
    subjects=[]
    marks=[]
    index=int(student_name.split("_")[1])
    print("index ",index)
    # student found or not 

    for keys in records.keys():
        if keys in "Name_Roll_noFav":
            continue
        marks.append(records[keys][index-1])
        subjects.append(keys)
    y=np.array(marks)
    x=np.array(subjects)
    plt.bar(x,y,width=0.1)
    plt.show()



def fav_subjects(record):
    freq=[0]*5
    for favs in record["Fav"]:
        #print("fav :",favs)
        freq[favs]+=1
    #print(freq)     
    y=np.array(freq)
    subjects=["Maths","Science","Social Science","EVS","Music"]
    plt.title("PiE CHART")
    plt.pie(y,labels=subjects)
    plt.legend(title="Five Subjects")
    plt.show()



    


no_of_records=int(input("enter number of data to fetch random number "))        
data=fetch(no_of_records)
records=process_data(data)
show_records(data)
print(subject_highest(records))

plot_subject_marks(records,"Student_10")
fav_subjects(records)