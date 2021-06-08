course='Python for beginers'
print(len(course))

##len() and print() ae inbuilt functions where as below listed are methods, to access methods we have to use dot

print(course.find('b')) #find operator gives the index of the character or sequence of characters
print(course.upper())
print(course.lower())
print(course.replace('P','J'))
print('python' in course)
print('for' in course)    #in operator ia a boolean operator and gives result as True or False