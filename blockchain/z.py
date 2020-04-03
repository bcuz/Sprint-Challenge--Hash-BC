import random
import string

# now lets see what this string module provide us.
# I wont be going into depth because the python
# documentation provides ample information.
# so lets generate a random string with 32 characters.

# print(string.ascii_letters[:6])

random = ''.join([random.choice(string.ascii_letters[:6] + string.digits) for n in range(6)])
print(random)