#Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
string = "12345@@@GpErI"

count_capital = 0
count_lower = 0
count_digit = 0
count_specialchar = 0

for i in string:
        if(i.isupper()):
                count_capital += 1
        elif(i.islower()):
                count_lower += 1
        elif(i.isdigit()):
                count_digit += 1
        else:
                count_specialchar += 1
print"the number of capital letters are  :", count_capital
print "the number of lower letters are  :" ,count_lower
print"the number of digits  are  :",  count_digit
print"the number of  specialcharacter are  :" , count_specialchar
