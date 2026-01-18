# #đưa ra giá trị văn bản
# print('hello world')

# #đưa ra giá trị văn bản bằng biến 'message'
# message='hello world 1'
# print(message)

# #nếu biến có nhiều từ ta sử dụng dấu gạch dưới để ngăn cách 
# my_message='hello world 2'
# print(message)
# #thường để tên biến dễ hiểu mang thông diệp để dễ nhận dạng không nên viết tắt

# # và dữ liệu văn bản này đuocj gọi là chuỗi

# #sự khác nhau của dấu nháy đơn và dấu nháy kép

# # message='hello's world 1' sẽ bị lỗi do py mặc định '  sẽ kết thúc chuôi và py không biết làm gì theo sau nó nếu chạy lệnh lập tức sẽ xảy ra lỗi

# #thay vậy ta nên dùng dấu nháy kép
# message="hello's world 3"
# print(message)

# #hoặc có thể sử dụng ngoặc lại 
# message='hello"s world 4'
# print(message)

# #hoặc có thể sử dụng dấu gạch chéo ngược "\" để thoát thì py sẽ cho rằng \' không phải để kết thúc chuỗi mà bỏ qua
# message='hello\'s world 5'
# print(message)

# #muốn tạo chuỗi nhiều dòng ta sur dụng 3 dấu nháy kép """ đầu và cuối
# message="""hello's world
# xin chào"""
# print(message)

# #muốn đếm độ dài chuỗi theo kí tự ta thực hiện hàm lend
# message='hello world'
# print(len(message))

# #có thể truy cập vào các vị trí trong chuỗi
# message="hello's world "
# print(message[0])

# # [] gọi là chỉ mục cắt lát

# #nếu muốn lấy 1 phần trong chuỗi
# message="hello's world"
# print(message[0:5]) #lấy từ không đến 5 và không bao gồm 5

# #hoặc có thể viết 
# message='hello world'
# print(message[:5])

# #hay có thể lấy giá trị từ 5 đến cuối
# message='hello world'
# print(message[5:11])

# # hay có thể viết
# message='hello world 1'
# print(message[5:])

# #thiết lập chuỗi về ký tự thường
# message='Hello World'
# print(message.lower())

# #thiết lập chuỗi về ký tự hoa
# message='hello world'
# print(message.upper())

# #thiết lập đối số trùng lặp
# message='hello world 1'
# print(message.count('l')) #đưa ra số lượng ký tự'l' trong chuỗi 2

# #có thể tìm kiếm ký tự bắt đầu từ ký tự số bằng cách
# message='hello world'
# print(message.find('l')) #đưa ra vị trí ký tự 'l' đầu tiên là 2

# #nếu từ cần tìm không có trong chuỗi thì py sẽ trả về giá trị âm

# #nếu muốn thay thế ký tự trong chuỗi bằng bằng ký tự khác
# message='hello world'
# message.replace('world','minh ngoc') #sau dấu , sẽ là ký tự thay thế cho ký tự trước dấu , trong chuỗi
# print(message)
# #nhưng khi không thay đổi biến đầu ra thì kết quả đưa ra vẫn là giá trị khi chưa thay thế
# message='hello world'
# new_message=message.replace('world','minh ngoc') 
# print(new_message)
# # sau khi đã thực hiến lệch thay thế của biến mới ta có thể đưa lại về biến ban đầu mà giá trị cho ra đã được thay thế
# message='hello world'
# message=message.replace('world','minh ngoc') 
# print(message)

# #kết hợp thông điệp bằng toán tử +
# greeting='hello'
# name='minh ngoc'

# message=greeting+name

# print(message) 
# #giá trị đưa ra sẽ là hellominh ngoc các ký tự sẽ không có khảng cách với nhau
# #thay vào vậy ta có thể sử dụng thêm kí tự cách sau chuỗi hay thực hiện phép toán thêm khoảng trống ' '
# greeting='hello'
# name='minh ngoc'

# message=greeting+' '+name+' welcome'  

# print(message) 

# #có thể nối các chuỗi lại với nhau bằng cách gọi là định dạng chuỗi giữ chỗ
# greeting='hello'
# name='minh ngoc'

# message='{}, {} welcome'.format(greeting,name)  

# print(message) 
# #hoặc ta có thể viết như sau
# greeting='hello'
# name='minh ngoc'

# message=f'{greeting}, {name} welcome' 

# print(message)

# #hoặc có thể viết in hoa hay im thường bằng cách chèn trực tiếp vào biến
# greeting='hello'
# name='minh ngoc'

# message=f'{greeting}, {name.upper()} welcome' 

# print(message)

# #lệnh có thể xem các phương pháp có thể thực hiện trên biến
# greeting='hello'
# name='minh ngoc'

# print(dir(name))

# #hoặc có thể sử dụng hàm trờ giúp để biết thêm đc nhiều thông tin hơn nhưng không thể nhập trực  tiếp biến vào đc mà phải thực hiện bằng
# greeting='hello'
# name='minh ngoc'

# print(help(str))
# #và có thể tìm thông tin thấp hơn 
# greeting='hello'
# name='minh ngoc'

# print(help(str.lower))

# #Dữ liệu số nguyên và số thực

# #số nguyên int
# num=3
# print(type(num)) #giá trị đưa ra sẽ là số nguyên int

# #số thực float
# num=3.14
# print(type(num)) #giá trị đưa ra sẽ là sô thực float

# #phép toán tử trong py

# print(3+2)

# print(3-2)

# print(3*2)

# print(3/2) 

# print(3//2) #phép chia lấy phần nguyên không lấy giá trị sau dấu phẩy

# print(3**2) #phép thực hiện lũy thừa vd là 3 mũ 2 

# print(3%2) #phép thực hiện chia lấy phần dư vd là 3 chia 2 bằng 1 lấy phần dư là 1

# #cũng có thể sử dụng dấu ngoặc đơn để thưc hiện thứ tự các phép tính giống ta thực hiện bình thường

# #phép toán tử số học
# num=1
# num=num+1
# print(num)

# #hoặc có thể dùng như sau
# num=1
# num+=1
# print(num) #giá trị cho ra vẫn là num +1

# #hay cũng dùng tương tự với các phép toàn khác
# num=1
# num*=10
# print(num) #giá trị cho ra là 10

# #các phép giá trị biến đổi số

# #abs hàm giá trị tuyệt đối
# print(abs(-3)) 

# #hàm round hàm thực hiện đưa giá trị về số nguyên gần nhất

# print(round(1.85))#giá trị đưa ra là 2

# #hoặc có thể làm tròn số đến giá trị bao nhiêu sau dấu thập phân

# print(round(3.85,1)) #giá trị đưa ra là 3.8 tức làm tròn đến vị trí thứ nhất sau dấu thập phân

# #phép so sánh và sẽ đưa ra giá trị yes hoặc no

# num_1=3 # dáu = ở đây là phép gán\
# num_2=2

# print(num_1==num_2) #phép so sánh bằng

# print(num_1!=num_2) #phép so sánh không bằng

# print(num_1>num_2) 

# print(num_1<num_2)

# print(num_1>=num_2) 

# print(num_1<=num_2)

# #chuối số nguyên
# num_1='100'
# num_2='200'
# print(num_1+num_2) #nó là nối các chuối

# #để đổi thành dạng số nguyên ta có thể dùng
# num_1='100'
# num_2='200'
# num_1=int(num_1)
# num_2=int(num_2)
# print(num_1+num_2) #giá trị đưa ra sẽ la 300 như mong muốn


# #danh sách
# courses=['a','b','c' ]
# print(courses)

# #có thể truy cập độ dài của danh sách
# courses=['a','b','c' ]
# print(len(courses)) #giá trị đưa ra sẽ là 3 là số mục trong danh sách

# #cũng thể truy cập các giá trị trong
# courses=['a','b','c' ]
# print(courses[0]) #đưa ra giá trị a

# #hoặc có thể sử dụng số âm để truy cập như
# courses=['a','b','c' ]
# print(courses[-1]) #giá trị đưa ra là c và là giá trị cuỗi cùng

# #nếu lấy 2 giá trị đầu
# courses=['a','b','c' ]
# print(courses[0:2]) #từ 0 đến 2 và không bao gồm 2 tương tự giông cắt lát 

# #thêm và danh sách
# courses=['a','b','c' ]
# courses.append('d') #lệnh này giúp vào cuối danh sách nhưng là thêm cả chuỗi bao gồm [] chuỗi thêm vào sẽ đc coi như là 1 vị trí đếm trong chuỗi
# print(courses)

# #thêm vào vị trí mong muốn
# courses=['a','b','c' ]
# courses.insert(0,'d') #lệnh này chèn vào vị trí mong muốn trong chuỗi vd như vị trí số 0
# print(courses)

# #khi có nhiều giá trị muốn thêm vào danh sách
# courses=['a','b','c' ]
# courses_2=['1','2']
# courses.insert(0,courses_2) #tương tự như chèn vào riêng lẻ các giá trị
# print(courses)

# #nhưng khi muốn đưa ra giá trị ở vị trí 0 thì py sẽ cho ra ['1','2'] bởi ta vừa gán giá trị đó vào vị trí 0

# #ta có thể thêm vào như các mục trong danh sách bằng cách
# courses=['a','b','c' ]
# courses_2=['1','2']
# courses.extend(courses_2)
# print(courses)

# #xóa giá trị trong danh sách
# courses=['a','b','c' ]
# courses.remove('a') #xóa giá trị theo mong muốn
# print(courses)

# #xóa giá trị cuối cùng của danh sách
# courses=['a','b','c' ]
# courses.pop() #xóa giá trị cuối cùng của danh sách
# print(courses)

# #ta có thể lấy giá trị vừa xóa đi bằng cách cài thêm biến và đưa ra 
# courses=['a','b','c' ]
# popped=courses.pop()
# print(popped) #kết quả đưa ra giá trị được loại bảo từ lệnh courses.pop()
# print(courses)

# #câu lệnh đảo ngược danh sách
# courses=['a','b','c' ]
# courses.reverse()
# print(courses)#đưa ra giá trị danh sách đảo ngược từ cuối lên đầu xếp lần lượt

# #đưa các giá trị về lần lượt theo số thứ tụ hay theo bảng chữ cái
# courses=['a','b','c' ]
# num=['1','3','2']

# num.sort()
# courses.sort()
# print(courses)
# print(num)

# #dưa ra các giá trị theo thứ tự giảm dần

# courses=['a','b','c' ]
# num=['1','3','2']

# num.sort(reverse=True)
# courses.sort(reverse=True) #True là giảm dần còn False là tăng dần
# print(courses)
# print(num)

# #có thể tìm các giá min hoặc max bằng cách hoặc tính tổng
# print(min(num))
# print(max(num))
# #print(sum(num))

# #có thể tìm chỉ số của giá trị trong danh sách  bằng cách
# course=['a','b','c' ]
# print(course.index('b'))  #giá trị đưa ra 1

# #nếu muốn kiểm tra trong danh sách có chưa giá trị đó không ta có thể sử dụng
# courses=['a','b','c' ]
# print('a' in course) #giá trị đưa ra sẽ là True nếu có hoặc False nếu không


# courses=['a','b','c' ]
# for item in course:
#     print(item) #giá trị đưa ra sẽ giá trị không theo danh sách bỏi câu lệnh in đưa ra các giá trị theo từng dòng

# #ta có thể liệt kê từng chỉ mục như sau
# courses=['a','b','c' ]
# for item in enumerate(course):
#     print(item) #giá trị đưa ra sẽ theo từng hàng và có từng chỉ mục từ con số 0

# #khi không muốn bắt đầu bằng số không ta sử dụng như sau
# courses=['a','b','c' ]
# for item in enumerate(course, start=1):
#     print(item) #giá trị đưa ra sẽ chỉ mục từ 1

# #nối các mục trong danh sách bằng cách
# courses=['a','b','c' ]
# course_str=', '.join(courses) #và có thể thay đổi cấc điểm nối
# print(course_str)

# #hoặc có thể đưa chuỗi về dạng danh sách bằng cách
# courses=['a','b','c' ]
# course_str=', '.join(courses)
# new_list=course_str.split(', ') #lệnh này giúp xóa bỏ các điểm nối và đưa chuỗi thành danh sách
# print(course_str)
# print(new_list)

# #kiểm tra giống và khác nhau không thực hiện cho danh sách ngoặc [] mà chỉ áp dụng {}

# courses_1 = {'a','b','c'}
# courses_2 = {'a','b','e'}

# # Giao nhau (giống nhau)
# print(courses_1.intersection(courses_2))  # {'a', 'b'}

# # Khác nhau (có trong 1 mà không có trong 2)
# print(courses_1.difference(courses_2))    # {'c'}
# print(courses_2.difference(courses_1))    # {'e'}

# # Hợp lại (mỗi phần tử chỉ 1 lần)
# print(courses_1.union(courses_2))         # {'a','b','c','e'}

# #tạo danh sách rỗng
# my_list={}
# print(my_list)


# #từ điển và từ khóa
# student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']} #chuỗi , số nguyên, danh sách
# print(student) #từ điển
# print(student['name']) #name là từ khóa để truy cập và hiển thị trong từ điển

# #hoặc có thể sủ dụng tương tự bằng cách
# student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']} #chuỗi , số nguyên, danh sách

# print(student.get('name')) #nếu truy cập key ko tồn tại giá tri đưa ra None

# #hoặc có thể thay đổi giá trị đưa ra như sau
# student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']} #chuỗi , số nguyên, danh sách

# print(student.get('phone', 'Not Found'))

# #có thể thêm hoặc cập nhật và biến
# student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']} #chuỗi , số nguyên, danh sách
# student['phone']='123456' #thêm vào từ điển
# student['name']='minh ngoc' #sửa đổi trong từ điển
# print(student)

# #hoặc cập nhật bằng cách
# student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']}
# student.update({'phone':1234567, 'name':'minh ngoc'})
# print(student)

# #có thể xóa bằng cách
# student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']}
# del student['age']
# print(student)

# #có thể lấy giá trị xóa đi đó 
# student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']}
# age=student.pop('age') 
# print(student) #kết quả đưa ra đã mất age
# print(age)

# #số lượng key hay chiều dài
# student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']}
# print(len(student))

# #hiển thị all key và hiển thị giá trị
# student={'name':'nga', 'age':20, 'live':['hanoi', 'bacgiang']}
# print(student.keys())
# print(student.values())

# print(student.items()) #hiển thị các cặp khóa và cặp giá trị

# for key in student:
#     print(key) #cho ra các key
# for values in student.items():
#     print(values)  #cho ra các giá trị

# #câu lệnh nếu
# n=True
# if n:
#     print('nga') #giá trị True
# else:
#     print('nga')#giá trị đưa ra là rỗng

# #nếu 
# laguage='nga'
# if laguage==12:
#     print('True')
# else:
#     print('False')

# #thực thi cho đến khi đúng hoặc đến else

# # #sử dụng if and lệnh và
# n='nga'
# m=False
# l=True
# if n=='nga' and m: #do đi cũng m=False nến giá trị đưa ra cũng là sai
#     print('yep')
# else:
#     print('??')
# # if or lệnh hoặc
# n='nga'
# m=False
# l=True
# if n=='nga' or m: #chỉ cần 1 trong 2 đúng
#     print('yep')
# else:
#     print('??')

# #if not 
# m=True
# if not m:
#     print('yep') #nếu không đúng thì là sai còn nếu không sai thì đúng
# else:
#     print('no')

# #
# a=1
# b=1
# print(a==b)#giá trị đưa ra là True
# print(a is b) #a là b sai do id của 2 biến khác nhau chỉ có giá trị giống nhau
# print(id(a))
# print(id(b))


# #đánh giá True False
# #các tập hợp '', [], {}, () đưa ra giá trị False
# #các chuỗi, số hanh danh sách đều đưa giá trị True
# m=[]
# if m:
#     print('True')
# else:
#     print('False')

# #vòng lặp for lặp lại thông qua 1 giá trị nhất định hoặc cho đến khi điều kiện được đáp ứng

# nums=[1,2,3,4,5,]
# for num in nums:
#     print(num) #sẽ giúp liệt kê các giá trị trong danh sách 

# #kết hợp vòng lặp for và câu lệnh nếu if
# for num in nums:
#     if num==3:
#         print('found')
#         break # Thoát hẳn khỏi vòng lặp.
#     print(num) #khi for tìm đến giá trị 3 như yêu cầu thì câu lệnh sẽ được in ra "found"và kết thúc quá trình

# #hoặc vẫn có thể giúp câu lệnh for tiếp tực bằng cách
# for num in nums:
#     if num==3:
#         print('found')
#         continue #Bỏ qua phần còn lại của vòng lặp hiện tại và sang vòng lặp kế tiếp.
#     print(num) #lệnh for vẫn tiếp thưc hiện khi num đã tìm được giá trị mong muốn

# #thực hiện vòng lặp chèn 
# for num in nums:
#     for so in 'abc':
#         print(num, so)
#         #giá trị đưa ra là vòng lặp từ trong ra ngoài

# #vòng lặp in ra teheo phạm vị chủ định
# for n in range(10):
#     print(n) #giá trị đưa ra sẽ thực hiện từ 0 đến 9 không bao gồm 10

# for n in range(1,10):
#     print(n) #giá trị đưa ra từ 1 đến 9

# # #vòng lặp while vô thời hạn cho đến khi đáp ứng được diều kiện đưa ra

# x=0
# while x<10:
#     print(x)
#     x+=1 #vòng lặp thực hiện liên tục cho đến khi x = 10 thì giá trị không thoả mãn điều kiện đưa ra khi đó vòng lặp sẽ dừng lại

# while x < 10:
#     x+=1
#     print(x) #khi thực hiện lệnh này thì vòng lặp sẽ thực hiện vô thời định do không có bất  kì điều kiện nào chỉ định và giá trị in ra sẽ là 0 và lặp đi lặp lại
#     break
# #giá trị đưa ra là 1 
# while x < 10:
#     print(x) #khi thực hiện lệnh này thì vòng lặp sẽ thực hiện vô thời định do không có bất  kì điều kiện nào chỉ định và giá trị in ra sẽ là 0 và lặp đi lặp lại
#     x+=1
#     break
# #giá trị đưa ra là 0
# x=0
# while x<10:
#     if x==5:
#         print('found')
#         break
#     print(x)
#     x+=1


# x=0
# while True:
#     if x==5:
#         print('found')
#         break
#     print(x)
#     x+=1
# #khi thực hiện True thì chắc chắn phải cần lệnh break để đừng lại nếu không nó sẽ thực hiện vô hạn định

# #nếu bị mắc kẹt trong vòng lặp vô hạn nhấn Ctrl c để dừng



# #function các chức năng

# #def chỉ hàm 
# def a():
#     pass #lệnh bỏ qua như không làm gì mà nó không đưa ra lỗi
# print(a()) #giá trị đưa ra sẽ là None bởi ta chưa thực hiện gì trong câu lệnh

# #
# def a():
#    print('nga')
# a() #giá trị đưa ra là nga bởi a() là 1 biến của 1 hàm

# def a():
#    print('nga!')
# a()
# a()
# a()
# a()
# # như vậy sẽ in ra được 4 lần và muón đổi thì có thể thay đổi trực tiếp thông qua giá trị trong hàm

# def a():
#    return 'nga' #trả về giá trị cho nơi gọi hàm
# print(a()) #kết quả sẽ đưa ra là nga bởi kết quả đưa ra là gọi ham a()
# print(a().upper()) #tạo ký tự viết hoa


# def a(greet):
#    return '{}, ngà'.format('greet') #gán tham số greet và vị trí trống
# print(a('hello'))

# def a(greet, name):
#    return '{}, {} ngà'.format(greet, name)
# print(a('hello', 'dinh')) 


# def a(greet, name = 'nga'):
#    return '{}, {} ngà'.format(greet, name) #có thể thêm 2 hoặc nhiều tham số khác
# print(a('hello', name = 'dinh'))

# def student(*a,**b):
#    print(a) #chứa từ thường
#    print(b) #chứ keyword

# student('toan', 'anh', ten='nga', tuoi=20)


# def student(*a,**b):
#    print(a)
#    print(b)
# c=['dinh', 'nga'] #danh sách ngoặc vuông
# d = {'live':'bac giang', 'age':20} #tư điển ngoặc ngọn
# student(c, d)#nó sẽ đưa ra dưới dạng danh sách


# #hoặc có thể thay đổi các tham số trong quá trình và kết quả đưa ra từ các tham

# def student(*a,**b):
#    print(a)
#    print(b)
# c=['dinh', 'nga'] #danh sách ngoặc vuông
# d = {'live':'bac giang', 'age':20} #tư điển ngoặc ngọn
# student(*c, **d) #nó sẽ đưa ra dưới dạng mục




# #Nhập các modules
# import src.test as test 
# #lúc nay in ra giá trị đưa ra sẽ là giá trị của modul test

# a = ['b', 'c', 'd']

# index = test.find_index(a, 'c')
# print(index)

# #
# import src.test as nga #as như thay thế cho test tạo cấu trúc giúp câu có thể ngắn và dễ nhìn hơn
# index = nga.find_index(a, 'c')
# print(index)

# from src.test import find_index, test_1  #from tên module import tên hàm hoặc tên biến trong module

# a = ['b', 'c', 'd']

# index = find_index(a, 'c')
# print(index)
# print(test_1)

# #
# from src.test import find_index, test_1  

# a = ['b', 'c', 'd']

# index = find_index(a, 'c')
# print(index)
# print(test_1)

# #
# from src.test import find_index as fi, test_1  #find_index được thay thể bằng fi

# a = ['b', 'c', 'd']

# index = fi(a, 'c')
# print(index)
# print(test_1)

# from src.test import *  #thay thế cho tất cả các biến trong module có chút bất tiện do ko biết biến nào của module khác

# a = ['b', 'c', 'd']

# index = find_index(a, 'c')
# print(index)
# print(test_1)

# #
# from src.test import find_index, test_1  

# a = ['b', 'c', 'd']

# index = find_index(a, 'c')
# print(index)
# print(test_1)

# #appen dùng để thêm phần tử vào cuối danh sách

# #lẹnh random
# import random

# a = ['b', 'c', 'd']

# a_1=random.choice(a) #choice lệnh lựa chọn 

# print(a_1)

