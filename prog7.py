#Write a Python program to remove the characters which have odd index values of a given string.

def odd_even(str):
        updated_str= ""
        for i in range(len(str)):
                if i%2==0:
                 updated_str=updated_str + str[i]
        return updated_str
        

print odd_even("ketul")
