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


class Student:
    student_count = 0
    all_students = []

    def __init__(
        self, first_name, last_name, age, gender, student_id, course, instructor
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age              # uses setter
        self.gender = gender        # uses setter
        self.student_id = student_id
        self.course = course        # uses setter
        self.instructor = instructor

        Student.student_count += 1
        Student.all_students.append(self)

    # ------------------ COURSE PROPERTY ------------------
    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        if course in ALL_COURSES:
            self._course = course
        else:
            raise ValueError(f"{course} is not offered at Moringa School")

    # ------------------ AGE PROPERTY ------------------
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 18:
            raise ValueError("Student must be at least 18 years old")
        self._age = value

    # ------------------ GENDER PROPERTY ------------------
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        allowed_genders = ["Male", "Female"]

        # normalize capitalization
        gender_normalized = value.capitalize()

        if gender_normalized not in allowed_genders:
            raise ValueError(f"Invalid gender: {value}. Allowed: {allowed_genders}")

        self._gender = gender_normalized

    # ------------------ OTHER PROPERTIES ------------------
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    @classmethod
    def total_students(cls):
        return f"The total number of students is: {cls.student_count}"

    @classmethod
    def student_list(cls):
        return [f"{student.first_name} {student.last_name}" for student in cls.all_students]

    @classmethod
    def student_list_2(cls):
        return [student.fullname for student in cls.all_students]

    @staticmethod
    def reverse_name(first_name, last_name):
        return f"{last_name} {first_name}"
