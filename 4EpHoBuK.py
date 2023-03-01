import re
# Validate strong password
password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
#re.match(password_pattern, 'secret') # Returns None
#re.match(password_pattern, '-Secr3t.') # Returns Match object
userpass = input("Enter your password")
#print(re.match(password_pattern, userpass))
if re.match(password_pattern, userpass) is None:
    print("vayblyad")
