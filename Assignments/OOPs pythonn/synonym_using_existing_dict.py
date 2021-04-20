# create an empty my_dictionary
my_my_dict={
    "sad":"sure",
    "depressed":"Sad",
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
def display(dict):
    iterator=1
    for keys,values in dict.items():    
    print(iterator,"\t\t",keys,"\t\t",values)
    iterator+=1


def key_found(key):
    
    for k in my_dict.keys():
        if k==key:
            return True
    return False
# def display(my_dict):
#     for k in my_dict.keys():
#         print(k,"type ",type(k))
# print("hello MR.X \n just enter number of words then follow the format. \n you are good to go \n we will take care of your synonym dairy ")


my_dict={}

#input number of words with their coreesponding meaning 
no_of_words=int(input("Number of words: "))

#creating a my_dictionary with key as meaning and values as list of words 
print("enter in format words : meaning")
#loop until all words are entered 
while(no_of_words):
    word=input()
    meaning=input(":")
    #display(my_dict)
    #if my_dict is empty:
    if key_found(meaning):
        #print("key found")
        my_dict[meaning].append(word)
        #display(my_dict)
        
    else:
        my_dict[meaning]=list()
        my_dict[meaning].append(word)
        display(my_dict)
    no_of_words-=1    
iterator=1
print("Page\t\tMeaning\t\tSynonymns)")
