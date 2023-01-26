age=int(input("enter the age"))
if(age>=18):
    print("you are eligible to vote")
else:
    yrs=18-age
    print("you have to wait for another ", yrs, " years to cast your vote")

