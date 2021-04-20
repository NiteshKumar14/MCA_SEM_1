'''
***********************
find_pair function 
operation: first two  argments as pair(x,y) and finds them in third argument(list_Pairs) 
input:two numbers and one dictionary
output:True (if found ) else False (not found )
***********************
'''

def find_pair(numbers,others,list_pairs):
    found=False
    for keys in list_pairs.items():
        if keys[0]==numbers or keys[1]==numbers:
            # print("keys :",keys)
            found=True 
    return found
'''
***********************
isPrime function
operation: checks wether a number is prime or not
input:
output:
***********************
'''


def isPrime(integers_array,prime_numbers=[]):
    
    
    for number in integers_array:
        flag=True
        for numbers in range(2,int(number**0.5)+1):
            if number%numbers==0:
                flag=False
        if flag and number!=1:
            prime_numbers.append(number)
            
    
    return prime_numbers



def even_odd(integers_array,even=[],odd=[]):
    for numbers in integers_array:
        if numbers%2==0:
            even.append(numbers)
        else:
            odd.append(numbers)    
    return even,odd


def pairSumNumber(n,m,list_pairs={}):
    for numbers in n:
        # print("n : ",numbers)
        for others in n:
            # print("others: ",others)                
            if (others+numbers)==m and  not find_pair(numbers,others,list_pairs):
                    list_pairs[numbers]=others
    return list_pairs                




upper_bound=int(input("enter range end like 1-n enter value of n ="))
integers_array=[i for i in range(1,upper_bound+1)]
print("integers array ",integers_array)
prime_list=isPrime(integers_array)
print("prime numbers between 1-",upper_bound,' : ',prime_list,"\ntotal number of prime numbers from 1 to ",upper_bound," are ",len(prime_list))
print("even : odd between given range",even_odd(integers_array))
n=int(input("value of n: "))
integers_array=[int(input()) for x in range(n)]
print("numbers are :",integers_array)    
m=int(input("m ="))
pairs=pairSumNumber(integers_array,m)
count=1
size=len(pairs.keys())
for items in pairs.items():
        if(count!=size):
            print(list(items)," and ",end='')
        else:
            print(list(items),end='')
        count+=1
