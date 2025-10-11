#danh sách
courses=['a','b','c' ]
print(courses)

#có thể truy cập độ dài của danh sách
courses=['a','b','c' ]
print(len(courses)) #giá trị đưa ra sẽ là 3 là số mục trong danh sách

#cũng thể truy cập các giá trị trong
courses=['a','b','c' ]
print(courses[0]) #đưa ra giá trị a

#hoặc có thể sử dụng số âm để truy cập như
courses=['a','b','c' ]
print(courses[-1]) #giá trị đưa ra là c và là giá trị cuỗi cùng

#nếu lấy 2 giá trị đầu
courses=['a','b','c' ]
print(courses[0:2]) #từ 0 đến 2 và không bao gồm 2 tương tự giông cắt lát 

#thêm và danh sách
courses=['a','b','c' ]
courses.append('d') #lệnh này giúp vào cuối danh sách nhưng là thêm cả chuỗi bao gồm [] chuỗi thêm vào sẽ đc coi như là 1 vị trí đếm trong chuỗi
print(courses)

#thêm vào vị trí mong muốn
courses=['a','b','c' ]
courses.insert(0,'d') #lệnh này chèn vào vị trí mong muốn trong chuỗi vd như vị trí số 0
print(courses)

#khi có nhiều giá trị muốn thêm vào danh sách
courses=['a','b','c' ]
courses_2=['1','2']
courses.insert(0,courses_2) #tương tự như chèn vào riêng lẻ các giá trị
print(courses)

#nhưng khi muốn đưa ra giá trị ở vị trí 0 thì py sẽ cho ra ['1','2'] bởi ta vừa gán giá trị đó vào vị trí 0

#ta có thể thêm vào như các mục trong danh sách bằng cách
courses=['a','b','c' ]
courses_2=['1','2']
courses.extend(courses_2)
print(courses)

#xóa giá trị trong danh sách
courses=['a','b','c' ]
courses.remove('a') #xóa giá trị theo mong muốn
print(courses)

#xóa giá trị cuối cùng của danh sách
courses=['a','b','c' ]
courses.pop() #xóa giá trị cuối cùng của danh sách
print(courses)

#ta có thể lấy giá trị vừa xóa đi bằng cách cài thêm biến và đưa ra 
courses=['a','b','c' ]
popped=courses.pop()
print(popped) #kết quả đưa ra giá trị được loại bảo từ lệnh courses.pop()
print(courses)

#câu lệnh đảo ngược danh sách
courses=['a','b','c' ]
courses.reverse()
print(courses)#đưa ra giá trị danh sách đảo ngược từ cuối lên đầu xếp lần lượt

#đưa các giá trị về lần lượt theo số thứ tụ hay theo bảng chữ cái
courses=['a','b','c' ]
num=['1','3','2']

num.sort()
courses.sort()
print(courses)
print(num)

#dưa ra các giá trị theo thứ tự giảm dần

courses=['a','b','c' ]
num=['1','3','2']

num.sort(reverse=True)
courses.sort(reverse=True) #True là giảm dần còn False là tăng dần
print(courses)
print(num)

#có thể tìm các giá min hoặc max bằng cách hoặc tính tổng
print(min(num))
print(max(num))
#print(sum(num))

#có thể tìm chỉ số của giá trị trong danh sách  bằng cách
course=['a','b','c' ]
print(course.index('b'))  #giá trị đưa ra 1

#nếu muốn kiểm tra trong danh sách có chưa giá trị đó không ta có thể sử dụng
courses=['a','b','c' ]
print('a' in course) #giá trị đưa ra sẽ là True nếu có hoặc False nếu không


courses=['a','b','c' ]
for item in course:
    print(item) #giá trị đưa ra sẽ giá trị không theo danh sách bỏi câu lệnh in đưa ra các giá trị theo từng dòng

#ta có thể liệt kê từng chỉ mục như sau
courses=['a','b','c' ]
for item in enumerate(course):
    print(item) #giá trị đưa ra sẽ theo từng hàng và có từng chỉ mục từ con số 0

#khi không muốn bắt đầu bằng số không ta sử dụng như sau
courses=['a','b','c' ]
for item in enumerate(course, start=1):
    print(item) #giá trị đưa ra sẽ chỉ mục từ 1

#nối các mục trong danh sách bằng cách
courses=['a','b','c' ]
course_str=', '.join(courses) #và có thể thay đổi cấc điểm nối
print(course_str)

#hoặc có thể đưa chuỗi về dạng danh sách bằng cách
courses=['a','b','c' ]
course_str=', '.join(courses)
new_list=course_str.split(', ') #lệnh này giúp xóa bỏ các điểm nối và đưa chuỗi thành danh sách
print(course_str)
print(new_list)

#kiểm tra giống và khác nhau không thực hiện cho danh sách ngoặc [] mà chỉ áp dụng {}

courses_1 = {'a','b','c'}
courses_2 = {'a','b','e'}

# Giao nhau (giống nhau)
print(courses_1.intersection(courses_2))  # {'a', 'b'}

# Khác nhau (có trong 1 mà không có trong 2)
print(courses_1.difference(courses_2))    # {'c'}
print(courses_2.difference(courses_1))    # {'e'}

# Hợp lại (mỗi phần tử chỉ 1 lần)
print(courses_1.union(courses_2))         # {'a','b','c','e'}

#tạo danh sách rỗng
my_list={}
print(my_list)
