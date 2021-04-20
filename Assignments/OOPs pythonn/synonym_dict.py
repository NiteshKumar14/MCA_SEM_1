# create an empty dictionary
def key_found(key):
    
    for k in dict.keys():
        if k==key:
            return True
    return False

print("


dict={}

#input number of words with their coreesponding meaning 
no_of_words=int(input("Number of words: "))

#creating a dictionary with key as meaning and values as list of words 
print("enter in format words : meaning")
#loop until all words are entered 
while(no_of_words):
    word=input()
    meaning=input(":")
    #display(dict)
    #if dict is empty:
    if key_found(meaning):
        #print("key found")
        dict[meaning].append(word)
        #display(dict)
        
    else:
        dict[meaning]=list()
        dict[meaning].append(word)
        display(dict)
    no_of_words-=1    
iterator=1
print("Page\t\tMeaning\t\tSynonymns)")
for keys,values in dict.items():
    
    print(iterator,"\t\t",keys,"\t\t",values)
    iterator+=1