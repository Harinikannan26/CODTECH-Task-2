# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:48:37 2024

@author: harin
"""

class GradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def calculate_average(self):
        total_score = 0
        total_entries = 0
        for subject, grades in self.grades.items():
            total_score += sum(grades)
            total_entries += len(grades)
        return total_score / total_entries if total_entries > 0 else 0

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def get_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_summary(self):
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        gpa = self.get_gpa(average)

        print("\nGrade Summary:")
        print("--------------------")
        print(f"Subjects: {list(self.grades.keys())}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

# Main function
def main():
    tracker = GradeTracker()

    while True:
        print("\nMenu:")
        print("1. Add Grade")
        print("2. Display Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            subject = input("Enter the subject name: ")
            try:
                grade = float(input("Enter the grade (0-100): "))
                if 0 <= grade <= 100:
                    tracker.add_grade(subject, grade)
                else:
                    print("Invalid grade! Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numerical value.")

        elif choice == '2':
            tracker.display_summary()

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
