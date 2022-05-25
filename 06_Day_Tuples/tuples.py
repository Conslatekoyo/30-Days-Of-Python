# Create an empty tuple
empty_tuple=()
print(empty_tuple)
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters_and_brothers=("Joanna","Mary","Serah","Jenipher")
print(sisters_and_brothers)
# Join brothers and sisters tuples and assign it to siblings
brothers=("James","John")
sisters=("Judith","Jackline")
siblings=brothers+sisters
print(siblings)
# How many siblings do you have?
count=len(siblings)
print(count)
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
new_list=list(siblings)
print(new_list)
add1=["Benta","Sam"]
add2=new_list.append(add1)
print(add2)

# Exercises: Level 2
# Unpack siblings and parents from family_members
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=("mango","apples")
vegetables=("broccoli","cabbage")
animal_products=("cheese","ghee")
addition=fruits+vegetables+animal_products
print(addition)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp=("sausage","croissant","rice","chicken","beef","salads")
food_stuff_lt =list(food_stuff_tp)
print(food_stuff_lt)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[0:6:2])
# Slice out the first three items and the last three items from food_staff_lt list
# Delete the food_staff_tp tuple completely
del food_stuff_lt
# Check if an item exists in tuple:
print('orange' in food_stuff_lt)
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')


def brothersSister(names):
    print (names)

brothersSister(names=("Joanna","Mary","Serah","Jenipher"))