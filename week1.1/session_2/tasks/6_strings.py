# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") # prints the original string input
print(f"Modified String 1: {user_string.lower()}")
print(f"Modified String 2: {user_string.upper()}") # capitalises everything from the input
print(f"Modified String 3: {user_string.strip()}")
print(f"Modified String 4: {user_string.replace('a', '@')}") #replaces a with @ from the input
print(f"Modified String 5: {user_string.capitalize()}") #capitalises the first letter from the input
print(f"Modified String 6: {user_string[::-1]}") #reverses all the characters from the input
print(f"Modified String 7: {user_string.title()}") #capitalises the first letter of each word
print(f"Modified String 8: {len(user_string)}") # gives the number of characters including spaces from the input
print(f"Modified String 9: {user_string.find('a')}") #gives the number of spaces from the input
print(f"Modified String 10: {user_string.count('a')}") # counts how many 'a's there are from the input
print(f"Modified String 11: {user_string.startswith('Hello')}") #states whether or not the user input starts with 'Hello' through true or false
print(f"Modified String 12: {user_string.endswith('!')}") #states whether or not the user input ends with '!'
print(f"Modified String 13: {user_string.isalnum()}")
print(f"Modified String 14: {user_string.isalpha()}")
print(f"Modified String 15: {user_string.isdigit()}") #states whether or not the user input is digits



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!