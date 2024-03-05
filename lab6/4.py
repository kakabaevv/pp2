#Write a Python program to count the number of lines in a text file.
import os

path = 'C:/Users/modik/Documents/pp2/Word.txt'
with open( path , 'r') as f:
    lines = f.readlines()
    print( len(lines) )
    