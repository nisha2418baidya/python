
#for the first student

student1 = {}

student1["name"] = input("Enter the 1st student name: ")
student1["maths"] = int( input("Enter the maths marks :"))
student1["phy"] = int(input("Enter the phy marks:"))
student1["bio"] = int(input("Enter the bio marks: "))

print(student1)

sum = student1["maths"] + student1["phy"]+ student1["bio"]
avg = sum / (len(student1) - 1)

print("the average marks is ", avg)

def highest(maths , phy , bio):

    if maths > phy and maths > bio:
        print("maths marks is highest: ", maths)
    elif phy >maths and phy > bio:
        print("physics marks is highest: ", phy)
    elif bio > maths and bio > phy:
        print("biology marks is highest: ", bio)
    else:
        print("Your two marks are equal")

highest(student1["maths"] , student1["phy"], student1["bio"])


def lowest(maths , phy , bio):
    if maths < phy and maths < bio:
        print("maths marks is lowest: ", maths)
    elif phy <maths and phy < bio:
        print("physics marks is lowest: ", phy)
    elif bio < maths and bio < phy:
        print("chemistry marks is lowest: ", bio)
    else:
        print("Your two marks are equal")

lowest(student1["maths"] , student1["phy"], student1["bio"])

def remove_name():
    name = input("enter a name: ")
    if name == student1["name"]:
     del student1["name"]

    else:
     print("enter name is invaild")
remove_name()

def remove_maths():
    marks= int(input("Enter the maths marks you wamt to remove : "))
    if student1["maths"] == marks:
        del student1["maths"]
        print(student1)
   
    else :
        print("the entered marks is invalid")
remove_maths()

def remove_phy():
    marks= int(input("Enter the phy marks you wamt to remove : "))
    if student1["phy"] == marks:
        del student1["phy"]
        print(student1)
    else :
        print("the entered marks is invalid")
remove_phy()

def remove_bio():
    marks= int(input("Enter the bio marks you wamt to remove : "))
    if student1["bio"] == marks:
        del student1["bio"]
        print(student1)
    else :
        print("the entered marks is invalid")
remove_bio()



#for the second student

student2 = {}

student2["name"] = input("Enter the 2nd student name: ")
student2["maths"] = int( input("Enter the maths marks :"))
student2["phy"] = int(input("Enter the phy marks:"))
student2["bio"] = int(input("Enter the bio marks: "))

print(student2)

sum = student2["maths"] + student2["phy"]+ student2["bio"]
avg = sum / (len(student2) - 1)

print("the average marks is ", avg)

def highest(maths , phy , bio):

    if maths > phy and maths > bio:
        print("maths marks is highest: ", maths)
    elif phy >maths and phy > bio:
        print("physics marks is highest: ", phy)
    elif bio > maths and bio > phy: 
        print("biology marks is highest: ", bio)
    else:
        print("Your two marks are equal")

highest(student2["maths"] , student2["phy"], student2["bio"])


def lowest(maths , phy , bio):
    if maths < phy and maths < bio:
        print("maths marks is lowest: ", maths)
    elif phy <maths and phy < bio:
        print("physics marks is lowest: ", phy)
    elif bio < maths and bio < phy:
        print("chemistry marks is lowest: ", bio)
    else:
        print("Your two marks are equal")

lowest(student2["maths"] , student2["phy"], student2["bio"])

def remove_name():
    name = input("enter a name: ")
    if name == student2["name"]:
     del student2["name"]

    else:
     print("enter name is invaild")
remove_name()

def remove_maths():
    marks= int(input("Enter the maths marks you wamt to remove : "))
    if student2["maths"] == marks:
        del student2["maths"]
        print(student2)
   
    else :
        print("the entered marks is invalid")
remove_maths()

def remove_phy():
    marks= int(input("Enter the phy marks you wamt to remove : "))
    if student2["phy"] == marks:
        del student2["phy"]
        print(student2)
    else :
        print("the entered marks is invalid")
remove_phy()

def remove_bio():
    marks= int(input("Enter the bio marks you wamt to remove : "))
    if student2["bio"] == marks:
        del student2["bio"]
        print(student2)
    else :
        print("the entered marks is invalid")
remove_bio()



#for the third student

student3 = {}

student3["name"] = input("Enter the 3rd student name: ")
student3["maths"] = int( input("Enter the maths marks :"))
student3["phy"] = int(input("Enter the phy marks:"))
student3["bio"] = int(input("Enter the bio marks: "))

print(student3)

sum = student3["maths"] + student3["phy"]+ student3["bio"]
avg = sum / (len(student3) - 1)

print("the average marks is ", avg)

def highest(maths , phy , bio):

    if maths > phy and maths > bio:
        print("maths marks is highest: ", maths)
    elif phy >maths and phy > bio:
        print("physics marks is highest: ", phy)
    elif bio > maths and bio > phy: 
        print("biology marks is highest: ", bio)
    else:
        print("Your two marks are equal")

highest(student3["maths"] , student3["phy"], student3["bio"])


def lowest(maths , phy , bio):
    if maths < phy and maths < bio:
        print("maths marks is lowest: ", maths)
    elif phy <maths and phy < bio:
        print("physics marks is lowest: ", phy)
    elif bio < maths and bio < phy:
        print("chemistry marks is lowest: ", bio)
    else:
        print("Your two marks are equal")

lowest(student3["maths"] , student3["phy"], student3["bio"])

def remove_name():
    name = input("enter a name: ")
    if name == student3["name"]:
     del student3["name"]

    else:
     print("enter name is invaild")
remove_name()

def remove_maths():
    marks= int(input("Enter the maths marks you wamt to remove : "))
    if student3["maths"] == marks:
        del student3["maths"]
        print(student3)
   
    else :
        print("the entered marks is invalid")
remove_maths()

def remove_phy():
    marks= int(input("Enter the phy marks you wamt to remove : "))
    if student3["phy"] == marks:
        del student3["phy"]
        print(student3)
    else :
        print("the entered marks is invalid")
remove_phy()

def remove_bio():
    marks= int(input("Enter the bio marks you wamt to remove : "))
    if student3["bio"] == marks:
        del student3["bio"]
        print(student3)
    else :
        print("the entered marks is invalid")
remove_bio()
