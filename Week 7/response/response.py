#  'someone@example.com' ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
import validators

email = input()
# try: 'someone@example.com'
valid = validators.email(email)
# except ValidationError:
   

# print(valid)
if valid != True:
     print("Invalid")
else:
    print("Valid")