# #In python the % is used in string formatting
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
from os import remove


print('Thirty', 'Days', 'Of', 'Python')
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print( 'Coding', 'For' , 'All' )
# Declare a variable named company and assign it to an initial value "Coding For All".
company="Coding For All"
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[1:])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding"in company)
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding","python"))
# Change Python for Everyone to Python for All using the replace method or other methods.
first="Python for Everyone"
print(first.replace("Everyone","All"))
# Split the string 'Coding For All' using space as the separator (split()) .
print("Coding For All".split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
big_five="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(big_five.split(", "))
# What is the character at index 0 in the string Coding For All.
code="Coding For All"
print(code[0])
# What is the last index of the string Coding For All.
print(code[-1])
# What character is at index 10 in "Coding For All" string.
print(code[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym='Python For Everyone'
print(acronym[0]+acronym[7]+acronym[11])
# Create an acronym or an abbreviation for the name 'Coding For All'.
abbr='Coding For All'
print(abbr[0]+abbr[7]+abbr[11])
# Use index to determine the position of the first occurrence of C in Coding For All.
print(abbr.index('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(abbr.index('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(abbr.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
x= 'You cannot end a sentence with because because because is a conjunction'
print(x.index('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(x.rindex('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(x[0:-1:31])
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(x.find('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(x.strip('because'))
# Does ''Coding For All' start with a substring Coding?
print(abbr.startswith('Coding'))
# Does 'Coding For All' end with a substring coding?
print(abbr.endswith('Coding'))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
remove='   Coding For All     '
print(remove.strip(" "))
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython 
print("30DaysOfPython".isidentifier())
# thirty_days_of_python
print("thirty_days_Of_python".isidentifier())
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
one= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(one))
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
print('I\nam \nenjoying \nthis\nchallenge')
# I just wonder what is next.
print('I \njust \nwonder \nwhat \nis \nnext')
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
print( 'Name     Age     Country   City.remove(" ")')
# Asabeneh  250     Finland   Helsinki
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# Make the following using string formatting methods 
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144