# grading_app.py

def calculate_grade(mark):
    """Return grade based on mark"""
    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

def main():
    students = {}  # store student: mark pairs
    
    print("Welcome to the Student Report Generator!\n")
    
    while True:
        try:
            name = input("Enter student name (or 'done' to finish): ")
            if name.lower() == "done":
                break
            
            mark = int(input(f"Enter {name}'s mark (0-100): "))
            
            if mark < 0 or mark > 100:
                print("Error: Mark must be between 0 and 100.")
                continue
            
            students[name] = mark
            
        except ValueError:
            print("Error: Please enter a valid whole number for marks.")

    # Write results to a text file
    with open("student_report.txt", "w", encoding="utf-8") as file:
        file.write("STUDENT REPORT\n")
        file.write("====================\n")
        for name, mark in students.items():  # <-- inside the with block
            grade = calculate_grade(mark)
            line = f"{name}: {mark} → Grade {grade}\n"
            print(line, end="")  # display on screen
            file.write(line)
    
    print("\nReport saved as 'student_report.txt'")

if __name__ == "__main__":
    main()
