### DO IT!! ###
def user():
  name = input("Enter your name:")
  passwd = input("Enter your password:")
  rt_passwd = input("Retype again: ")

  if passwd == rt_passwd :
    print("Welcome ", name)
  else :
    print(name, ", your password didn't match. Try again!")
    user()
    
user()
