#generate password which is tough to break

import random                                                       #random module used
lower_case=input("abcdefghijklmnopqrstuvwxyz: ")
upper_case=input("ABCDEFGHIJKLMNOPQRSTUVWXYZ: ")
number=input("0123456789: ")
symbol=input("!%$@&^$*@: ")



use_for=lower_case + upper_case + number + symbol
length_for_pass= 10                                                 #length of the password

password= "".join(random.sample(use_for,length_for_pass))
print("your generated password is:",password)
