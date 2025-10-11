#từ điển và từ khóa
student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']} #chuỗi , số nguyên, danh sách
print(student) #từ điển
print(student['name']) #name là từ khóa để truy cập và hiển thị trong từ điển

#hoặc có thể sủ dụng tương tự bằng cách
student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']} #chuỗi , số nguyên, danh sách

print(student.get('name')) #nếu truy cập key ko tồn tại giá tri đưa ra None

#hoặc có thể thay đổi giá trị đưa ra như sau
student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']} #chuỗi , số nguyên, danh sách

print(student.get('phone', 'Not Found'))

#có thể thêm hoặc cập nhật và biến
student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']} #chuỗi , số nguyên, danh sách
student['phone']='123456' #thêm vào từ điển
student['name']='minh ngoc' #sửa đổi trong từ điển
print(student)

#hoặc cập nhật bằng cách
student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']}
student.update({'phone':1234567, 'name':'minh ngoc'})
print(student)

#có thể xóa bằng cách
student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']}
del student['age']
print(student)

#có thể lấy giá trị xóa đi đó 
student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']}
age=student.pop('age') 
print(student) #kết quả đưa ra đã mất age
print(age)

#số lượng key hay chiều dài
student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']}
print(len(student))

#hiển thị all key và hiển thị giá trị
student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']}
print(student.keys())
print(student.values())

print(student.items()) #hiển thị các cặp khóa và cặp giá trị

for key in student:
    print(key) #cho ra các key
for values in student.items():
    print(values)  #cho ra các giá trị

