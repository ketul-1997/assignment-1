def delete(word, n):  
      x = word[:n]   
      y = word[n+1:]  
      return x + y

print(delete("hello", 0))
