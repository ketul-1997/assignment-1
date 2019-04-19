import textwrap

str = '''21.21. Slovak ................................................................................................. 166
21.22. Spanish ............................................................................................... 166
21.23. Swedish ............................................................................................... 167
21.24. Turkish     '''

text_without_prefix = textwrap.dedent(str)
print()
print(text_without_prefix)
print()


text_with_prefix = textwrap.indent(str,'>')
print()
print(text_with_prefix)
print()

