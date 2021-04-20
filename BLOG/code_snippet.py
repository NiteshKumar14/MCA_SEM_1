

variable_1=12.09
variable_2=10
print("variable_1:",type(variable_1))
print("variable_2:",type(variable_2))
print("variable_1:i am now a integer haha ",int(variable_1))
print("variable_2:i am now a floating point number  haha ",float(variable_2))


# why we need it

name="abc"
roll_no="20"
pincode="220001"
marks_in_maths="90"
total_marks=0
print(type(marks_in_maths))
total_marks+=marks_in_maths



# implicit type conversion
print("variable_1:",type(variable_1))
print("variable_2:",type(variable_2))
sum=variable_1+variable_2
print("sum:",sum,"\t type",type(sum))
# float+int=float


# explicit type conversion

print("variable_1:",type(variable_1))
print("variable_2:",type(variable_2))
sum=int(variable_1)+variable_2
print("sum:",sum,"\t type",type(sum))
