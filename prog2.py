string = "google.com"
value = { }
for i in string:
        if value.get(i):
                value[i] = value[i] + 1
                
        else:
                value[i] = 1
print value

