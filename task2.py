class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

# Creating three student objects
student1 = Student("Mark Anthony Miralles", 20, "Information Technology II")
student2 = Student("Bob Narco ", 22, "Mathematics")
student3 = Student("Charlie Puth", 21, "Physics")

# Calling the introduce method for each student
student1.introduce()
student2.introduce()
student3.introduce()
