salary=int(input("Enter your salary:"))
Age=int(input("Enter your age:"))
if(salary>=20000 or Age<25):
    amount=int(input("Enter your required amount:"))
    if(amount<50000):
        print("You are applicable")
    else:
        print("You are not Applicable")
    print("Your eligible")
else:
    print("Your not eligible")