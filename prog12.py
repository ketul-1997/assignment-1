#import textwrap

#str = '''            A Byte of Python" is a free book on programming using the Python language. It serves
#as a tutorial or guide to the Python language for a beginner audience. If all you know
#about computers is how to save text files, then this is the book for you.               

 #'''

#new_string= textwrap.dedent(str)
#print(new_string)

import textwrap
sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.dedent(sample_text)
print()
print(text_without_Indentation )
print()
