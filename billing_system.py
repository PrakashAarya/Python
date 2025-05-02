while True:
    name=input("Enter Customer's Name")
    total=0
    while True:
        print("Enter the amount and Quantity")
        amount=float(input("Enter amount"))
        Quantity=float(input("Enter the Quantity"))
        total+=amount*Quantity
        repeat=input("do you want to add more items?(yes/no):")
        if repeat =="no" or repeat=="No":
            break
    print("_"*45)
    print("Name:",name)
    print("Ampunt to be paid:",total)
    print("_"*45)
    print("************Happy   Shopping************")

    repeat1=input("do you want to go to next customer?(Yes/no):")
    if repeat1 == "No" or repeat1 == "no":
        break
        

