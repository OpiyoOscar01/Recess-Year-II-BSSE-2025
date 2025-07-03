from datetime import date

# Base Class
class Person:
    def __init__(self, first_name, last_name, email, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birth_date = birth_date

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )


# Student Class
class Student(Person):
    def __init__(self, first_name, last_name, email, birth_date, student_id, program):
        super().__init__(first_name, last_name, email, birth_date)
        self.student_id = student_id
        self.program = program
        self.courses = []
        self.grades = {}

    def enroll(self, course):
        self.courses.append(course)

    def assign_grade(self, course, grade):
        if course in self.courses:
            self.grades[course] = grade

    def get_gpa(self):
        if not self.grades:
            return 0.0
        total_points = sum(self.grades.values())
        return round(total_points / len(self.grades), 2)


# Lecturer Class
class Lecturer(Person):
    def __init__(self, first_name, last_name, email, birth_date, staff_id, department):
        super().__init__(first_name, last_name, email, birth_date)
        self.staff_id = staff_id
        self.department = department
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)

    def list_courses(self):
        return self.courses_taught


# Staff Class
class Staff(Person):
    def __init__(self, first_name, last_name, email, birth_date, staff_id, role):
        super().__init__(first_name, last_name, email, birth_date)
        self.staff_id = staff_id
        self.role = role

    def get_role_description(self):
        return f"{self.full_name()} works as a {self.role}."


# Example usage
if __name__ == "__main__":
    # Student
    student = Student("Alice", "Johnson", "alice@uni.edu", date(2002, 5, 15), "S1001", "Computer Science")
    student.enroll("CS101")
    student.enroll("MA102")
    student.assign_grade("CS101", 4.0)
    student.assign_grade("MA102", 3.5)

    # Lecturer
    lecturer = Lecturer("Dr. Bob", "Smith", "bob@uni.edu", date(1980, 3, 20), "L2001", "Engineering")
    lecturer.assign_course("CS101")
    lecturer.assign_course("CS201")

    # Staff
    staff = Staff("Cathy", "Williams", "cathy@uni.edu", date(1975, 8, 30), "ST3001", "Registrar")

    # Output
    print(f"Student: {student.full_name()} ({student.program}) - GPA: {student.get_gpa()}")
    print(f"Lecturer: {lecturer.full_name()} - Teaches: {', '.join(lecturer.list_courses())}")
    print(f"Staff: {staff.get_role_description()}")
