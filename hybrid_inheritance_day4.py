# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("Name:", self.name)


# Derived class 1
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display_student(self):
        self.display_person()
        print("Student ID:", self.student_id)


# Derived class 2
class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        super().__init__(name)
        self.sport_name = sport_name

    def display_sports_player(self):
        self.display_person()
        print("Sport Name:", self.sport_name)


# Hybrid inheritance class
class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        Person.__init__(self, name)
        self.student_id = student_id
        self.sport_name = sport_name
        self.college_name = college_name

    def display_college_student(self):
        self.display_person()
        print("Student ID:", self.student_id)
        print("Sport Name:", self.sport_name)
        print("College Name:", self.college_name)

student = CollegeStudent("Mehataj", "CS101", "Badminton", "ABC Engineering College")

student.display_college_student()