# This program takes a student's name and final grade
# then determines if they passed or failed.
Name = input("Please enter your name: ")
FinalGrade = int(input("Please enter your final grade: "))

if (FinalGrade >= 60): # Greater than or equal to 60
    print(f"Hello {Name}, you passed this class")
else: # Less than 60
    print(f"Hello {Name}, you failed this class")
