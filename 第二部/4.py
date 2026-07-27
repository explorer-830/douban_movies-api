num_list=[]
for i in range(1,21):
    num_list.append(i**2)
print(num_list)
num2_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]
num3_list=[]
for a in num2_list:
    if a%2==0:
        num3_list.append(a**2)
print(num3_list)
num2_list.remove(2)
print(num2_list)
