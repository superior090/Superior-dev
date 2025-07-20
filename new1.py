
import json
import os  

class School_student:
    def __init__(self, name, subject, scores, average, grade):
        self.name = name
        self.subject = subject
        self.scores = scores
        self.average = average
        self.grade = grade

    def to_json(self):
        return {
            "Name": self.name,
            "Subject": self.subject,
            "Scores": self.scores,
            "Average": self.average,
            "Grade": self.grade }

def add_student():
    name = input("Enter student name: ")
    subject = input("Enter the subject: ")
    score_input = input("Enter the scores separated by commas: ")

    try:
        score_list = list(map(float, score_input.split(',')))
        average = sum(score_list) / len(score_list)
    except ValueError:
        print("Invalid scores entered.")
        return

  
    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    new_student = School_student(name, subject, score_list, average, grade)

    students = []
    if os.path.exists("my_student.json"):
        with open("my_student.json", "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    students = data
                else:
                    students = [data]  
            except json.JSONDecodeError:
                students = []

    students.append(new_student.to_json())

    with open("my_student.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Student added successfully!")

def view_student():
    try:
        with open("my_student.json", "r") as file:
            students = json.load(file)
            for student in students:
                print("-" * 40)
                print("Student details:", student)
    except FileNotFoundError:
        print("No student found")

def update_student():
    try:
        with open("my_student.json", "r") as file:
            students = json.load(file)

        name = input("Enter student name to update: ")
        found = False

        for student in students:
            if student["Name"].lower() == name.lower():
                print("Student found. Enter new scores.")
                scores_input = input("Enter new scores separated by commas: ")
                try:
                    new_scores = list(map(float, scores_input.split(',')))
                    average = sum(new_scores) / len(new_scores)
                except ValueError:
                    print("Invalid input.")
                    return

                if average >= 70:
                    grade = "A"
                elif average >= 60:
                    grade = "B"
                elif average >= 50:
                    grade = "C"
                elif average >= 40:
                    grade = "D"
                else:
                    grade = "F"

                student["Scores"] = new_scores
                student["Average"] = average
                student["Grade"] = grade
                found = True
                break

        if found:
            with open("my_student.json", "w") as file:
                json.dump(students, file, indent=4)
            print("Student updated successfully.")
        else:
            print("No student found.")
    except FileNotFoundError:
        print("Student not found.")

# Create file if it doesn't exist
if not os.path.exists("my_student.json"):
    with open("my_student.json", "w") as file:
        json.dump([], file)
        print("JSON file created and initialized")

# Main loop
while True:
    print("\n1. Add")
    print("2. View")
    print("3. Update")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, try again.")




    


