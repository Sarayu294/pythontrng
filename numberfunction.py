
def biggest(no1, no2, no3):
    if(no1 >= no2) and (no1 >= no3):
        largest = no1
    elif (no2 >= no1) and (no2 >= no3):
        largest = no2
    else:
        largest = no3
    return largest


print(biggest(10, 20, 30))

