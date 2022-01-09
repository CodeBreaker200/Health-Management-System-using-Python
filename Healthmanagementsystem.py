
#HEALTH MANAGEMENT SYSTEM
import datetime
def gettime():
    return datetime.datetime.now()
def get (R):
    if R==1:
        inp=int(input("Enter 1 for Excersise & 2 for Food\n"))
        if(inp==1):

            value=input("ENTER  DAY &  EXCERSISE\n")
            with open("ROHTI EX .txt","a") as rk:
                rk.write(str([str(gettime())])+"- "+value+"\n")
            print("Successfully Added Rohit Excersise\n")
        
        elif(R==2):
            value = input("ENTER DAY & FOOD\n")
            with open("ROHIT FOOD.txt", "a") as rk:
                rk.write(str([str(gettime())]) + "- " + value + "\n")
            print("successfully Added Rohit food\n")

    elif(R==2):
        R = int(input("Enter 1 for Excersise & 2 for food\n"))
        if (R == 1):
            value = input("ENTER  DAY &  EXCERSISE \n")
            with open("RUTIK EX.txt", "a") as rk:
                rk.write(str([str(gettime())]) + "- " + value + "\n")
            print("Successfully Added Rutik Excersise\n")
        elif (R == 2):
            value = input("ENTER DAY & FOOD\n")
            with open("RUTIK FOOD.txt", "a") as rk:
                rk.write(str([str(gettime())]) + "- " + value + "\n")
            print("Successfully Added Rutik Food")
    elif(R==3):
        R = int(input("Enter 1 for Excersise & 2 for Food\n"))
        if (R == 1):
            value = input("ENTER DAY & EXCERSISE\n")
            with open("SUSHANT EX .txt", "a") as sk:
                sk.write(str([str(gettime())]) + "- " + value + "\n")
            print("Successfully Added Sushant Excersise\n")
        elif (R == 2):
            value = input("ENTER DAY & FOOD\n")
            with open("SUSHANT FOOD.txt", "a") as sk:
                sk.write(str([str(gettime())]) + "- " + value + "\n")
            print("Successfully Added Sushant Food\n")
    else:
        print("Please Enter Vallid Input -- As 1 (ROHTI) 2 (RUTIK) 3 (SUSHANT) )")
def Retrieve(R):
    if R==1:
        R=int(input("Enter 1 for Excersise & 2 for Food\n"))
        if(R==1):
            with open("ROHTI EX .txt") as rk:
                for i in rk:
                    print(i,end="THANK YOU ROHIT !!\n")
        elif(R==2):
            with open("ROHIT FOOD.txt") as rk:
                for i in rk:
                    print(i, end="THANK YOU ROHIT !!\n")

    elif(R==2):
        R = int(input("Enter 1 for Excersise & 2 for Food\n"))
        if (R == 1):
            with open("RUTIK EX.txt") as rk:
                for i in rk:
                    print(i, end="THANK YOU RUTIK !!\n")

        elif (R == 2):
            with open("RUTIK FOOD.txt") as rk:
                for i in rk:
                    print(i, end="THANK YOU RUTIK\n")

    elif(R==3):
        R = int(input("Enter 1 for Excersise & 2 for Food\n"))
        if (R == 1):
            with open("SUSHANT EX .txt") as sk:
                for i in sk:
                    print(i, end="THANK YOU SUSHANT !!\n")

        elif (R == 2):
            with open("SUSHANT FOOD.txt") as sk:
                for i in sk:
                    print(i, end="THANK YOU SUSHANT !!\n")

    else:
        print("Please Enter Vallid Input -- As 1 (ROHTI) 2 (RUTIK) 3 (SUSHANT\n))")

print("***Welcome To Our Health Management System***\n")
a=int(input("Press 1 for Loc & 2 for Retrieve:-\n "))

if a==1:
    b = int(input("Press 1 for ROHIT 2 for RUTIK 3 for SUSHANT\n "))
    get(b)
else:
    b = int(input("Press 1 for ROHIT 2 for RUTIK 3 for SUSHANT \n"))
    Retrieve(b)
