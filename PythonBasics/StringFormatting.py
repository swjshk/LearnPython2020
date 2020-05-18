"""
format you output
2 ways
"""

# Method 1
# formatted string literals 'f' or 'F'
year = "2020"
month = "May"
str1 = f"Year {year} and Month {month}"
# print(str1)


# Method 2
# str.format()
yes_votes = 42_572_654
# print(yes_votes)
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
str2 = "{:-9} Yes votes  {:2.2%}".format(yes_votes, percentage)
# use string slicing and concatenation to format the passed string
# print(str2)

import math

# print(f"The value of pi is {math.pi:.3f}.")



print('{0} and {1}'.format('spam', "eggs"))
print('{1} and {0}'.format('spam', "eggs"))
# {0} position of the objects passed into the .format()

print('This {food} is {adjective}.'.format(
    food="spam", adjective='absolutely horrible'))
# keyword arguments

table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table))
# pass the tabel as keyword args with '**'
print('jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# format specification mini-language
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x,x*x*x))


test=1