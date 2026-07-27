list1=[2,4,8,20,76,12,14]
list2=[1,14,54,7,33,11,14]
list3=list1+list2
print(list3)
new_list=[]
for i in list3:
    if i not  in new_list:
        new_list.append(i)
print(new_list)
list4=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list5=[]
for a in list4:
    if a%3==0 or a%5==0:
        list5.append(a)
print(list5)

