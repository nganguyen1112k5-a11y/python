
# '''
# *Lập trình hướng đối tượng(OOP)

# - Lớp và đối tượng là hai khái niệm cốt lỗi trong lập trình hướng đối tượng
# Lớp (class) định nghĩa hình dạng của một đối tượng, và đối tượng được tạo ra dựa trên lớp đó.
# ví dụ:
# Class: Xe máy
# Object: Xe Wave biển 29, xe Vision màu đỏ
# Class: Sinh viên
# Object: Bạn An, bạn Bình

# '''
# #Tạo một lớp tên MyClass thuộc tính x:
# class MyClass:
#     x = 5

# #Tạo đối tượng tên p1 in ra giá trị của x:
# p1 = MyClass()
# print(p1.x)

# #Xóa đối tượng p1
# del p1

# #Tạo nhiều đối tượng
# p1 = MyClass()
# p2 = MyClass()
# p3 = MyClass()
# print(p1.x)
# print(p2.x)
# print(p3.x)

# '''
# Lưu ý: Mỗi đối tượng là độc lập và có bản sao riêng của các thuộc tính lớp.
# '''



# '''
# *Phương thức __init__()
# -Tất cả các lớp đều có một phương thức tích hợp sẵn được gọi là __init__(), phương thức này luôn được thực thi khi lớp được khởi tạo.
# -Phương pháp này __init__()được sử dụng để gán giá trị cho các thuộc tính của đối tượng, hoặc để thực hiện các thao tác cần thiết khi đối tượng được tạo ra.
# '''

# class Person:
#   def __init__(self, name, age):    #self thay cho đối tượng p1
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)

# print(p1.name)
# print(p1.age)

# '''
# -Phương thức này __init__()được gọi tự động mỗi khi lớp được sử dụng để tạo một đối tượng mới.
# -Không sử dụng __init__() thì phải thiết lập gán đối với thuộc tính 1 cách thủ công 
# -Có thể đặt giá trị mặc định cho các tham số trong __init__()phương thức (def __init__(self, name, age=18):)
# '''


# '''
# * Tham số tự  tham chiếu

# - Tham số tự thân (self = bản thân đối tượng)
# - Tham số self phải là tham số đầu tiên của bất kỳ phương thức nào trong lớp.
# -Nếu không có từ khóa self, Python sẽ không biết bạn muốn truy cập thuộc tính nào của đối tượng
# -Và không nhất thiết là tên self, có thể thay đổi thành tên khác nhưng self là quy ước chung để dễ đọc và hiểu
# '''

# #Truy cập các thuộc tính bằng chính nó và gọi 1 phương thức từ một phương thức khác
# class SinhVien:
#     def __init__(self, ten, diem):      #self thay thế cho đối tượng hiện tại là sv
#         self.ten = ten                  # self.thuoc_tinh
#         self.diem = diem

#     def hien_thi(self):
#         return self.ten

#     def xin_chao(self):
#        nga = self.hien_thi()            #self.phuong_thuc
#        print(f'xin chao {nga}')

# sv = SinhVien("An", 8.5)
# sv.xin_chao()               


# #Thuộc tính của lớp
# '''
# Thuộc tính là các biến thuộc về một lớp. Chúng lưu trữ dữ liệu cho mỗi đối tượng được tạo ra từ lớp đó.
# -Truy cập vào thuộc tính của đối tượng bầng dấu chấm 
# +(p1.name: truy cập vào thuộc tính tên của đối tượng p1)

# -Sửa đối thuộc tính bằng cách truy cập vào thuộc tính và gán giá trị vào thuộc tính đó 
# +(p1.name = "ngà")

# - xóa thuộc tính sử dụng  del 
# +(del p1.name)

# _Thuộc tính của lớp không ở bên trong __init__() nằm ở ngoài các phương thức và được chia sẻ bởi tất cả các đối tương

# -Sửa đổi thuộc tính của lớp
# (lớp.thuộc tính = giá trị)

# _Thêm thuộc tính mới
# (p1.thuộc tính mới = giá trị)
# '''
# class Person:
#     # Thuộc tính của lớp (không nằm trong __init__)
#     species = "Human"

#     def __init__(self, name, age):
#         # Thuộc tính đối tượng
#         self.name = name
#         self.age = age

# # Tạo đối tượng
# p1 = Person("An", 20)
# p2 = Person("Bình", 22)

# # 1. Truy cập thuộc tính bằng dấu chấm
# print(p1.name)        # An
# print(p1.species)     # Human

# # 2. Sửa đổi thuộc tính đối tượng
# p1.name = "Ngà"
# print(p1.name)        # Ngà

# # 3. Xóa thuộc tính của đối tượng
# del p1.name
# # print(p1.name)      # ❌ AttributeError

# # 4. Sửa đổi thuộc tính của lớp
# Person.species = "Homo sapiens"
# print(p1.species)     # Homo sapiens
# print(p2.species)     # Homo sapiens

# # 5. Thêm thuộc tính mới cho đối tượng
# p1.country = "Viet Nam"
# print(p1.country)     # Viet Nam


# '''
# -Phương thức của lớp : tất cả các phương thức của lớp đều phải có self là tham số đầu tiên:
# +def add(self):
# -Các phương thức có thể nhận tham số như các hàm thông thường
# +def add(self, a, b):
# - Các phương thức có thể truy cập và thay đổi các thuộc tính bằng self
# + self.age += 1
# -Phương thức __str__ kiểm soát giá trị trả về khi in ra

# -Tương tự cũng có thể xóa phương thức ra khỏi lớp như xóa thuộc tính bằng cách sử dụng del

# '''
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # 1. Phương thức có self là tham số đầu tiên
#     def add(self):
#         print("This is a method without extra parameters")

#     # 2. Phương thức nhận tham số như hàm bình thường
#     def add_numbers(self, a, b):
#         return a + b

#     # 3. Phương thức truy cập và thay đổi thuộc tính bằng self
#     def birthday(self):
#         self.age += 1
#         print(self.age)

#     # 4. Phương thức __str__ kiểm soát khi in đối tượng
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"

# # Tạo đối tượng
# p1 = Person("Ngà", 20)

# # Gọi các phương thức
# p1.add()
# print(p1.add_numbers(3, 5))   #8
# p1.birthday()  #21
# p1.birthday()  #22
# #In đối tượng → gọi __str__()
# print(p1)  #Name: Ngà, Age: 22   khi in đối tượng trong 1 lớp mà không đi theo phương thức  hay thuộc tính nào thì sẽ in ra theo __str__ nếu ko có __str__ sẽ ko in ra 

# # 5. Xóa phương thức khỏi lớp
# del Person.add_numbers
# # p1.add_numbers(1, 2)  # ❌ AttributeError


# '''
# *Kế thừa trong Python
# -Kế thừa cho phép chúng ta định nghĩa một lớp kế thừa tất cả các phương thức và thuộc tính từ một lớp khác.
# -Lớp cha là lớp được kế thừa từ đó, còn được gọi là lớp cơ sở.
# -Lớp con là lớp kế thừa từ một lớp khác, còn được gọi là lớp dẫn xuất.
# - và có thể kế thừa từ nhiều lớp cha ngăn cách hau bởi dấu phẩy 
# '''
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def birthday(self):
#         self.age += 1
#         print(f"{self.name} is now {self.age} years old")

#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"


# # Lớp con kế thừa
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     # ghi đè birthday()  
#     def birthday(self):         #sẽ chỉ in ra birthday được ghi đè lên
#         print(f"Student {self.student_id} just had a birthday 🎉")

#     def study(self, subject):
#         print(f"{self.name} is studying {subject}")

#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}"


# # Sử dụng
# s1 = Student("Ngà", 20, "SV001")

# s1.birthday()
# s1.study("Python")
# print(s1)



# '''
# *Đóng gói 
# Đóng gói là giấu dữ liệu bên trong lớp và chỉ cho phép truy cập thông qua các phương thức an toàn.( Không thể truy cập trực tiếp vào các thuộc tính riêng tư từ bên ngoài lớp)
# - Nhận đình và thiết lập giá trị chỉ có thể thông qua phương pháp
# -có thuộc tính riêng tư và phương pháp riêng tư
# '''
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner              # public
#         self.__balance = balance        # private attribute (tài sản riêng tư)

#     # setter có kiểm soát (thiết lập bảo vệ)
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.__log_transaction("Deposit", amount)
#         else:
#             print("Amount must be positive")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             self.__log_transaction("Withdraw", amount)
#         else:
#             print("Invalid withdrawal")

#     # getter
#     def get_balance(self):
#         return self.__balance

#     # private method (phương thức riêng tư)
#     def __log_transaction(self, action, amount):
#         print(f"{action}: {amount}")
# acc = BankAccount("Ngà", 1000)

# acc.deposit(500)
# acc.withdraw(300)

# print(acc.get_balance())

# # Lớp nội bộ

# class Company:
#     def __init__(self, name):
#         self.name = name

#     def show_company(self):
#         print(f"Company: {self.name}")

#     # ===== LỚP NỘI BỘ CẤP 1 =====
#     class Department:
#         def __init__(self, dept_name, company):
#             self.dept_name = dept_name
#             self.company = company   # tham chiếu tới lớp ngoài

#         def show_department(self):
#             print(f"Department: {self.dept_name}")
#             print(f"Belongs to company: {self.company.name}")

#         # ===== LỚP NỘI BỘ CẤP 2 =====
#         class Employee:
#             def __init__(self, emp_name, department):
#                 self.emp_name = emp_name
#                 self.department = department  # tham chiếu tới Department

#             def show_employee(self):
#                 print(f"Employee: {self.emp_name}")
#                 print(f"Department: {self.department.dept_name}")
#                 print(f"Company: {self.department.company.name}")
# company = Company("OpenAI")
# company.show_company()

# dept = Company.Department("IT", company)
# dept.show_department()

# emp = Company.Department.Employee("Ngà", dept)
# emp.show_employee()




#chuỗi phương thức 
# class Car:
    
#     def turn_on(self):
#         print("You start the engine")
#         return self
    
#     def drive(self):
#         print("You drive the car")
#         return self
    
#     def brake(self):
#         print("You step on the brakes")
#         return self
    
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
# #cần return self bởi khi car.turn_on sẽ trả về self như vậy sẽ có thể thực hiện tiếp các lệnh sau đó 

# car = Car()
# car.turn_on().drive().brake().turn_off()  
# #hoặc sử dụng
# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()


#các lớp trừu tượng
#Lớp trừu tượng (Abstract Class) là một lớp dùng để làm khuôn mẫu, không dùng để tạo đối tượng trực tiếp, mà để các lớp con kế thừa và triển khai chi tiết
# các lớp con phải có các phương thức của lớp cha

from abc import ABC, abstractmethod

# Lớp trừu tượng
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


# Lớp con 1
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def draw(self):
        print("Vẽ hình chữ nhật")


# Lớp con 2
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def draw(self):
        print("Vẽ hình tròn")


# Sử dụng
s1 = Rectangle(4, 5)
s2 = Circle(3)

print(s1.area())   # 20
s1.draw()

print(s2.area())   # 28.26
s2.draw()



#Duck typing
#Nếu một object có đúng phương thức cần dùng, thì ta dùng nó,không cần quan tâm nó thuộc lớp nào.
class Dog:
    def sound(self):
        print("Gâu")

class Cat:
    def sound(self):
        print("Meo")

class Car:
    def sound(self):
        print("Bíp bíp")
def make_sound(obj):
    obj.sound()    # không cần biết obj là Dog, Cat hay Car
d = Dog()
c = Cat()
x = Car()

make_sound(d)   # Gâu
make_sound(c)   # Meo
make_sound(x)   # Bíp bíp


