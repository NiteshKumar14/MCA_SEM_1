def recur_length(string,count):
    print(string)
    print(count)
    if string=='':
        print("ye")
        return count
    return recur_length(string[count:],count+1)    


string=input()
print(recur_length(string,0))
import matplotlib.pyplot as plt
import numpy as np

def read_text():
    shapes=[]
    with open("sorted.txt","r") as my_file:
        shapes=my_file.read().split("\n")
        return shapes

# print(shapes)
def plot_histo():
    dimensions=[]
    for items in shapes:
        dimensions.append(items.split(" "))
        print("dimensions: \n",dimensions)
        

volumes=[]
cuboids=0
cones=0
temp_volume=1
for objects in dimensions:
    temp_volume=1
    if(not objects[0]  in "CuboidCone"):
        continue
    if objects[0]=="Cuboid":
        for i in range(1,len(objects)):
            
            temp_volume=temp_volume*int(objects[i])
        volumes.append(temp_volume)
    if objects[0]=="Cone":
        cones+=1    

print("volume: ",volumes)
print("cones",cones)

x=np.array(volumes)

cuboids=len(volumes)
plt.hist(x,bins=10)
plt.show()
pie_chart=[]
pie_chart.append(cuboids)
pie_chart.append(cones)
x=np.array(pie_chart)
plt.pie(x,labels=["cuboids="+str(cuboids),"cones="+str(cones)])
plt.show()

