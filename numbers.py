no1 = int(input("Enter no1"))
no2= int(input ("Enter no2"))
no3 = int(input("Enter no3"))
if(no1 >= no2) and (no1 >= no3):
    print(no1)
elif (no2 >= no1) and (no2 >= no3):
    largest = no2
else:
    largest = no3
print("the largest no is", largest)

