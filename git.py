a = 9;
b = 7;
c =9+7;
print(c)

d=int(input("enter your age"))
print(d)

e=(input("enter name"))
print(e)

import random, string
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print(password)  # Example: "X7fB2pLz"