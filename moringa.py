from pprint import pp

class Employee:
    def __init__(self, first_name, last_name, salary, gender, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.gender = gender
        self.phone_number = phone_number
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def id(self):
        initials = f"{self.first_name[0]}{self.last_name[0]}"
        last_three_digits = self.phone_number[-3:]   
        return f"MS-{initials.upper()}-{last_three_digits}"     

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@moringaschool.com"


class Manager(Employee):
    def __init__(
        self,
        first_name,
        last_name,
        salary,
        gender,
        phone_number,
        department=None,
        employees=None,
    ):
        super().__init__(first_name, last_name, salary, gender, phone_number)
        self.department = department
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_employees(self):
        return [employee.fullname() for employee in self.employees]


class Instructor(Employee):
    def __init__(self, first_name, last_name, salary, gender, phone_number, course):
        super().__init__(first_name, last_name, salary, gender, phone_number)
        self.course = course

class Trainee(Employee):
    def __init__(self, first_name, last_name, salary, gender, phone_number, contract_duration):
        super().__init__(first_name, last_name, salary, gender, phone_number)
        self.contract_duration = contract_duration
        
    def list_trainees(self, trainee):
        pass

classroom_manager = Manager(
    "Benard", "Musau", "500000", "Male", "0712345678"
)

instructor1 = Instructor(
    "Jerald", "Nyaga", "200000", "Male", "0723456789", "Python Programming"
)
instructor2 = Instructor(
    "Nelson", "Murithi", "201000", "Male", "0755617262", "Java Programming"
)
instructor3 = Instructor(
    "Erick", "Mongare", "203000", "Male", "0723477789", "C++ Programming"
)

# ❗ Add instructors to the manager (this is what was missing)
classroom_manager.add_employee(instructor1)
classroom_manager.add_employee(instructor2)
classroom_manager.add_employee(instructor3)

print("Classroom Manager Details:")
pp({
    "Full Name": classroom_manager.fullname(),
    "ID": classroom_manager.id,
    "Email": classroom_manager.email,
    "Department": classroom_manager.department,
    "Employees": classroom_manager.list_employees()
})
print("\nInstructors Details:")
for instructor in classroom_manager.employees:
    pp({
        "Full Name": instructor.fullname(),
        "ID": instructor.id,
        "Email": instructor.email,
        "Course": instructor.course
    })
    print()
    
    
#create traneee
trainee1 = Trainee(
    "Jeavan" "Tyson", "500", "Male", "0711223344", "3 months"
)