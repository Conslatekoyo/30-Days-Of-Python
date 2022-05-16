# Create an empty dictionary called dog
# from turtle import color
dog={}
print(dog)
# Add name, color, breed, legs, age to the dog dictionary
dog['color']='brown'
dog['legs']=4
dog['age']=6
dog['name']='Yugo'
dog['breed']='German_Sheperd'
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={}
student['first_name']='Teresa'
student['last_name']='Umuhoza'
student['gender']='female'
student['age']=24
student['marital_status']='single'
student['skills']='analytical_skills'
student['country']='Rwanda'
student['City']='Kigali'
student['address']='616_Korongo_rd'
print(student)
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
skills=student.values()
print(skills)
print(list(student))
# Modify the skills values by adding one or two skills
# student=['skills']= 'python','SQL'
print(student)
# Get the dictionary keys as a list
print(dict(student))
print(student.keys())
# Get the dictionary values as a list
skills=student.values()
# Change the dictionary to a list of tuples using items() method
print(tuple(student))
# Delete one of the items in the dictionary
# Delete one of the dictionaries
del student
print(student)