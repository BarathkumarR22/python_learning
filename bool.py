total = int(input("How manhy classes were held?"))
attended= int(input("How many classes did you attend?"))
percentage= (attended/total)
print(percentage)
if percentage > 0.75:
    print("You can attent exam")
else:
    print("You are not eligible")

