list = [1,2,3,4,5]

list2 = [','.join(str(i)) for i in list if i%2==0]
print list2
