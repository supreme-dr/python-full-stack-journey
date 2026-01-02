# grading_app.py

def calculate_grade(mark):
    """Return grade based on mark"""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

def main():
    students = {}  # dictionary to store student: mark pairs
    
    while True:
        try:
            name = input("Enter student name (or 'done' to finish): ")
            if name.lower() == "done":
                break
            
            mark = int(input(f"Enter {name}'s mark (0-100): "))
            
            if mark < 0 or mark > 100:
                print("Error: Mark must be between 0 and 100.")
                continue
            
            students[name] = mark  # store in dictionary
            
        except ValueError:
            print("Error: Please enter a valid whole number for marks.")

    # Display grades for all students
    print("\n--- Student Grades ---")
    for name, mark in students.items():
        grade = calculate_grade(mark)
        print(f"{name} scored {mark} and got grade {grade}.")

if __name__ == "__main__":
    main()
