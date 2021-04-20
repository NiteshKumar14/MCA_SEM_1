def list_insert(string ,listt=[]):
    # print("data type \n 1.int \n2.string \n ")
    print(string)
    if string=="":
        return "",listt
    
    if  string[0]=="]":                                                # if input is closing  brackets then its means current list has ended 
        print("] closing mila ")
        return string[1:],listt
    
    if string[0]=="[":                                                # if its a opening brackets then simply create a list and call for that too and append its value in the current list 
        print("[ opening mila ")
        new_list=list()
        string,new_list=list_insert(string[1:],new_list)
        print("new list",new_list)
        listt.append(new_list)
        print("after new list completion:",len(string),":",string)
        return list_insert(string,listt)
    else:                                                        # if its not string that means an integer value  
        listt.append(int(string[0]))                                      # append that in the list 
        return list_insert(string[1:],listt)                                       #simply return to the list 


def flatten_list(listt,out=[]):                         #performs:it flattens the list recursively by checking elements type 
    # print("out : ",out)
    # print("list : ",listt)
    if listt==[]:                                       #terminating condition if list is empty 
       return out
    else:
        try:                                            #if its list perform the same operation recursively
                                                        #else append in out list 
            element=listt[0]
            print("element : ",element)
            if type(element)!=type(list()):
                out.append(element)
            else:
                return flatten_list(element,out)
        except:
            print("not a list")
            out.append(element)
        finally:
            return flatten_list(listt[1:],out)          #call the function again with list excluding its first element 
string=input(";")
print(string)
string,number_list=list_insert(string)
print("list :\n",number_list)
print("after flattening:\n",flatten_list(number_list))

def list_insert(listt,var=0):
    # print("data type \n 1.int \n2.string \n ")

    var,data_type=map(str,input("element type : ").split(" "))  #taking two value as element and its type 

    if var=="]":                                                # if input is closing  brackets then its means current list has ended 
        # print("] closing mila ")
        return listt
    
    if var=="[":                                                # if its a opening brackets then simply create a list and call for that too and append its value in the current list 
        # print("[ opening mila ")
        new_list=list()
        listt.append(list_insert(new_list))
    else:                                                        # if its not string that means an integer value  
      
        if data_type!="s":
            listt.append(int(var))
        else:
            listt.append(var)                                      # append that in the list 
    return list_insert(listt)                                       #simply return to the list 

