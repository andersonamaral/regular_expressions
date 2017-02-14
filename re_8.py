import re

x = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008 '

#at least one non-white space character around @ sign

y = re.findall('\S+@\S+', x)

print(y)
