def binary_search(number,array):
    start=0
    end=len(array)-1    
    mid=(start+end-1)//2
    if number==array[mid]:
        return mid
    else:
        while (start-mid)!=1 :
            if(number>mid):
                start=mid
            else:
                end=mid
            for i in range(start,end+1):
                if array[i]==number:
                    return i
            return "not found"                     
def binary_search_optimized(number,array):
    start=0
    end=len(array)-1
    mid=(start+end-1)//2
    while(start<=end):
        if array[mid]==number:
            return mid
        if array[mid]<number:
            end=mid+1
        else:
            start=mid-1   
    return -1             




ele=int(input())
array=[0]*ele
for elements in range(len(array)):
    array[elements]=int(input())
print(array)
test_case=int(input("test case"))

while(test_case):
    number=int(input(":"))
    print(binary_search(number,array,))            
    test_case-=1

