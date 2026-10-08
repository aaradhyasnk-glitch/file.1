print ("========================")
print ("Holiday activity planner")
print ("========================")

print ("\nStep 1:")
print ("\nPrint your holiday type: ")
print ("1. Beach ")
print ("2. Mountain ")
print ( )

choice1 = int (input("Enter 1 or 2: "))

if choice1==1:
    print ("\nStep 2:")
    print ("\nPick your Activity")
    print ("1. Swimming ")
    print ("2. Sandcastle Building")

    beach_activity= int(input("Enter 1 or 2:"))
    if beach_activity==1:
        print("You picked  : Swimming")
        print("Best time   : Morning")
        print("Remember    : Carry sunscreen and water")
    else:
        print("You picked  : Sandcastle               ")
        print("Best time   : Evening                  ")
        print("Remember    : Carry a bucket and spade ")

elif choice1==2:
    print ("\nStep 2:")
    print ("\nPick your Activity")
    print ("1. Hiking  ")
    print ("2. Camping")
   
    mountain_activity= int(input("Enter 1 or 2:"))
    if mountain_activity==1:
           print("You picked  : Hiking"                )
           print("Best for    : Exploring trails"      )
           print("Remember    : Wear comfortable shoes")
    else:
           print("You picked  : Camping                    ")
           print("Best for    : Staying close to nature    ")
           print("Remember    : Carry a tent and flashlight")

else:
     print ("That is not the valid choice!")
     print ("Please selsect between option 1. and 2.")

print ("\n===========================================")
print ("\n     Your Holiday Plan is READY!!! ")
print ("            Enjoy your trip!")
print ("\n===========================================")