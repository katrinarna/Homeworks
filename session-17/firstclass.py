class Student:
    """
    A class to represent a student and their enrolled courses.

    Attributes:
    name : The name of the student.
    student_id : The unique student ID.
    courses : A list of courses the student is enrolled in.
    """
    def __init__(self, name, student_id, courses):
        """
        Initialize a student with name, student ID, and optional courses list.
        """
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        """
        Enroll the student in a course if not already enrolled.

        Parameters:
        course : Name of the course to enroll in.

        Raises: ValueError If the course is already enrolled.
        """
        if course not in self.courses:
            self.courses.append(course)
        else:
            raise ValueError(f"Already enrolled in {course}.")

    def get_courses(self):
        """Return the list of courses the student is currently enrolled in."""
        return self.courses


student1 = Student("Kata", 287, [''])
print(student1.name)  

student1.enroll("Physics")
print(student1.courses)

student1.enroll("Math")
print(student1.courses)