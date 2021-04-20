
#reverse string taking string input 



def rev_string(__string__):
    
    length=len(__string__)-1                            
    # print("length: ",length)
    if not length:                              #edge case if string is null
        return ""
    __output__=""   
    while length:                               #iterating from end to start and appending it into output string
        # print("length ",length)
        __output__+=__string__[length]
        length-=1
    __output__+=__string__[0]                   #as loop halts at 0 so adding the last element 
    return __output__                           #returning the output 


'''
Task:
takes a string and returns number of words in it .
Approach : two pointer approach 

'''

def no_of_words(string):                        
    if not len(string):                 #edge case if string is empty 
        return 0    
    else:
        length=len(string)                              
        # print("len:",length)
        current_char=1                   #keeping track of current and previous character to pick words 
        previous_char=0
        word_count=0
        while current_char<length:
            # print("org: ",current_char)
            if (string[current_char]==" " and string[previous_char]!=" "):      #if current is space and previous is a non space then treat that as a word 
                # print("space encontered")
                word_count+=1
                while  current_char<length and  string[current_char]==" ":
                    current_char+=1
                    # print("ch: ",current_char)
                
            previous_char=current_char
            current_char+=1
            

    

    return word_count+1                                #returning word+1 as this approach considers senetence ends without space 


'''
Using ascii values determining which is vowels ,consonants or special character 
for vowels checking character to match any in (a,e,i,o,u )
for consonants ascii values between 65-122
if none of the above condition is met then that must be a special character 
'''

def count_character_types(__string__):
    dict={"vowel":0,"consonants":0,"special_characters":0}
    length=len(__string__)-1
    while length>=0:
        if (__string__[length]=='a' or __string__[length]=='e' or __string__[length]=='i' or __string__[length]=='o' or __string__[length]=='u'):
            dict['vowel']+=1
        elif(ord(__string__[length])>=65 and ord(__string__[length])<=122):
            dict['consonants']+=1
        else:
            dict['special_characters']+=1    
        length-=1
    return dict   


def rev_each_word(string):
    if not len(string):                         #using the same approach as in number of words just keepin track of each word using previous char 
        return ""
    else:
        output=""
        length=len(string)
        current_word=""
          # print("len:",length)
        current_char=1
        previous_char=0
        word_count=0
        while current_char<length:
            # print("org: ",current_char)
            current_word+=string[previous_char] 
            if (string[current_char]==" " and string[previous_char]!=" "):
                # print("space encontered")
                output+=rev_string(current_word)+" "
                current_word=""
                while  current_char<length and  string[current_char]==" ":
                    current_char+=1
                    # print("ch: ",current_char)
               
            previous_char=current_char
            current_char+=1
            
        if current_word!="":
            output+=rev_string(current_word+string[length-1])
    return output


def longest_word(string):                   #finds longest word by using space as a seprator and comparing their length 
                                            
    if len(string)==0:
        return string

    length=len(string)
    current_word=""
    current_max=""
    iterator=0
    count=0
    while  iterator<length:
        # print("iteration : ",iterator)
        if string[iterator]==" " or (length-iterator)==1 :
            # print("space encountered ")
            if len(current_word)>len(current_max):
                # print("current max : ",current_max)
                current_max=current_word
                # print("after modification current max :",current_max)
                count+=1
            current_word=""
        else:
            current_word+=string[iterator]
            # print("current word ",current_word)
        iterator+=1
    if(count==0):
        return string
    return current_max    









sentence=input("enter a sentence to find no of words in it: ")
print("Sentence : ",sentence)
print("Reverse : ",rev_string(sentence))
print("Reverse of each word ",rev_each_word(sentence))
print("no of words ",no_of_words(sentence))
print("character types :",count_character_types(sentence))
print("longest word :",longest_word(sentence))

"""
enter a sentence to find no of words in it: My name is Nitesh Kumar
Sentence :  My name is Nitesh Kumar
Reverse :   ramuK hsetiN si eman yM
Reverse of each word  yM eman si hsetiN ramuK
no of words  5
character types : {'vowel': 7, 'consonants': 12, 'special_characters': 5}
longest word : Nitesh
"""