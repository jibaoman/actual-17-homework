mylist = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,444,111,3333,4,5,777,65535,45,5001,33,45,6000]

mx_num_1=0
mx_num_2=0

for i in mylist:
    if i > mx_num_1:
        mx_num_1 = i
    if i < mx_num_1 and i >mx_num_2:
        mx_num_2 = i
    
print 'the max  number is %s'%(mx_num_1)
print 'the secend max_number is %s'%(mx_num_2)

