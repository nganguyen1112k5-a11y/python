class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} + {self.age}'



studen = Student('nguyen vawn a',21)
print(studen)
print(studen.name)
print(studen.age)
print(studen)


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

class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    # def __str__(self):
    #     return self.name

class Dog(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
    def sound(self):
        return 'go'

class Cat(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

dog  = Dog('Ngoc', 55)
cat = Cat('Caty', 5 )
print(dog.name)
print(dog.sound())
