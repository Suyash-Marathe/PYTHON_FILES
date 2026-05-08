subject_1 = int(input("Enter marks of subject 1 :"))
subject_2 = int(input("Enter marks of subject 2 :"))
subject_3 = int(input("Enter marks of subject 3 :"))
subject_4 = int(input("Enter marks of subject 4 :"))

total = subject_1 + subject_2 + subject_3 + subject_4

if (total >= 200) : print("Pass")
elif (total >= 100) : print("ATKT")
else : print("Fail")