# # Tính chất của OOP
# # 1. Kế thừa: cho phép lớp con kế thừa toàn bộ thuộc tính và phương thức từ lớp cha, 
# # giúp tái sử dụng code

# class Human:
#     def __init__(self, name):
#         self.name = name
    
#     def greeting(self):
#         print(f"Hello, my name is {self.name}")

# class Student(Human):
#     def __init__(self, name, grade):
#         super().__init__(name)

#         self.grade = grade
    
#     def study(self):
#         print(f"I'm studying, my grade is {self.grade}")

# class Teacher(Human):
#     def __init__(self, name, salary):
#         super().__init__(name)

#         self.salary = salary
    
#     def total_salary(self):
#         print(f"I'm teacher, my salary is {self.salary}")

# human1 = Human("Pham Van A")
# student1 = Student("Nguyen Van B", 9.0)
# teacher1 = Teacher("Mr.C", 5000000)

# teacher1.greeting()
# teacher1.total_salary()


