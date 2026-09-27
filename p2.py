# the user-defined function computes the average of 3 activity scores
def ave (score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return average

students = int(input("How many students?: "))

# it will validate that the program will process at least 3 students
if students < 3:
    print("Must be at least 3 students")
else:
    s = 0 # counter to keep track of the current student num
    # loop that repeat the process of every student
    while s < students:
        s = s + 1
        print("Student", s)
        name = input("Enter name: ")
        act1 = float(input("Activity 1: "))
        act2 = float(input("Activity 2: "))
        act3 = float(input("Activity 3: "))
        # it will compute the average of all activity scores
        average = ave(act1, act2, act3)
        # determines the status based on the ave
        if average >=90:
            status = "Excellent"
        elif average >=80:
            status = "Very Good"
        elif average>=75:
            status = "Passed"
        else:
            status = "Failed"

        print("-------------------------")
        print("|  STUDENT PERFORMANCE  |")
        print("-------------------------")
        print(" Name: ", name)
        print(" Activity Scores")
        print("  Activity 1 .......", act1)
        print("  Activity 2 .......", act2)
        print("  Activity 3 .......", act3)
        print("--------------------------")
        print(" Average:", round(average, 2))
        print(" Status:", status)
        print("==========================")




