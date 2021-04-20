'''
Mr.GOOFY this is for you 
Encoding and Decoding messaging program


'''
def reverse(string,rev_string=""):
    # print("string ",string," rev ",rev_string)

    if string=="":                                  #terminating condition when string gets empty
        return rev_string
    else:
        # print(" after : ",string[:-1])
        return reverse(string[:-1],rev_string+string[-1])



number={1:'one',2:'two',3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

def encoding(message ,encoded_message=""):
    # print("message",message)
    length=len(message)
    for iterator in range(length):
        if ord(message[iterator])>=48 and ord(message[iterator])<=57:
            digit=int(message[iterator])
            in_words=number[digit]
            encoded_message+=reverse(in_words)+" "
        
        elif ord(message[iterator])>=65 and ord(message[iterator])<=90:  #upper case A-Z their ascii values 
            ascii_value=ord(message[iterator])
            encoded_message+=reverse(str(ascii_value))+" "
        elif ord(message[iterator])>=97 and ord(message[iterator])<=122: #lower case a-z #upper case A-Z their ascii values 
            ascii_value=ord(message[iterator])
            encoded_message+=reverse(str(ascii_value))+" "
        else:                                                             #its a special character 
            encoded_message+=message[iterator]+" "    

    return encoded_message    
number_w={'one':1,'two':2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

def decoding(message,decoded_message=""):
    message=message.split(" ")
    # message.remove('')

    # print("message",message)
    for items in message:
        found=number_w.get(reverse(items),"notFound")           #checking in dictionary if its exists in number_w then it will a integer 
        # print("found: ",found)
        if(found!="notFound"):
            decoded_message+=str(found)
        else: 
                ajeeb_character='\n'                     
                if items in  ajeeb_character or items=='':
                    # print("occured")
                    decoded_message+=items+" "
                    continue                             #else if its length is one then that means its a special character 
                word=reverse(items)
                if(len(word)==1):
                    # print("special ",word)
                    decoded_message+=word
                else:                                           #else its a alphabet 
                    # print("char",word)
                    # print("word: ",word)
                    decoded_message+=chr(int(word))
                
    return decoded_message


import time 
import os






# message=input("enter message to encode: ")
# encoded_message=encoding(message)
# print("encoded message: ",encoded_message)
# decoded_message=decoding(encoded_message)
# print("decoded message :",decoded_message)
# # print(ord("A"))
# print(chr(65))
file=open("message.txt",'r')        #opened the message file 
message=file.read() 

print("message: ",message)           #read the contents of the file 
encoded_message=encoding(message)
print("\nencoding..........")
time.sleep(6)
print("\nencoded message",encoded_message)
file=open("encoded_message.txt",'w')
print("\ncreated encoded message file :encoded_message.txt")
file.write(encoded_message)
file.close()
file=open("encoded_message.txt",'r')
time.sleep(2)
print("\ncontents of encoded_message.txt\n",file.read())

file.close()
file=open("decoded_message.txt",'w')
print("\ncreated decoded message file :decoded_message.txt")
print("\ndecoding ....")
time.sleep(10)
file.write(decoding(encoded_message))
file.close()
file=open("decoded_message.txt",'r')
print("\nreal message :\n\n",file.read())
file.close()


print('Hey',end='')

for i in range(4):
    print('\b',end='')
print("how is your day?")    



