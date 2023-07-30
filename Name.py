import random #will generate numbers based on the range provided by the developer.

def ec2namecharacter(name): #generate several characters
    return "". join(chr(random.randint(2,100)) for i in range(name))
    
ec2count = int(input("What is the number of AWS EC2 instance ")) 

#list the departments.

departments = ["Accounting", "FinOps", "Marketing"]
count = 0 #determined the number of requested random names enter the user

while count != ec2count: #define
    if count < ec2count:
        print("select the departments: Accounting, FinOps or Marketing")
        ec2name = str(input("\n included in your AWS ec2 instance: ")) #prompts the user for the desired named
    if ec2name in departments:
        print(ec2name + ec2namecharacter(15)) #generator charactor
        print("\n")
        count +=1
    elif not ec2name in departments: #did not enter the correct spelling or incorrect upper or lowercase letters.
        ec2name = str(input("\nPlease select again from the following departments: Accounting, FinOps, or Marketing!\n"))
        if ec2name in departments: #recheck the new entry
            print(ec2name + ec2namecharacter(10))
            count += 1
        else:
            print("\nNot authorized to use this program!") #did not correctly enter the name now they are not authorized. 
            print("\nenter the required authorization and run the program again.")
            break
        
#user request is completed
    print('\nYour request is complete and ' + str(count) + 'generator name is created!')
    print('Thank you!')