def one():
# Exercises: Level 1
    # 1. Create an empty tuple
    emptytuple = ()

    #2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
    # These are fake names 
    brothers = ('Larry', 'Kevin', 'Alphonso', 'Ron')
    sisters = ('Kimberly', 'Milagros', 'Marilyn', 'Joyce')

    #3. Join brothers and sisters tuples and assign it to siblings
    siblings = brothers + sisters

    #4. How many siblings do you have?
    print(f'I have {len(siblings)} siblings.')

    #5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
    siblings +=  ('Robert', 'Trista')
    family_members = siblings

# Exercises: Level 2
    #1. Unpack siblings and parents from family_members
    
    print(type(family_members))
    siblings = family_members[0:8]
    parents = family_members[8:10]
    print(parents, siblings)


def two():
    #2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
    fruits = ('apple', 'banana', 'cherry', 'avocade', 'strawberry')
    vegetables = ('carrot', 'broccoli', 'spinach', 'zucchini', 'kale')
    animal_products = ('beef', 'chicken', 'egg', 'milk', 'honey')

    #3. Change the about food_stuff_tp tuple to a food_stuff_lt list
    food_stuff_tp = fruits + vegetables + animal_products
    food_stuff_lt = list(food_stuff_tp)
    print(food_stuff_lt) 
    print(type(food_stuff_lt))

    #4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
    first_half = food_stuff_lt[:len(food_stuff_lt)//2]
    second_half = food_stuff_lt[len(food_stuff_lt)//2:]
    if len(food_stuff_lt)%2 == 0:
        print(f'The two middle items are {first_half[-1]} and {second_half[0]}')
    else:
        print(f'The middle item is {first_half[-1]}')
    
    #5. Slice out the first three items and the last three items from food_stuff_lt list
    print(food_stuff_lt[:3])
    print(food_stuff_lt[-3:])
    #6. Delete the food_stuff_tp tuple completely
    del food_stuff_tp
    #7. Check if an item exists in tuple:
    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    
    #Check if 'Estonia' is a nordic country
    cunt = input("Enter a country: ").title()
    if cunt in nordic_countries:
        print(f'{cunt} is a nordic country')
    else:
        print(f'{cunt} is not a nordic country')
