def result_out():
    mark = int(input("Enter your mark:"))
    if (mark>50 and mark<=60):
    
        print ("Grade:D")
    
    elif(mark>60 and mark<=70):
    
        print("Grade:C")

    elif(mark >70 and mark<=80):
        print("Grade:B")
    elif(mark>80 and mark<90):
        print("Grade: A")
    elif(mark>90 and mark<100):
        print("Grade:O")
    else:
        print("Re appear")
    
result_out()
