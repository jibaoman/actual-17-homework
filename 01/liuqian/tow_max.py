#/usr/bin/env python
list1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,444,111,3333,4,5,777,65535,45,5001,33,45,6000]
max_num = list1[0]


for i in list1:
    if max_num < i:
       max_num = i

print max_num

j = 0         
while j < len(list1):
    if list1[j] == max_num:
       del list1[j]
    j = j + 1
print list1 

tow_max = list1[0]
for i in list1:
    if tow_max < i:
       tow_max = i
print tow_max

