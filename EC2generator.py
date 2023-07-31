import random #generate numbers by the developer. 

def ec2namecharacter(name): #generate several characters
    return "". join(chr(random.randint(2,100)) for i in range(name))
    
ec2numbers = int(input("How many instances do you need? "))

#List the departments.

departments = ["Accounting", "FinOps", "Marketing"]
tally = 0 #determined the number of request random names enter by the user

while tally != ec2numbers: #will be consective additions
    if tally < ec2numbers:
        print("Choose the departments: Accounting, FinOps, or Marketing")
        ec2name = str(input("\nInsert the name of ec2 instance: ")) #cue user for the preference name
    if ec2name in departments:
        print(ec2name + ec2namecharacter(13)) #print requested name and characters
        print("\n")
        tally += 1
    elif not ec2name in departments: #did not enter the correct spelling or uppercase or lowercase letters.
        ec2name = str(input("\nPlease choose from the following departments: Accounting, FinOps, or Marketing!\n"))
        if ec2name in departments: #recheck entry
            print(ec2name + ec2namecharacter(13))
            tally += 1
        else:
            print("\nNot authorized to use!") #did not correctly enter the name. They are denied access. 
            print("\nEnter the required authorization and try again.")
            break
    
#user request is completed.
    print("\nYour request is complete and ' + str(tally) + ' EC2 Generator is created!")
    print("Thank you. Merci!")