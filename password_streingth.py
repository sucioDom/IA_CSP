#IA, password_streingth

password = input("give mea password:\n").strip()
length = False
upcase = False
lowcase = False
number = False
symble = False

if len(password) >= 8:
     length = True 
     print(f"Has a least eight characters: {length}")
else:
     print(f"has at least eight characters: {length}")

     for letter in password:
          if letter.isupper():
               upcase = True
               if letter.isnumeric
               number = True
               if letter in !@#$%^&*
               symble = True
