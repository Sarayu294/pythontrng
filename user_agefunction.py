name = str(input('enter your name'))
age = int(input("enter your age"))


def user_age(name, age):
  user_age=(100-age)+2021
  return user_age
print("you will return 100 years old in")
print(user_age(name,age))