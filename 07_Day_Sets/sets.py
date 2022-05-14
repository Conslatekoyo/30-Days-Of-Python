
# # sets
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 1
# Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
# Add 'Twitter' to it_companies
add=it_companies.add('twitter')
print(add)
# Insert multiple IT companies at once to the set it_companies
multiple_it_companies={'Andela',"Yoco","Skygarden","Softhub"}
print(it_companies.update(multiple_it_companies))
# Remove one of the companies from the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(it_companies.remove('Facebook'))
# What is the difference between remove and discard
print("The temove method raises an error when the item is not in the set whereas the discard method doesnt raise an error and the set remains intact")
# Exercises: Level 2
# Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
c=A.union(B)
print(c)
# Find A intersection B
print(A.intersection(B))
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
print(A.isdisjoint(B))
# Join A with B and B with A
print(A.union(B))
print(B.union(A))
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# Delete the sets completely
# print(del A)
# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(set(age))
# Explain the difference between the following data types: string, list, tuple and set
print("A string is a combinaton of different characters using double quotes")
print("A list is an ordered sequence of elements having square brackets")
print("A tuple is a set of ordered sequence of elements having round brackets")
print("A set is an immutable sequence of elements having curly braces")
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence="I am a teacher and I love to inspire and teach people."
print(sentence.split())