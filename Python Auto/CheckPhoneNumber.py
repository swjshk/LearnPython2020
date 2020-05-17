import re

text1='814-777-4394 is not 123-777-4394'

phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # use 'r' to save the \\

mo=phoneNumRegex.search(text1)
print('phone number found '+mo.group())

mo1=phoneNumRegex.findall(text1)
print(mo1)

#website to test regex https://www.regexpal.com/



