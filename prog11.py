#Write a Python program to display formatted text (width=50) as output.

import textwrap
sample_text = '''"A Byte of Python" is a free book on programming using the Python language. It servesas a tutorial or guide to the Python language for a beginner audience. If all you knowabout computers is how to save text files, then this is the book for you. '''

print(textwrap.fill(sample_text, width=50))

