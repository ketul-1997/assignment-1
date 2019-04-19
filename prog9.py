#Write a Python function to reverses a string if it's length is a multiple of 4.

def reverse_str(string):

        new_str = ""
        for i in range(len(string)):
                if i%4==0:
                        new_str = new_str + string[i]
        return new_str
        
print reverse_str("thiruvandapuram")

