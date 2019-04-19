num = [1,2,3,4,5,6,7,8,9,10]

odd= "-"
even= "-"
for i in num:

        if (i % 2 ==0):
               even = even.join(i)
        else:
                odd = odd.join(i)
print "even numbers are \n",even
print "odd numbers are\n",odd
