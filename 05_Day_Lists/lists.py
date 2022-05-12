# Declare an empty list
empty_list=[]
print(empty_list)
# Declare a list with more than 5 items
x=["oranges","mangoes","bananas","apples","pears","raspberries"]
print(x)
# Find the length of your list
print(len(x))
# Get the first item, the middle item and the last item of the list
print(x[0],x[3],x[-1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["Conslate",29,162,"single","616 Korongo rd"]
print(mixed_data_types)
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=[ "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle" "Amazon"]
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0],it_companies[3],it_companies[-1])
# Print the list after modifying one of the companies
it_companies[0]="sky garden"
print(it_companies)
# Add an IT company to it_companies
print(it_companies.append("Yoco"))
# Insert an IT company in the middle of the companies list
z=it_companies.insert("Ushaidi")
print(z)
# Change one of the it_companies names to uppercase (IBM excluded!)
# up=it_companies.upper()
# print(up)
# Join the it_companies with a string '#;  '
join=["#"]
c= it_companies+join
print(c)
# Check if a certain company exists in the it_companies list.
print("Ushahidi" in it_companies)
# Sort the list using sort() method
print(it_companies.sort())
# Reverse the list in descending order using reverse() method
print(it_companies.reverse())
# Slice out the first 3 companies from the list
print(it_companies[3:])
# Slice out the last 3 companies from the list
print(it_companies[0:3])
# Slice out the middle IT company or companies from the list

# Remove the first IT company from the list

# Remove the middle IT company or companies from the list

# Remove the last IT company from the list

# Remove all IT companies from the list

# Destroy the IT companies list

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
 back_end = ['Node','Express', 'MongoDB']
joining= front_end+back_end
print(joining)
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

# Exercises: Level 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
