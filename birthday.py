def birthday(name):
    if name=="albert einstein":
        print(name,"birthday is",data["albert einstein"])
    elif name=="benjamin franklin":
        print(name, "birthday is", data["benjamin franklin"])
    elif name=="Ada Lovelace":
        print(name, "birthday is",data["Ada Lovelace"])
    else:
        print("the input you gave is not in our directory please recheck")
data={"albert einstein":"20/07/1991","benjamin franklin":"01/17/1706","Ada Lovelace":"16/12/1945"}
print("welcome to the birthday dictionary . we know the birthdays of :\nalbert einstein \n benjamin franklin \n Ada Lovelace ")
name=input("who's birthday you want to look?")
birthday(name)



