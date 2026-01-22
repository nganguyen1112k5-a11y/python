# class Student:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'{self.name} + {self.age}'



# studen = Student('nguyen vawn a',21)
# print(studen)
# print(studen.name)
# print(studen.age)
# print(studen)


'''
Quy ước:
Trong OOP (lập trình hướng đối tượng), getter và setter là các phương thức dùng để:
Getter → lấy (đọc) giá trị của thuộc tính
Setter → gán (thay đổi) giá trị của thuộc tính
'''

'''
-Đóng gói - enscapsulation: bảo mật dự liệu

Phạm vi:
- public: bắt đầu tên không có gạch chân ở dưới
- priavte: __tên
- protected: _tên

'''


'''
Kế thừa:
-nhận biết được đặc điểm chung của nhiều đối tượng phân cấp
'''

# class Animal:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#     # def __str__(self):
#     #     return self.name

# class Dog(Animal):
#     def __init__(self, name, weight):
#         super().__init__(name, weight)
#     def sound(self):
#         return 'go'

# class Cat(Animal):
#     def __init__(self, name, weight):
#         super().__init__(name, weight)

# dog  = Dog('Ngo', 55)
# cat = Cat('Caty', 5 )
# print(dog.name)
# print(dog.sound())





'''
-Cách viết hàm overwrite
- Cách dùng static, phân biệt static và functional class
- Cách dùng data-class
- Cách sử dụng type hint trong data-class
'''

'''
overwrite: Những phương thức/ chức năng được tự động kích hoạt theo tình huống
'''
# class Songuyen:
#     def __init__(self,value):
#         self.value = value
#     def __add__(self, other: 'Songuyen'): #chú thích dữ liệu
#         dap_an = self.value + other.value
#         return Songuyen(value = dap_an)
#     def __str__(self):
#         return f'{self.value}'
    
# a = Songuyen(1)
# b = Songuyen(2)
# c = Songuyen(3)
# print(a + b + c)

'''
static là thuộc tính toàn cục thuộc về class được khởi tạo không cần phải thông qua theo cấp độ phạm vi (scope)
object < static < class
'''
# class Student:
#     dem = 0      # static thuộc tính của lớp
#     def __init__(self,name):
#         self.name = name
#         Student.dem +=1
    
# st = Student('a')
# st = Student('b')
# st = Student('c')
# print(Student.dem)

'''
static function: hàm toàn cục
- Không lệ thuộc vào đối tượng, sử dụng kông cần thông qua object
- có thể thêm thuộc tính  và không tạo đối tượng hay thuộc tính ban đầu sẽ tối ưu bộ nhớ
'''

# class Math:       #không cần khởi tạo đối tượng gọi thông qua tên lớp
#     @staticmethod
#     def add(a,b):
#         return a + b
    
#     @staticmethod
#     def sub(a,b):
#         return a - b
    
#     @staticmethod
#     def mul(a,b):
#         return a * b
    
# print(Math.add(2,4))

'''
function class:
- Chỉ hỗ trợ hàm chứ năng, không thể thêm thuộc tính vì đã khởi tạo đối tượng
'''
class Math():      #đã có sự khợi tạo đối tượng và gọi thông qua đối tượng
    def add(a,b):
        return a + b 

print(Math.add(1,2))


'''
data-class : lưu trữ dữ liệu, không có các phương thức chỉ cần chỉ số thuộc tính không cần init
'''

from dataclasses import dataclass

@dataclass
class User:
    username: str  #chú thích dữ liệu
    password: str  #chú thích dữ liệu

user = User(username = 'u1', password = '123')
print(user.username)





from typing import *
from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str
    phone: Optional[str]  #optional là phép hợp giữa kiểu dự liệu mà xác định và None 

user = User('u2', '123',123)
print(user.username)
print(user.phone)