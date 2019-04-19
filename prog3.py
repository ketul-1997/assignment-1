str1 = 'abc'

str2 = 'xyz'

temp = 0

str3 = str1 + str2
print "the strring is \n" +str(str3)

def swap(temp,i,j):

	temp= temp.replace(j,'!')
	temp=temp.replace(i,j)
	temp=temp.replace('!',i)
	return temp

print swap(str3,"ab","xy")

