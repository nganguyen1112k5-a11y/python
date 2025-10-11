#function các chức năng

#def chỉ hàm 
def a():
    pass #lệnh bỏ qua như không làm gì mà nó không đưa ra lỗi
print(a()) #giá trị đưa ra sẽ là None bởi ta chưa thực hiện gì trong câu lệnh

#
def a():
   print('nga')
a() #giá trị đưa ra là nga bởi a() là 1 biến của 1 hàm

def a():
   print('nga!')
a()
a()
a()
a()
# như vậy sẽ in ra được 4 lần và muón đổi thì có thể thay đổi trực tiếp thông qua giá trị trong hàm

def a():
   return 'nga' #trả về giá trị cho nơi gọi hàm
print(a()) #kết quả sẽ đưa ra là nga bởi kết quả đưa ra là gọi ham a()
print(a().upper()) #tạo ký tự viết hoa


def a(greet):
   return '{}, ngà'.format('greet') #gán tham số greet và vị trí trống
print(a('hello'))

def a(greet, name):
   return '{}, {} ngà'.format(greet, name)
print(a('hello', 'dinh')) 


def a(greet, name = 'nga'):
   return '{}, {} ngà'.format(greet, name) #có thể thêm 2 hoặc nhiều tham số khác
print(a('hello', name = 'dinh'))

def student(*a,**b):
   print(a) #chứa từ thường
   print(b) #chứ keyword

student('toan', 'anh', ten='nga', tuoi=20)


def student(*a,**b):
   print(a)
   print(b)
c=['dinh', 'nga'] #danh sách ngoặc vuông
d = {'live':'bac giang', 'age':20} #tư điển ngoặc ngọn
student(c, d)#nó sẽ đưa ra dưới dạng danh sách


#hoặc có thể thay đổi các tham số trong quá trình và kết quả đưa ra từ các tham

def student(*a,**b):
   print(a)
   print(b)
c=['dinh', 'nga'] #danh sách ngoặc vuông
d = {'live':'bac giang', 'age':20} #tư điển ngoặc ngọn
student(*c, **d) #nó sẽ đưa ra dưới dạng mục




