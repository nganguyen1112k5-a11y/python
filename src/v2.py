



# #SCOPE   : GLOBAL AND NONLOCAL




# x = 'hello' 
# def test():
#     y = 'mau y'
#     print(y)
# test()  #in ra gia tri cua y

# x = 'hello' 
# def test():
#     y = 'mau y'
#     print(x)
# test() #in ra gia tri cua x

# x = 'hello' 
# def test():
#     y = 'mau y'
# test()
# print(y) #loi do khong tim thay gia tri cua y de in ra do gia tri cua y nam trong ham

# x = 'hello' 
# def test():
#     x = 'mau x'
#     print(x)
# test() #in ra x trong ham
# print(x) #in ra x ngoai ham

# # 'global'  khai bao rang dung bien x toan cuc 
# x = 'hello' 
# def test():
#     global x  #ap dung x cho ca ngoai ham
#     x = 'mau x'
#     print(x)
# test() #in ra x trong ham
# print(x) #in ra x trong ham


 
# def test(z):
#     x = 'mau x'
#     print(z)
# test('dinh nga') #in ra dinh nga do bien cuc bo in ra la z

# def test(z):
#     x = 'mau x'
#     print(x)
# test('dinh nga') #in ra mau x do bien cuc bo in ra la x


# def test(z):
#     x = 'mau x'
#     print(z)
# test('dinh nga')

# def min():
#     pass

# m = min([1, 2, 3, 4, 5])  #min() là giá trị toàn cục nên khi sau đó đưa min vào giá trị tích hợp sẽ gây mâu thuẫn
# print(m) 

# #ta có thể thay đổi biến toàn cục min() thành my_min() từ đó sẽ không gây mâu thuận giữ biến toàn cục và biến tích hợp

# def my_min():
#     pass
# m = min([1, 2, 3, 4, 5]) 
# print(m) #như vậy sẽ đưa ra được giá trị min của m


# #hàm trong hàm
# def outer():
#     x = 'out'

#     def inter():
#         x = 'inter'
#         print(x)

#     inter()
#     print(x)

# outer
# #kq inter va out

# def outer():
#     x = 'out'

#     def inter():
#         #x = 'inter'
#         print(x)

#     inter()
#     print(x)

# outer()

# #kq out out do biến cục bộ bên trong mất đi biến bên ngoài sẽ thay thế

# #khi đặt x bên trong sẽ không anh hưởng đến hàm bên ngoài 

# #và biến x bên ngoài có thể thay thế x bên trong nhưng biến bên trong không thể thay thế biến bên ngoài


# # nonlocal dùng để nhận diện x mới
# def outer():
#     x = 'out'

#     def inter():
#         nonlocal x
#         x = 'inter'
#         print(x)

#     inter()
#     print(x)
# outer() #in ra 2 lần inter 

# x = 'nga'

# def outer():
#     x = 'out'

#     def inter():
#         x = 'inter'
#         print(x)

#     inter()
#     print(x)

# outer()

# print(x)

# #làm tuần tự từ trong ra ngoài trong thiếu ngoài sẽ thay thế vào







# #3 Sling list




# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# #           0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# print(my_list[1]) #đưa ra giá trị chỉ mục trong danh sách

# print(my_list[0:5]) #ko bao gom 5

# print(my_list[2:])

# print(my_list[-7:-1])

# print(my_list[1:-2])

# print(my_list[:])  # ra all

# print(my_list[2:-1:2])    #[ đầu, cuối, bước nhảy]

# #không bao gồm giá trị cuối cùng


# #trích xuất giá trị trong chuôi

# x = 'nga'
# print(x[::-1]) #chạy ngược danh sách

# print(x[1:])#mất giá trị đầu tiên







# # # ##





# my = [] #tạo khối đâu ra
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for n in nums:
#     my.append(n) #append tạo đầu ra giá trị ngay liền kế tiếp giá trị trước
# print(my)
# # viết dưới dạng rút gọn
# my = [n for n in nums]
# print(my)

my = [] 
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for n in nums:
#     my.append(n*n) #in giá trị bình phương
# print(my)
# # viết dưới dạng rút gọn
# my = [n*n for n in nums]
# print(my)

# # viết tương tự:
# my = map(lambda n : n*n, nums)
# print(my) #đưa ra giá trị tương tự như trên


# ## kết hợp với for
# for n in nums:
#     if n%2 == 0:
#         my.append(n)
# print(my)
# # Đưa ra giá trị tương đương
# my = [n for n in nums if n%2 == 0] 


# for trong for
# for lit in 'abcd':
#     for n in nums:
#         my.append((lit,n))
# print(my)

#tương tự
# my = [(lit,n) for lit in 'abcd' for n in nums]
# print(my)


#zip sẽ ghép các phần tử tương ứng của nhiều danh sách thành cặp hoặc bộ
# lits = ['a','b','c','d','e','f','g','h','i','k','j']
# lit = ['a','b','c','d','e','f','g','h','i','k']

# print(list(zip(lits,lit))) #khi không có cùng số lượng ký tự kết quả in sẽ đến chuỗi có giá trị ít hơn và kết thúc

##tìm hiểu thêm


#lệnh set() loại bỏ các giá trị trùng lặp và chỉ in ra 1 lần duy nhất
a = [1,1,2,3,4,5,5,3,4,3,2,3]
# b = set(a)
# print(b)

# lệnh add() dùng đề thêm phần tử vào tập hợp và không thể thêm các giá trị đã có sẵn
# c = set()
# for x in a:
#     c.add(x) #chèn x vào trong c để sử dụng lệnh set
# print(c) 

# c = {n for n in a}
# print(c)  #in ra kết quả tương tự


# yield dùng trong hàm  để trả về từng giá trị một mà không kết thúc hàm ngay

# def my(nums):
#     for n in nums:
#         yield n*n
# my(nums)
# for i in my(nums):
#     print(i)   #in từng giá trị 1 theo từng hàm

# my = [i*i for i in nums] 
# print(my)     #in từng giá trị 1 theo mảng


# n = {i for i in a} #thay thế giống cho set
# print(n) 



# [ ] → hình vuông có “vị trí rõ ràng” → dùng cho list , chỉ mục

# { } → giống tập hợp trong toán → dùng cho set/dict

# ( ) → giống ngoặc toán học → dùng cho biểu thức và hàm , đặt biến



##



# sorted lệnh sắp sắp theo thứ tự tăng dần
li = [7,5,8,4,6,2,1,3,4,9,0]
# s_li = sorted(li)
# print(s_li)
# print(li)

#dùng tương tự với sort()
# li.sort()
# print(li)

# sorted(x) → “Tạo ra bản sao sắp xếp.”   làm thay đổi dữ liệu gốc 
# x.sort() → “Sắp xếp tại chỗ.”           không làm thay đổi dữ liệu


##xếp thoe thứ tự giảm dần chỉ cần thêm câu lệnh giảm là là đúng

#reverse là câu lệnh giúp đảo ngược thứ tự các phần tử trên danh sách

# s_li = sorted(li, reverse=True)
# print(s_li)
# print(li)

# # dùng tương tự với sort()
# li.sort(reverse=True)
# print(li)


# x = sorted(li)
# print(x)

#cũng làm việc tương tự với các giá trị trong từ diển hay kí tự chữ, số âm

# li = [-6,-5,-4,1,2,3]
# s_li = sorted(li, key=abs)
# s_li.reverse()
# print(s_li)




# # -------------------- ĐỊNH NGHĨA LỚP --------------------
# class test:
#     # Hàm khởi tạo (constructor): tự động chạy khi tạo một đối tượng mới của lớp test
#     def __init__(self, ten, tuoi, stt):
#         # self đại diện cho chính đối tượng đang được tạo ra
#         # Gán giá trị cho các thuộc tính (biến thành viên) của đối tượng
#         self.ten = ten    # Thuộc tính 'ten' (kiểu chuỗi) — lưu tên của đối tượng
#         self.tuoi = tuoi  # Thuộc tính 'tuoi' (kiểu số nguyên) — lưu tuổi
#         self.stt = stt    # Thuộc tính 'stt' (kiểu số nguyên) — lưu số thứ tự

#     # Hàm __repr__: quy định cách hiển thị đối tượng khi in ra (print)
#     def __repr__(self):
#         # Trả về chuỗi mô tả đối tượng theo định dạng "ten,tuoi,stt"
#         # Ví dụ: nếu đối tượng có ten='a', tuoi=20, stt=1 → sẽ hiển thị là "a,20,1"
#         return '{},{},{}'.format(self.ten, self.tuoi, self.stt)


# # -------------------- KHỞI TẠO CÁC ĐỐI TƯỢNG --------------------
# # Tạo 3 đối tượng của lớp test, mỗi đối tượng mang thông tin khác nhau
# s1 = test('a', 20, 1)   # Đối tượng 1: tên = a, tuổi = 20, stt = 1
# s2 = test('c', 13, 3)   # Đối tượng 2: tên = c, tuổi = 13, stt = 3
# s3 = test('b', 18, 2)   # Đối tượng 3: tên = b, tuổi = 18, stt = 2

# # -------------------- TẠO DANH SÁCH --------------------
# # Biến tests là danh sách (list) chứa 3 đối tượng vừa tạo
# tests = [s1, s2, s3]


# # -------------------- HÀM push --------------------
# # Hàm này được dùng để xác định “khóa sắp xếp” (sorting key)
# # Trong ví dụ này, ta sẽ sắp xếp các đối tượng dựa vào thuộc tính 'ten'
# def push(s_test1):
#     return s_test1.ten   # Trả về giá trị 'ten' của đối tượng s_test1


# # -------------------- SẮP XẾP DANH SÁCH --------------------
# # Hàm sorted() dùng để sắp xếp các phần tử trong danh sách
# # Cú pháp: sorted(iterable, key=<hàm_chọn_khóa>, reverse=<True/False>)
# # - iterable: dữ liệu cần sắp xếp (ở đây là danh sách 'tests')
# # - key: xác định thuộc tính hoặc giá trị dùng để so sánh khi sắp xếp
# # - reverse: nếu =True → sắp xếp GIẢM DẦN, nếu =False → sắp xếp TĂNG DẦN

# # Ở đây:
# #   key=push → hàm sorted() sẽ gọi hàm push() để lấy thuộc tính 'ten' làm tiêu chí sắp xếp
# #   reverse=True → sắp xếp GIẢM DẦN (Z → A)
# s_test1 = sorted(tests, key=push, reverse=True)


# # -------------------- IN KẾT QUẢ --------------------
# # Khi in danh sách s_test1, Python sẽ tự động gọi hàm __repr__() cho từng đối tượng
# # Nhờ vậy, thay vì in ra địa chỉ bộ nhớ, ta sẽ thấy dạng rõ ràng như "ten,tuoi,stt"
# print(s_test1)

# # Kết quả hiển thị sẽ là:
# # [c,13,3, b,18,2, a,20,1]
# # → Nghĩa là danh sách đã được sắp xếp theo thứ tự tên giảm dần: c → b → a







# # -------------------- ĐỊNH NGHĨA LỚP --------------------
# class test:
#     # Hàm khởi tạo (constructor): tự động chạy khi tạo một đối tượng mới của lớp test
#     def __init__(self, ten, tuoi, stt):
#         # self đại diện cho chính đối tượng được tạo ra
#         # Gán giá trị cho các thuộc tính (biến bên trong đối tượng)
#         self.ten = ten    # Thuộc tính 'ten' — kiểu chuỗi (string), dùng để lưu tên
#         self.tuoi = tuoi  # Thuộc tính 'tuoi' — kiểu số nguyên (int), dùng để lưu tuổi
#         self.stt = stt    # Thuộc tính 'stt' — kiểu số nguyên (int), lưu số thứ tự của đối tượng

#     # Hàm __repr__ quy định cách đối tượng được hiển thị khi in ra bằng print()
#     # Mục đích: giúp dễ đọc hơn khi in đối tượng (thay vì hiện địa chỉ bộ nhớ)
#     def __repr__(self):
#         # Trả về chuỗi mô tả đối tượng có dạng: "ten,tuoi,stt"
#         # Ví dụ: nếu ten='a', tuoi=20, stt=1 → sẽ in ra "a,20,1"
#         return '{},{},{}'.format(self.ten, self.tuoi, self.stt)


# # -------------------- KHỞI TẠO CÁC ĐỐI TƯỢNG --------------------
# # Tạo 3 đối tượng của lớp test, mỗi đối tượng có giá trị riêng cho tên, tuổi và số thứ tự
# s1 = test('a', 20, 1)   # Đối tượng 1: tên = a, tuổi = 20, stt = 1
# s2 = test('c', 13, 3)   # Đối tượng 2: tên = c, tuổi = 13, stt = 3
# s3 = test('b', 18, 2)   # Đối tượng 3: tên = b, tuổi = 18, stt = 2

# # -------------------- TẠO DANH SÁCH CHỨA CÁC ĐỐI TƯỢNG --------------------
# # Biến tests là một danh sách (list) gồm 3 đối tượng s1, s2 và s3
# tests = [s1, s2, s3]


# # -------------------- SẮP XẾP DANH SÁCH --------------------
# # Hàm sorted() dùng để sắp xếp các phần tử trong danh sách theo một tiêu chí nhất định
# # Cú pháp: sorted(iterable, key=<hàm_chọn_khóa>, reverse=<True/False>)
# #   - iterable: dữ liệu cần sắp xếp (ở đây là 'tests')
# #   - key: xác định thuộc tính hoặc giá trị dùng để so sánh khi sắp xếp
# #   - reverse: nếu =True thì sắp xếp giảm dần, mặc định =False là tăng dần

# # Ở đây:
# #   key=lambda e: e.ten  nghĩa là mỗi đối tượng e trong danh sách sẽ được sắp xếp dựa vào giá trị 'e.ten'
# #   (lambda e: e.ten là một hàm vô danh – nó trả về thuộc tính 'ten' của đối tượng e)
# #   reverse không được đặt, nên mặc định là False → sắp xếp TĂNG DẦN theo tên (A → Z)
# s_test1 = sorted(tests, key=lambda e: e.ten)


# # -------------------- IN KẾT QUẢ --------------------
# # Khi in danh sách s_test1, Python sẽ gọi tự động hàm __repr__() của từng đối tượng trong đó
# # Nhờ vậy, ta sẽ thấy nội dung hiển thị rõ ràng (thay vì dạng <__main__.test object at 0x...>)
# print(s_test1)
# # Kết quả hiển thị: [a,20,1, b,18,2, c,13,3]
# # → Danh sách đã được sắp xếp theo thứ tự tên: a, b, c


##định dạng chuôi

exm ={'name': 'Ngà', 'old': 20}
# a = 'my name is ' + exm['name'] + ' i am ' + str(exm['old'])
# print(a)

# #ta có thể dùng fomat trình giữ chỗ

# a = 'my name is {} , I am {} year old'.format(exm['name'],exm['old']) #chỉ mục #exm['name'] truy xuất từ bên ngoài vào trong format
# print(a) #my name is Ngà , I am 20 year old

# a = 'nga'
# b = 'dinh'
# c = '{0} {1} {0}'.format(a,b) #lấy chỉ mục trong trình giữ chỗ
# print(c) #nga dinh nga


#hoặc có thể viết

# a = 'my name is {0[name]} , I am {1[old]} year old'.format(exm,exm) #{0[name]} truy xuất từ bên trong format ra ngoài 
# print(a) #my name is Ngà , I am 20 year old

# a = 'my name is {0[name]} , I am {0[old]} year old'.format(exm)
# print(a)


#đổi cách trích xuất khác 
# l = ['Ngà',23]
# a = 'my name is {0[0]} , I am {0[1]} year old'.format(l) #trích xuất từ chỉ mục trong l

# class Person():
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old

# p1 = Person('Ngàa', '20')

# a = 'My name is {0.name} and I am {0.old} years old.'.format(p1) #[name] chỉ sử dụng trong từ điển
# # .name trích xuất giá trị trong biến p1
# print(a) #My name is Ngà and I am 20 years old.






# a = 'My name is {name} and I am {age} years old.'.format(name = 'ngà', age = 20)
# print(a)  #My name is ngà and I am 20 years old.


so = {'name': 'Ngà', 'age': 20}
# a = 'My name is {name} and I am {age} years old.'.format(**so) 
# # **so giải nén từ diển tương dương với .format(name='Ngà', age=20)

# print(a) #My name is Ngà and I am 20 years old.


# # *      → dùng cho danh sách, tuple, string (giải nén theo thứ tự).

# # **     → dùng cho dictionary (giải nén theo key=value).
# #có thể kết hợp trong format
# # Danh sách và dictionary
# values = [10, 20, 30]
# person = {'name': 'Ngà', 'age': 20}

# # Template với {} cho list và {key} cho dict
# template = "List values: {}, {}, {}. Name: {name}, Age: {age}"

# # Dùng * để giải nén list, ** để giải nén dictionary
# result = template.format(*values, **person)
# #giá trị danh sách {} không cần đưa giá trị chỉ thị giá trị từ điển cần từ khóa vào trong {name}
# print(result) #List values: 10, 20, 30. Name: Ngà, Age: 20


# for i in range(1,11):
#     a = 'đếm số:{}'.format(i)
#     print(a)

# for i in range(1,11):
#     a = 'đếm số:{:03}'.format(i) #{:03} định dạng giá trị gán vào bao gồm 3 chữ số
#     print(a)   #đếm số:001 ...


# pi = 3.1415926535
# a = 'pi bằng:{:.2f}'.format(pi) #định dạng giá trị gán vào số thập phân 2 chữ số
# print(a) #pi bằng:3.14

# # Dấu hai chấm : → bắt đầu phần định dạng cho giá trị.

# # .2 → hiển thị 2 chữ số sau dấu thập phân.

# # f → viết tắt của float (số thực), nghĩa là định dạng theo kiểu số thực thập phân.

# a = 'so thuc:{:,}'.format(10000**2) #ngăn cách giá trị bằng dấu ' , ' 
# print(a) #so thuc:100,000,000


# a = 'so thuc:{:,.2f}'.format(10000**2) #ngăn cách giá trị bằng dấu ' , ' 
# print(a) #so thuc:100,000,000.00

# import datetime

# my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# sentence = '{:%B %d, %Y}'.format(my_date)
# print(sentence)






##   thư viên os giúp truy cập và làm với các folder trên thiết bị



# import os
# print(dir(os)) #hiển thị thuộc tính và công thức của module os

import os
# print(os.getcwd())  #lấy thư mục làm việc hiện tại.
#C:\ABE\VSCODE\yt


# os.chdir('C:\ABE\VSCODE\yt')  #chuyển (thay đổi) thư mục làm việc hiện tại.
# print(os.getcwd()) 
#C:\ABE\VSCODE

# os.mkdir('test3.py')
# os.makedirs('test4')  #cả 2 dùng để tạo một thư mục mới trong thư mục hiện tại



# sự khác nhau giữa mkdir và makedirs:
# os.mkdir	    Tạo 1 thư mục duy nhất	
# os.makedirs	Tạo nhiều thư mục lồng nhau cùng lúc



# os.mkdir('test3')
# os.makedirs('test5\\test51')
# os.makedirs('test5\\test52')
# os.makedirs('test5\\test53')
# #           thư mục cha\\ thư mục con

# print(os.listdir())  #Liệt kê (list) tất cả tên file và thư mục có trong thư mục được chỉ định.
# print(os.listdir('test5'))   #['test51', 'test52', 'test53']
# print(os.listdir)

# os.rmdir('test3')     #Xóa một thư mục trống duy nhất.
# os.removedirs('test5\\test51')     #Xóa nhiều thư mục liên tiếp (lồng nhau) — cũng chỉ khi tất cả đều trống.

# print(os.listdir())


# os.rename('test3', 'test4')    #('tên tệp cũ' ,'tên tệp mới')
# print(os.listdir())


# xuất ra thông tin trong thu mục
# print(os.stat('src'))

#xuất ra kích thước mục
# print(os.stat('src').st_size)


#xuất ra thời gian chỉnh sửa
# print(os.stat('src').st_mtime)  #dạng số

#đổi thời qua thời gian thực
# from datetime import datetime
# a = os.stat('src').st_mtime
# print(datetime.fromtimestamp(a))  #in ra ngày giờ



      #  os.walk  liệt kê tất cả các thư mục con và file trong một thư mục gốc.
# for dirpath, dirnames, filenames in os.walk('C:\ABE\VSCODE\yt'):
#     print("Thư mục:", dirpath)        #Chuỗi đường dẫn của thư mục hiện tại
#     print("Thư mục con:", dirnames)   #Danh sách tên các thư mục con bên trong dirpath
#     print("Tệp tin:", filenames)      #Danh sách tên các tệp (files) trong dirpath
#     print("-----------------------")

#goi thư mục
# print(os.environ.get('test5'))  #None

# print(os.environ.get('HOME')) 
#nối các thư mục cũng dùng phép toàn tử + hoặc phép gán format như bình thường 


# print(os.path.basename('\\tmp\\test.txt'))  #test.txt
# #basename() → trả về tên của file hoặc thư mục cuối cùng trong đường dẫn.

# print(os.path.dirname('\\tmp\\test.txt'))  #\tmp
# #dirname() → trả về phần thư mục (folder path), bỏ phần tên file.

# print(os.path.split('\\tmp\\test.txt'))  #('\\tmp', 'test.txt')
# # split() → tách đường dẫn thành 2 phần:
# # (thư mục cha, tên file)

# print(os.path.exists('C:\ABE\VSCODE\yt')) #True
# # Dùng để kiểm tra đường dẫn có tồn tại (file hoặc thư mục).
# # Trả về True nếu có.
# # Trả về False nếu không

# print(os.path.isfile('test'))  #False
# #isfile() → kiểm tra xem đường dẫn có phải là một file hợp lệ hay không.

# print(os.path.splitext('\\tmp\\test.txt'))  #('\\tmp\\test', '.txt')
# # splitext() → tách tên file và phần mở rộng (đuôi).
# # '\\tmp\\test' là tên file (không có phần mở rộng)
# # '.txt' là phần mở rộng

# print(dir(os.path))






## File Object




#phuongw pháp mở tệp
# f = open('test.txt', 'w')     #vd: = open('C:/ABE/VSCODE/yt/.venv/test.text')

#nểu thực hiện các tệp ở các thư mục khác nhau thì cần truyền dường dẫn còn trong cùng 1 thu mực thì không cần

# #in ra tên tệp truy cập
# print(f.name)  #test.txt
# #in ra chế độ làm việc hiện tại
# print(f.mode)   #r
# # #đóng
# # f.close()

# 'r': chỉ đọc (read)

# 'w': ghi (ghi đè nội dung cũ)

# 'a': ghi nối thêm (append)

# 'x': tạo file mới (lỗi nếu file đã tồn tại)

# 'b': chế độ nhị phân (binary) – dùng cho ảnh, video,...

# 't': chế độ văn bản (text) – mặc định.

# Có thể kết hợp: 'rb', 'wb', 'rt', 'wt'...




#trình quản lý ngữ cảnh   

# with   được dùng để quản lý tài nguyên tự động, 
# giúp bạn mở – dùng – đóng tài nguyên (như file, kết nối mạng, luồng dữ liệu, khóa, v.v.) 
# một cách an toàn và gọn gàng.





# with open('test.txt', 'r') as f:
#     pass
# print(f.closed)   #True  
# # khi kết thúc khối with, file sẽ tự động đóng (không cần f.close()). nêu khi in ra nó sẽ là True

# with open('test.txt', 'r') as f:
#     print(f.closed)  # Trong khối with → file đang mở  #False
# print(f.closed)      # Ngoài khối with → file đã đóng  #True



# with open('src\\test.txt', 'r') as f:
#     a = f.read()
#     print(a)
# Ná»™i dung trong file: nguyá»…n Ä‘Ã¬nh ngÃ 
# ngÃ 
# ngaf nguyá»…n
# nguyen dinh nga


# with open('src\\test.txt', 'r') as f:
#     ab = f.readline()
#     print(ab)  #in dòng đầu tiên
#     ab = f.readline()
#     print(ab)  #in dòng thứ 2
# # 1 Ná»™i dung trong file: nguyá»…n Ä‘Ã¬nh ngÃ 

# # 2 ngÃ 
#


# with open('src\\test.txt', 'r') as f:
#     ab = f.readline()
#     print(ab,end='')  #thêm kết thúc câu mỗi câu sau sẽ không bị cách dòng
#     ab = f.readline()
#     print(ab,end='') 
# # 1 Ná»™i dung trong file: nguyá»…n Ä‘Ã¬nh ngÃ 
# # 2 ngÃ 


# with open('src\\test.txt', 'r') as f:
#     for line in f:
#         print(line,end='')  #tạo vòng lặp để in ra , kết thúc mỗi dòng bằng khoảng trống bên trong ''
# 1 Ná»™i dung trong file: nguyá»…n Ä‘Ã¬nh ngÃ 
# 2 ngÃ 
# 3 ngÃ  nguyá»…n
# 4 nguyen dinh nga


# with open('src\\test.txt', 'r') as f:
#     ab = f.read(20)
#     print(ab,end='')  #in 20 ký tự đầu tiên
# #1 Ná»™i dung trong f
#     ab = f.read(20)
#     print(ab,end='') #in thêm 20 kí tự nữa của tệp
# #khi quá ký tự trong tệp python sẽ in ra chuối rỗng



# with open('src\\test.txt', 'r') as f:

#     sizef = 10
    
#     ab = f.read(sizef) #yêu cầu đọc ra 10 ký tự
    
#     while len(ab) > 0:   #độ dài ab còn lại sau khi đọc
#         print(ab,end='') 
#         ab = f.read(sizef) #tiếp tục đọc thêm 10 ký tự và lặp lại cho đến khi len(ab) == 0
#     print('\nhet')  #\n để xuống dòng không dùng \n sẽ không thể xuống dòng do anh hưởng bởi end=''



# with open('src\\test.txt', 'r') as f:

#     sizef = 20
    
#     ab = f.read(sizef) 
#     print(ab,end='')  #in ra 20 kí tự

#     ab = f.read(sizef) 
#     print(ab,end='') #in tiếp 20 kí tự

#     print(f.tell())   #đọc vị trí làm  việc hiện tại




# with open('src\\test.txt', 'r') as f:

#     sizef = 20
    
#     ab = f.read(sizef) 
#     print(ab,end='*')  #in ra 20 kí tự

#     f.seek(0) #f.seek(0) nghĩa là đưa con trỏ quay lại đầu tệp (vị trí 0).
    
#     ab = f.read(sizef) 
#     print(ab,end='*') #in ra 20 kí tự

#     print(f.tell())   #    1 Noi dung trong fil*1 Noi dung trong fil*20
# #tell() là đọc vị trí làm việc hiện tại nên do khi seek() tìm kiếm vị trí 0 (đầu tệp) nên khi thực hiện xong telll chỉ đếm được kên 20


# # KHông thể đồng thời mở tệp để đọc và ghi cùng lúc

# with open('test2.txt', 'w') as f:
#     f.write('test')
#     f.write('nga')

# Khi mở tệp bằng 'w':
# Nếu tệp chưa tồn tại, Python sẽ tự động tạo mới tệp đó.
# Nếu tệp đã tồn tại, toàn bộ nội dung cũ sẽ bị xóa (ghi đè hoàn toàn)

