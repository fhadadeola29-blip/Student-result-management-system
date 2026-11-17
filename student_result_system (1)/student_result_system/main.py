"""
STUDENT RESULT MANAGEMENT SYSTEM
Created by : Fhad Balogun
Contributor: Khidir Segun Aileru
Run with   : python main.py
"""
import re
from student import Student
from results import SUBJECTS
from storage import load_students, save_students
from reports import report_card, class_list, class_statistics, save_report_to_file

students = load_students()


def find_student(student_id):
    for s in students:
        if s.student_id.lower() == student_id.lower():
            return s
    return None


def ask_scores():
    """Ask for a score (0-100) for each of the 5 subjects."""
    scores = {}
    for subject in SUBJECTS:
        while True:
            try:
                value = float(input(f"  {subject} score (0-100): "))
                if 0 <= value <= 100:
                    scores[subject] = value
                    break
                print("  Score must be between 0 and 100.")
            except ValueError:
                print("  Please enter a number.")
    return scores


def add_student():
    sid = input("Student ID (e.g. ST001): ").strip().upper()
    if not re.fullmatch(r"ST\d{3}", sid):          # regex validation
        print("Invalid ID. Use format ST001.")
        return
    if find_student(sid):
        print("That ID already exists.")
        return
    name = input("Full name: ").strip()
    class_name = input("Class/Form (e.g. SS1): ").strip()
    gender = input("Gender (M/F): ").strip().upper()
    dob = input("Date of birth (YYYY-MM-DD): ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    students.append(Student(sid, name, class_name, gender, dob))
    save_students(students)
    print("Student added.")


def view_students():
    if not students:
        print("No students yet.")
        return
    for s in students:
        print(f"{s.student_id} | {s.name} | {s.class_name} | {s.gender} | {s.dob}")


def search_student():
    word = input("Enter ID or name: ").strip().lower()
    found = [s for s in students if word in s.student_id.lower() or word in s.name.lower()]
    if not found:
        print("No match found.")
    for s in found:
        print(f"{s.student_id} | {s.name} | {s.class_name} | {s.gender} | {s.dob}")


def update_student():
    s = find_student(input("Student ID to update: ").strip())
    if not s:
        print("Student not found.")
        return
    print("Press Enter to keep the old value.")
    s.name = input(f"Name [{s.name}]: ").strip() or s.name
    s.class_name = input(f"Class [{s.class_name}]: ").strip() or s.class_name
    s.gender = input(f"Gender [{s.gender}]: ").strip().upper() or s.gender
    s.dob = input(f"DOB [{s.dob}]: ").strip() or s.dob
    save_students(students)
    print("Student updated.")


def delete_student():
    s = find_student(input("Student ID to delete: ").strip())
    if not s:
        print("Student not found.")
        return
    if input(f"Delete {s.name}? (y/n): ").lower() == "y":
        students.remove(s)
        save_students(students)
        print("Student deleted.")


def record_scores():
    s = find_student(input("Student ID: ").strip())
    if not s:
        print("Student not found.")
        return
    s.set_scores(ask_scores())          # also works for updating scores
    save_students(students)
    print("Scores saved.")


def show_report_card():
    s = find_student(input("Student ID: ").strip())
    if not s:
        print("Student not found.")
    elif not s.scores:
        print("No scores recorded for this student yet.")
    else:
        print(report_card(s))


def show_class_list():
    choice = input("Sort by (1) Average or (2) Name: ").strip()
    print(class_list(students, "name" if choice == "2" else "average"))


def main():
    print("=" * 45)
    print("  STUDENT RESULT MANAGEMENT SYSTEM")
    print("  Created by Fhad Balogun")
    print("  Contributor: Khidir Segun Aileru")
    print("=" * 45)
    menu = {
        "1": ("Add student", add_student),
        "2": ("View all students", view_students),
        "3": ("Search student", search_student),
        "4": ("Update student", update_student),
        "5": ("Delete student", delete_student),
        "6": ("Record / update scores", record_scores),
        "7": ("Show report card", show_report_card),
        "8": ("Class list (sorted)", show_class_list),
        "9": ("Class statistics", lambda: print(class_statistics(students))),
        "10": ("Save report to file", lambda: print("Saved to:", save_report_to_file(students))),
        "0": ("Exit", None),
    }
    while True:
        print("\n----- MENU -----")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        choice = input("Choose: ").strip()
        if choice == "0":
            save_students(students)
            print("Goodbye!")
            break
        elif choice in menu:
            try:
                menu[choice][1]()
            except Exception as e:
                print("Something went wrong:", e)
            finally:
                print()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
