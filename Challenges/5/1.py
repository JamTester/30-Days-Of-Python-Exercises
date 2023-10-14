import math 
#1. Declare an empty list
#2. Declare a list with more than 5 items
#3. Find the length of your list
#4. Get the first item, the middle item and the last item of the list
#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)


def one():
    lst = []
    goodsongs = ['https://music.youtube.com/watch?v=Aopq767GO3Q&feature=shared', 'https://music.youtube.com/watch?v=3qkdHarF-mw','https://music.youtube.com/watch?v=lsV500W4BHU&feature=shared','https://music.youtube.com/watch?v=UXIvINyQ0RA&feature=shared','https://music.youtube.com/watch?v=rz7v6GXrZP8&feature=shared','https://music.youtube.com/watch?v=6QL_bUCuhvo&feature=shared']
    len(goodsongs)
    print(goodsongs[0], goodsongs[len(goodsongs)//2], goodsongs[-1]) 
    mixed_data_types = ['Jason Sawyer', 21, '170cm', 'Single', 'Yeah No'] #eww PII

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
#7. Print the list using print()
#8. Print the number of companies in the list
#9. Print the first, middle and last company 
#10. Print the list after modifying one of the companies
#11. Add an IT company to it_companies
#12. Insert an IT company in the middle of the companies list
#13. Change one of the it_companies names to uppercase (IBM excluded!)
#14. Join the it_companies with a string '#;  '


def two():
    it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 
    print(it_companies)
    print(len(it_companies))
    num = len(it_companies)/2
    num = (math.ceil(num))
    print(it_companies[0], it_companies[num], it_companies[-1])

    it_companies[0] = 'Meta'
    print(it_companies)

    it_companies.insert(len(it_companies)//2, 'Samsung')
    print(it_companies)
    it_companies[1] = it_companies[1].upper() 
    print("#; ".join(it_companies))

#15. Check if a certain company exists in the it_companies list.
#16. Sort the list using sort() method
#17. Reverse the list in descending order using reverse() method
#18. Slice out the first 3 companies from the list
#19. Slice out the last 3 companies from the list
#20. Slice out the middle IT company or companies from the list
#21. Remove the first IT company from the list
#22. Remove the middle IT company or companies from the list
#23. Remove the last IT company from the list
#24. Remove all IT companies from the list
#25. Destroy the IT companies list

def three():
    it_companies = ['Samsung', 'META', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
    a = input("Name an IT Company: ")
    if a in it_companies:
        print(f'{a} is in the list of IT Companies')
    else:
        print(f'{a} is not in the list of IT Companies')

    it_companies.sort()
    print(it_companies)
    it_companies.sort(reverse=True); print(it_companies)
    print(it_companies)
    print(it_companies[3:8])
    print(it_companies[0:5])
    print(it_companies[0:3] + it_companies[5:8])
    del it_companies[0]
    print(it_companies)
    del it_companies[4:6]
    print(it_companies)
    del it_companies[-1]
    print(it_companies)
    del it_companies

def four():
    #26. Join the following lists:
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    full_stack = front_end + back_end
    print(full_stack)
    full_stack.insert(5, 'Python'); full_stack.insert(6,'SQL')
    print(full_stack)

# Exercises: Level 2

def five():
#1. The following is a list of 10 students ages:
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#- Sort the list and find the min and max age
#- Add the min age and the max age again to the list
#- Find the median age (one middle item or two middle items divided by two)
#- Find the average age (sum of all items divided by their number )
#- Find the range of the ages (max minus min)
#- Compare the value of (min - average) and (max - average), use _abs()_ method
    ages.sort()
    min = ages[0]
    max = ages[-1]
    avg = sum(ages)/len(ages)
    print(f'{min} is the min age. {max} is the max age.')
    num = len(ages)/2
    num = (math.ceil(num))
    print(f'{ages[num]} is the medium age')
    print(f'{avg} is the average')
    print(f'{max - min} is the range')
    print(f'{abs(min - avg)}')

def six():
    #1. Find the middle country(ies) in the countries list
    #2.Divide the countries list into two equal lists if it is even if not one more country for the first half.
    #3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
        countries = [
            'Afghanistan',
            'Albania',
            'Algeria',
            'Andorra',
            'Angola',
            'Antigua and Barbuda',
            'Argentina',
            'Armenia',
            'Australia',
            'Austria',
            'Azerbaijan',
            'Bahamas',
            'Bahrain',
            'Bangladesh',
            'Barbados',
            'Belarus',
            'Belgium',
            'Belize',
            'Benin',
            'Bhutan',
            'Bolivia',
            'Bosnia and Herzegovina',
            'Botswana',
            'Brazil',
            'Brunei',
            'Bulgaria',
            'Burkina Faso',
            'Burundi',
            'Cambodia',
            'Cameroon',
            'Canada',
            'Cape Verde',
            'Central African Republic',
            'Chad',
            'Chile',
            'China',
            'Colombi',
            'Comoros',
            'Congo (Brazzaville)',
            'Congo',
            'Costa Rica',
            "Cote d'Ivoire",
            'Croatia',
            'Cuba',
            'Cyprus',
            'Czech Republic',
            'Denmark',
            'Djibouti',
            'Dominica',
            'Dominican Republic',
            'East Timor (Timor Timur)',
            'Ecuador',
            'Egypt',
            'El Salvador',
            'Equatorial Guinea',
            'Eritrea',
            'Estonia',
            'Ethiopia',
            'Fiji',
            'Finland',
            'France',
            'Gabon',
            'Gambia, The',
            'Georgia',
            'Germany',
            'Ghana',
            'Greece',
            'Grenada',
            'Guatemala',
            'Guinea',
            'Guinea-Bissau',
            'Guyana',
            'Haiti',
            'Honduras',
            'Hungary',
            'Iceland',
            'India',
            'Indonesia',
            'Iran',
            'Iraq',
            'Ireland',
            'Israel',
            'Italy',
            'Jamaica',
            'Japan',
            'Jordan',
            'Kazakhstan',
            'Kenya',
            'Kiribati',
            'Korea, North',
            'Korea, South',
            'Kuwait',
            'Kyrgyzstan',
            'Laos',
            'Latvia',
            'Lebanon',
            'Lesotho',
            'Liberia',
            'Libya',
            'Liechtenstein',
            'Lithuania',
            'Luxembourg',
            'Macedonia',
            'Madagascar',
            'Malawi',
            'Malaysia',
            'Maldives',
            'Mali',
            'Malta',
            'Marshall Islands',
            'Mauritania',
            'Mauritius',
            'Mexico',
            'Micronesia',
            'Moldova',
            'Monaco',
            'Mongolia',
            'Morocco',
            'Mozambique',
            'Myanmar',
            'Namibia',
            'Nauru',
            'Nepal',
            'Netherlands',
            'New Zealand',
            'Nicaragua',
            'Niger',
            'Nigeria',
            'Norway',
            'Oman',
            'Pakistan',
            'Palau',
            'Panama',
            'Papua New Guinea',
            'Paraguay',
            'Peru',
            'Philippines',
            'Poland',
            'Portugal',
            'Qatar',
            'Romania',
            'Russia',
            'Rwanda',
            'Saint Kitts and Nevis',
            'Saint Lucia',
            'Saint Vincent',
            'Samoa',
            'San Marino',
            'Sao Tome and Principe',
            'Saudi Arabia',
            'Senegal',
            'Serbia and Montenegro',
            'Seychelles',
            'Sierra Leone',
            'Singapore',
            'Slovakia',
            'Slovenia',
            'Solomon Islands',
            'Somalia',
            'South Africa',
            'Spain',
            'Sri Lanka',
            'Sudan',
            'Suriname',
            'Swaziland',
            'Sweden',
            'Switzerland',
            'Syria',
            'Taiwan',
            'Tajikistan',
            'Tanzania',
            'Thailand',
            'Togo',
            'Tonga',
            'Trinidad and Tobago',
            'Tunisia',
            'Turkey',
            'Turkmenistan',
            'Tuvalu',
            'Uganda',
            'Ukraine',
            'United Arab Emirates',
            'United Kingdom',
            'United States',
            'Uruguay',
            'Uzbekistan',
            'Vanuatu',
            'Vatican City',
            'Venezuela',
            'Vietnam',
            'Yemen',
            'Zambia',
            'Zimbabwe',
            ]
        mid1 = len(countries)//2
        mid2 = math.ceil(len(countries)/2)
        print(mid2)
        firsthalf = countries[0:mid1]
        secondhalf = countries[mid2:-1]
        print(firsthalf)
        print(secondhalf)
def seven():
    countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
    chi, rus, usa, *scandic = countries
    print(countries)
