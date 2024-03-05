import re
txt = input()


#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
x = re.search('ab*', txt )


if x:
    print("true")

else:
    print("false")
print(x)