# Python dictionaries 

# Its also a datatype in python but it stores values in 
# a pair of key(like a word in the normal dictionary) and 
# value(as the meaning of that word in the normal dictionary)
# Duplicates are not allowed in a dictionary.

my_dictionary = {
    'name' : 'Tim',
    'age' : '20',
    'school': 'Unniversity of Buea',
    'Faculty': 'Engineering and Technology',
    'Department' : 'Software Engineering',
    'is_tall':True,
    'Quarter':' Clean South'
}



# value = int(input('Input a number: '))

# if value % 5  ==0:
#     print(value, 'can be divided by 5')
# else:
#     print(value, 'can not be divided by 5')
print(len(my_dictionary))



x = my_dictionary['Department']
print(x)