# Take input for the student that he can attend the exam or not
medical_cause = input("Did you have a medical cause?(Y/N):").strip().upper()

#Checking the user input and predicting output accordingly
if medical_cause == 'Y':   #Condition 1
    print("yuo are allowed")
else:
    #Take input of attendance
    atten = int(input("Enter the attendance of student: "))

    if atten >= 75:    #Condidtion 2
        print("Allowed")
    else:
        print("Not allowed")