"""
Write a Python program that reads a text file called "data.txt" and counts the number of lines in the file.
"""
i = 0
with open ('data.txt') as f:
    for line in f:
        i = i+1

print(i)