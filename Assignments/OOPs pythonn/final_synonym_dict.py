'''
defining fuction synonym_iteration:
    
    input : Synonym Dictionary
    operation: iterates my_dict and stores same meaning word in a dict(Synonym_dict)


'''





def synonym_iteration(synonym_dict):          
    for words,meanings in my_dict.items():              #itertaing words and meaning in my_dict 
        if key_found(meanings,synonym_dict):            #checking if meaning already exists then append the words 
            synonym_dict[meanings].append(words)
        else:                                           #else create entry of new word with its meaning as key
            synonym_dict[meanings]=list()
            synonym_dict[meanings].append(words)    

def synonym_recursion(my_dict,synonym_dict):            #using recursion performing the same task 
    if my_dict=={}:                                     #terminating conditions when dictionar gets empty
        return
    else:                                                
                                                        #pop my dict key:value pair
        key_value=my_dict.popitem()                     #if key found append in list
        if key_found(key_value[1],synonym_dict):
            synonym_dict[key_value[1]].append(key_value[0])
        else:
            synonym_dict[key_value[1]]=list()           #else create entry of new word with its meaning as key    
            synonym_dict[key_value[1]].append(key_value[0])
        synonym_recursion(my_dict,synonym_dict)    

def display(dict):                              #A simple display function to display a dictionary
    for x,y in dict.items():
        print(x,"\t\t\t",y)
def key_found(key,dict):                         #return true if a key is found in the dictionary else false
    
    for keys in dict.keys():
        if keys==key:
            return True
    return False
def insert_into_dictionary(dict):
                                                #Insert function to insert values in my_dict if needed 
    
    choice="y"              
    while( choice=='y'):                        #until user inputs y keep on adding items in my_dictionary
        print("Words : Meaning")
        word=input()
        print(":",end='')
        meaning=input()
        my_dict[word]=meaning
        print("want to add more press y or else n")
        choice=input()
print("hello MR.X \n just enter number of words then follow the format. \n you are good to go \n we will take care of your synonym diary ")


my_dict={                                       #defining my_dict with some items 
    "Depressed":"Sad",
    "Dejected":"Sad",
    "Heavy":"Sad",
    "Amused":"Happy",
    "Delighted":"Happy",
    "Pleased":"Happy",
    "Annoyed":"Angry",
    "Agitated":"Angry",
    "Mad":"Angry",
    "Determined":"Energized",
    "Creative":"Energized",
}
print("your my dictionary ")
print("word\t\t\tMeaning")

display(my_dict)                            #using display function to print items in my_dict 
#printing my dictionary

print("wanna add more ")                    #asking user y or no for inserting additional items to my_dict
decide=input("y/n\n")
if(decide=="y"):
    insert_into_dictionary(my_dict)
    print("after adding new ones ")
    display(my_dict)


#create a synonym dictionary
synonym_dict={}
decide=input("Recursion press (r) or  for iteration(i):")
if decide=='r':                             #creating an empty synonym_dict 
    synonym_recursion(my_dict,synonym_dict)     #calling recursion function to perform the automation of creating of synonym dictionary
else:
    synonym_iteration(synonym_dict)           #calling itertaion one 
print("synonym dict")                          #printing synonym dictionary 

iterator=1                                          
print("Page\t\t\tMeaning\t\t\tSynonymns")         
for keys,values in synonym_dict.items():
    print(iterator,"\t\t\t",keys,"\t\t\t",end='')
    for words in values:
        print(words," ",end='')
    print("")    
    iterator+=1

