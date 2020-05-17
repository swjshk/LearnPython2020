'''
format you output
2 ways
'''

# Method 1
# formatted string literals 'f' or 'F'
year='2020'
month='May'
str1=f'Year {year} and Month {month}'
# print(str1)


# Method 2
# str.format()
yes_votes=42_572_654  
#print(yes_votes)
no_votes=43_132_495
percentage = yes_votes / (yes_votes + no_votes)
str2 = '{:-9} Yes votes  {:2.2%}'.format(yes_votes,percentage) 
#use string slicing and concatenation to format the passed string
#print(str2)

import math
print(f'The value of pi is {math.pi:.3f}.')
