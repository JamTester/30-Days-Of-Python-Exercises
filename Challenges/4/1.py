# I am now commenting the question so it's easy to understand
#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

def one():
    a = 'Thirty'
    b = 'Days'
    c = 'Of'
    d = 'Python'
    e = ' '
    sent = a+e+b+e+c+d
    print(sent)

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
def two():
    a = 'Coding'
    b = 'For'
    c = 'All'
    d = ' '
    print(a+d+b+d+c)


#3. Declare a variable named company and assign it to an initial value "Coding For All".
#4. Print the variable company using print().
#5. Print the length of the company string using len() method and print().
#6. Change all the characters to uppercase letters using upper() method.
#7. Change all the characters to lowercase letters using lower() method.
#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

def three():
    company = 'Coding For All'
    print(company)
    print(len(company))
    print(company.upper())
    print(company.lower())
    print(company.capitalize())
    print(company.title())
    print(company.swapcase())


#9. Cut(slice) out the first word of Coding For All string.
#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.

def four():
    company = 'Coding For All'
    sli = company[7:14]
    print(sli)

    sli = company[0:6]
    if sli in company:
        print(f'"{sli}" is in "{company}"')
    else:
        print(f'"{sli}" is not in "{company}"')
    
    if company.find(sli) == 0:
        print(f'{sli} is found in {company}')
    else:
        print(f'{sli} is not found in {company}')
    
    if company.index(sli) == 0:
           print(f'{sli} is found in {company}')
    else:
        print(f'{sli} is not found in {company}')
    
#11. Replace the word coding in the string 'Coding For All' to Python.
#12. Change Python for Everyone to Python for All using the replace method or other methods.
#13. Split the string 'Coding For All' using space as the separator (split()) .

def five():
    company = 'Coding For All'
    print(company.replace('Coding', 'Python'))
    
    sli = company[7:14]
    print(f'Python {sli}')

    a, b, c = company.split()
    print(f'{a} {b} {c}')
    print(b, c, a)
    print(f'Python {b} {c}')

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

def six():
    var = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
    var = var.split(",")
    print(type(var))
    print(var)

#16. What is the last index of the string _Coding For All_


def seven():
    var = '_Coding For All_'    
    lastindex = var[-1]
    print(f' The last last index is {lastindex} and it is number', len(var) - 1)

#17. What character is at index 10 in "Coding For All" string.
#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
#19. Create an acronym or an abbreviation for the name 'Coding For All'.

def eight():
    var = 'Coding For All'
    var1 = var[10]
    print(f'"{var1}" is the character located at index ten')

    var1 = 'Python For Everyone'
    
    a = var1[0] + var1[7] + var1[11]
    print(a)

    C = var[0] + var[8] + var[12]
    print(C.upper())

#20. Use index to determine the position of the first occurrence of C in Coding For All.
#21. Use index to determine the position of the first occurrence of F in Coding For All.
#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
def nine():
    var = 'Coding For All'
    print(var.index('C'))
    print(var.index('F'))
    print(var.rfind('I'))

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#26. (author repeated question) Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#27. (author repeated question) Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#28. Does 'Coding For All' start with a substring Coding?
#29. Does 'Coding For All' end with a substring coding?

def ten():
    sent = 'You cannot end a sentence with because because because is a conjunction'
    print(sent.index('because'))
    print(sent.find('because'))
    print(sent.rfind('because'))
    sli = sent[0:30] + sent[54:71]
    print(sli)
    print(sent.index('because'))

    print('\n')

    a = 'Coding For All'
    b = 'All'

    if a.index(b) == 0:
        print(f'{a} starts with {b}')
    else:
        print(f'{a} does not start with {b}')


    if a.rfind(b) == len(a) - len(b):
        print(f'{a} ends with {b}')
    else:
        print(f'{a} does not ends with {b}')


#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
#31 Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython, thirty_days_of_python


def eleven():
    a = '   Coding For All      '
    print(a.strip())
    b = 'thirty_days_of_python'
    c = '30DaysOfPython' 
    if b.isidentifier() == True:
        print(f'{b} is an identifier')
    else:
        print(f'{b} is not identifier')

    if c.isidentifier() == True:
        print(f'{c} is an identifier')
    else:
        print(f'{c} is not identifier')

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
def twelve():
    a = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
    join = '# '.join(a)
    print(join)

#33. Use the new line escape sequence to separate the following sentences.
#34. Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki

def thirteen():
    print(f'I am enjoying this challenge.\nI just wonder what is next.')
    var = "Name \tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
    print(var.expandtabs(10))

#35. Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.

def fourteen():
    radius = 10
    area = 3.14 * radius ** 2
    print("The area of a circle with radius {} is {} meters square.".format(radius, area))

#36. Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
def fifteen():
    a = 8
    b = 6
    print('{} + {} = {}'.format(a, b, a + b))
    print('{} - {} = {}'.format(a, b, a - b))
    print('{} * {} = {}'.format(a, b, a * b))
    print('{} / {} = {:.2f}'.format(a, b, a / b)) 
    print('{} % {} = {}'.format(a, b, a % b))
    print('{} // {} = {}'.format(a, b, a // b))
    print('{} ** {} = {}'.format(a, b, a ** b))
fifteen()