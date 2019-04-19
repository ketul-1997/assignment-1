string = "p y t h o n"
nospace = [i for i in string if i!=" "]
space  = len(string)-len(nospace)
result = " "*space
result = result + ''.join(nospace)
print result
