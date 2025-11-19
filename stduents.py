ALL_COURSES = [
    "Data Science",
    "Software Engineering",
    "DevOPS",
    "Cyber Security",
    "AI Engineering",
    "High School Bootcamp",
    "Product Design",
    "Data Analytics",
    "Data Analytics for HR Professionals",
    "Bio Tech",
]

# STUDENT CLASS DEFINITION
class Student:
    """
    The Student class represents a student enrolled at Moringa School.
    It contains instance variables (unique to each student), class variables
    (shared by all students), properties for controlled access, and methods.
    """
    
    # CLASS VARIABLES
    student_count = 0       # Tracks total number of Student instances created
    all_students = []       # Stores references to all student objects for easy access

    # CONSTRUCTOR METHOD
    def __init__(self, first_name, last_name, age, gender, student_id, course, instructor):
        """
        Called when a new Student object is created.
        Initializes instance variables using setters to enforce validation.
        Updates class variables to track all students.
        """
        # INSTANCE VARIABLES (WITH VALIDATION)
        self.first_name = first_name  # Triggers first_name setter for validation
        self.last_name = last_name    # Triggers last_name setter for validation
        self.age = age                # Triggers age setter for validation (>=18)
        self.gender = gender          # Triggers gender setter (Male/Female)
        self.student_id = student_id  # Unique ID for the student
        self.course = course          # Triggers course setter to check valid course
        self.instructor = instructor  # Name of the course instructor

        # UPDATE CLASS VARIABLES
        Student.student_count += 1           # Increment the total number of students
        Student.all_students.append(self)    # Add this student instance to the global list

    # FIRST NAME PROPERTY
    @property
    def first_name(self):
        """Getter: Returns the student's first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """Setter: Validates and sets the student's first name."""
        if not value or not isinstance(value, str):  # Must be a non-empty string
            raise ValueError("First name must be a non-empty string")
        self._first_name = value.strip().title()    # Capitalize first letter, remove extra spaces

    # LAST NAME PROPERTY
    @property
    def last_name(self):
        """Getter: Returns the student's last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """Setter: Validates and sets the student's last name."""
        if not value or not isinstance(value, str):  # Must be a non-empty string
            raise ValueError("Last name must be a non-empty string")
        self._last_name = value.strip().title()     # Capitalize first letter, remove extra spaces

    # AGE PROPERTY
    @property
    def age(self):
        """Getter: Returns the student's age."""
        return self._age

    @age.setter
    def age(self, value):
        """Setter: Validates that age is an integer >= 18."""
        if not isinstance(value, int):               # Age must be integer
            raise TypeError("Age must be an integer")
        if value < 18:                              # Enforce minimum age
            raise ValueError("Student must be at least 18 years old")
        self._age = value

    # GENDER PROPERTY
    @property
    def gender(self):
        """Getter: Returns the student's gender."""
        return self._gender

    @gender.setter
    def gender(self, value):
        """Setter: Ensures gender is either 'Male' or 'Female'."""
        allowed_genders = ["Male", "Female"]
        gender_normalized = value.capitalize()  # Capitalize input for consistency
        if gender_normalized not in allowed_genders:
            raise ValueError(f"Invalid gender: {value}. Allowed: {allowed_genders}")
        self._gender = gender_normalized

    # COURSE PROPERTY
    @property
    def course(self):
        """Getter: Returns the student's course."""
        return self._course

    @course.setter
    def course(self, value):
        """Setter: Validates that the course exists in ALL_COURSES."""
        if value not in ALL_COURSES:
            raise ValueError(f"{value} is not offered at Moringa School")
        self._course = value

    # FULLNAME PROPERTY
    @property
    def fullname(self):
        """Returns the student's full name by combining first and last names."""
        return f"{self.first_name} {self.last_name}"

    # EMAIL PROPERTY
    @property
    def email(self):
        """Generates student email based on first and last names."""
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    # CLASS METHODS
    @classmethod
    def total_students(cls):
        """Returns the total number of students (class variable)."""
        return f"The total number of students is: {cls.student_count}"

    @classmethod
    def student_list(cls):
        """Returns a list of students' full names using individual attributes."""
        return [f"{student.first_name} {student.last_name}" for student in cls.all_students]

    @classmethod
    def student_list_2(cls):
        """Returns a list of students' full names using the fullname property."""
        return [student.fullname for student in cls.all_students]

    # STATIC METHOD
    @staticmethod
    def reverse_name(first_name, last_name):
        """
        Static utility function to reverse the order of a name.
        Does not depend on instance or class.
        """
        return f"{last_name} {first_name}"

# Student Objects
student1 = Student(
    "Bradley", "Murimi", 40, "Male", "MSS-1234", "Software Engineering", "Fainus Mudahe"
)
student2 = Student(
    "Mariam",
    "Rashid",
    20,
    "Female",
    "MSS-1428",
    "Software Engineering",
    "Julius Mutindwa",
)
student3 = Student(
    "Fredrick",
    "Rangara",
    50,
    "Male",
    "MSS-1480",
    "Software Engineering",
    "Julius Mutindwa",
)
student4 = Student(
    "Adonis",
    "Pierre",
    30,
    "Male",
    "MSS-3445",
    "Bio Tech",
    "Julius Mutindwa",
)

print(Student.total_students())
print(Student.student_list())
print(Student.student_list_2())
print(Student.reverse_name("Alice", "Johnson"))