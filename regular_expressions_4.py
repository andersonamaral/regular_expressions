import re

lin = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008 '

y = re.findall('^From .*@([^ ]*)', lin)

print(y)
