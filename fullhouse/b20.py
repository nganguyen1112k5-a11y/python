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
# '''
# class Songuyen:
#     def __init__(self,value = int):    #int chỉ để gọi ý ko ảnh hưởng khi mk nhập str hay float
#         self.value = value
#     def __add__(self, other: 'Songuyen'): #chú thích dữ liệu khi chưa xây dụng xong hay chưa làm việc sau cần cho vào trong nháy đơn
#         return Songuyen(self.value + other.value)
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
Static method
Là hàm nằm trong class
Không dùng self, không lệ thuộc object
Gọi trực tiếp qua tên class
Dùng cho các hàm tiện ích / logic độc lập
Có thể dùng thuộc tính cấp lớp
Không có trạng thái riêng
'''

# class Math: 
#     def __init__(self):
#         pass                    
#     @staticmethod                #giúp biến hàm bên trong thành 1 phương tĩnh nó được coi như 1 hàm tiện ích không ảnh hưởng đến class hay object
#     def add(a,b):                #nếu ko có decorator hàm sẽ lỗi do python nghĩ a = self
#         return a + b
    
#     @staticmethod
#     def sub(a,b):
#         return a - b
    
#     @staticmethod
#     def mul(a,b):
#         return a * b
# sv = Math()
# print(Math.add(2,4))
# print(sv.sub(7,5))              #có thể gọi hàm tiện ích thông qua object

'''
function class:
- Chỉ hỗ trợ hàm chứ năng, không thể thêm thuộc tính vì đã khởi tạo đối tượng
'''
# class Math():      #đã có sự khợi tạo đối tượng và gọi thông qua đối tượng
#     def add(a,b):
#         return a + b 

# print(Math.add(1,2))


'''
dataclass

Dùng để lưu trữ dữ liệu (data holder)

Python tự sinh __init__, __repr__, __eq__…

Có thể có phương thức hoặc không

Chỉ cần khai báo thuộc tính + kiểu dữ liệu
'''

# from dataclasses import dataclass

# @dataclass
# class User:
#     username: str  #chú thích dữ liệu nên dùng khi truyền vào không dúng vẫn sử dụng được bth nếu phương thức tính hợp lệ
#     password: str  #chú thích dữ liệu

# user = User(username = 'u1', password = '123')
# print(user.username)





# from typing import Optional
# from dataclasses import dataclass

# @dataclass
# class User:
#     username: str
#     password: str
#     phone: Optional[str]  #optional (không bắt buộc) là phép hợp giữa kiểu dự liệu mà xác định và None 
'''kiểu type hint'''
# user = User('u2', '123',123)
# print(user.username)
# print(user.phone)





# class dem:
#     mnv = 0
#     def __init__(self,name):
#         self.name = name
#         dem.mnv += 1          
#         self.id = dem.mnv             #giup
#     def __str__(self):
#         return f'NV0{self.id} {self.name}'
# nv1 = dem('nga')
# nv2 = dem('ngaff')
# print(nv1)
# print(nv2)



# class A:
#     def __init__(self, x):
#         self.x = x

#     def __add__(self, other):            #hàm cộng thêm và nó sẽ thực hiện cộng a1+a2 trước sau thực hiện dần sau đó
#         return A(self.x + other.x)

#     def __str__(self):
#         return str(self.x)
# a1 = A(2)
# a2 = A(3)
# a3 = A(4)

# print(a1 + a2 + a3)





# class Test:
#     def __init__(self,A):
#         self.A = A
#     def tong(self):
#         tong1 = 0
#         for i in self.A:
#             tong1 +=i
#         return tong1
            
#     def __str__(self):
#         return str(self.tong()/len(self.A))
    
# a = [1,2,3,4,5,6] 
# b = Test(a)
# print(b)
        


# from typing import *
# class Student:
#     ds_std: List['Student'] = []
#     stt = 1

#     def __init__(self,
#                     name: str,
#                     class_code: str,
#                     bod: str,
#                     gpa: float,
#                  ):
        
#         self.name = self.standardlize_name(value=name)
#         self.class_code = class_code
#         self.bod = self.standardlize_birthday(value=bod)
#         self.gpa = gpa
#         self.mssv = self.create_id_student()

#         Student.ds_std.append(self)

#     def create_id_student(self):
#         value = 'SV' + f"{Student.stt}".zfill(3)
#         Student.stt+=1
#         return value

#     def standardlize_birthday(self, value: str):
#         dd, mm, yyyy = value.split('/')
#         dd = '0' + dd if dd.__len__() == 1 else dd
#         mm = '0' + mm if mm.__len__() == 1 else mm
#         return '/'.join([dd,mm,yyyy])

#     def standardlize_name(self, value: str):
#         step1 = value.strip().title()
#         step2 = ' '.join(step1.split())
#         return step2    
#     @staticmethod
#     def print_descreased_gpa():
#         res = sorted(Student.ds_std, key=lambda obj: -obj.gpa)
#         res = list(res)
#         for obj in res:
#             print(obj.mssv, obj.name, obj.class_code, obj.bod, f'{obj.gpa:.2f}')

# n = int(input())
# while n:
#     Student(input(), input(), input(), float(input()))
#     n -= 1

# Student.print_descreased_gpa()



# Abstraction class là hình thức tổ chức code nghiêm ngặt có qui tắc, không được làm sai yêu cầu


class Sinhvien:
    ds = []
    stt = 0
    def __init__(self,name,my_class,bod,gpa):
        self.name = self.chuan_hoa_ten(name)
        self.bod = self.chuan_hoa_ngay(bod)
        self.my_class = my_class
        self.gpa = gpa
        self.msv = self.ma_sinh_vien()
        Sinhvien.ds.append(self)
    def chuan_hoa_ngay(self,bod):
        d,m,y = bod.split('/')
        return f'{d.zfill(2)}/{m.zfill(2)}/{y}'
    def chuan_hoa_ten(self,name):
        return name.title()
    def ma_sinh_vien(self):
        Sinhvien.stt +=1
        return f'SV{str(Sinhvien.stt).zfill(3)}'
    @staticmethod
    def tra_ve():
        a = sorted(Sinhvien.ds, key= lambda x: (-x.gpa,int(x.msv[2:])))
        for i in a:
            print(i)
        
n = int(input())
for i in range(n):
    Sinhvien(input(),input(),input(),float(input()))
Sinhvien.tra_ve()