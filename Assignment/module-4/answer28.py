#What relationship is appropriate for Course and Faculty?

class Faculty:
    def __init__(self, name):
        self.name = name
        self.courses = []  # Composition: Faculty has multiple Courses

    def add_course(self, course):
        self.courses.append(course)

class Course:
    def __init__(self, name, faculty):  # Association: Course is taught by a Faculty
        self.name = name
        self.faculty = faculty

# Example usage:
faculty1 = Faculty("Dr. Smith")
course1 = Course("Math 101", faculty1)
course2 = Course("Math 202", faculty1)

faculty1.add_course(course1)
faculty1.add_course(course2)

print(faculty1.courses)  # [course1, course2]
print(course1.faculty)  # Dr. Smith