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
        initials = f"self.first_name[0]{self.last_name[0]}"
        phone_digits = self.phone_number[-3:]        
    

    @property
    def email(self):
        pass
    




class Manager:
    pass



class Instructor:
    pass