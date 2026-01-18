# Toán tử walrus operator := là toán tử vừa gán vừa trả về giá trị trong một biểu thức.

# happy = True
# print(happy)

# print(happy := True)

# m = list()
# while a :=input('Nhap:') != '0':
#     m.append(a)


#Gán hàm cho biến
# def hello():
#     print('hello nga')

# hi = hello
# hello()
# hi()

# say = print
# say('hello nga')

#Hàm bậc cao là nhận hàm khác làm đối số
#            là hàm trả về 1 hàm khác 
# def loud(text):
#     return text.upper()
# def quiet(text):
#     return text.lower()
# def hello(func):
#     text = func('Hello')
#     print(text)
# hello(quiet)
# hello(loud)

# def di(x):
#     def div(y):
#         return y/x
#     return div  
# da = di(2)
# print(da(10))   #5.0

# print(di(2)(10))  #5.0

#Hàm lambda
# age_check = lambda x : 1 if x >=18 else 0
# print(age_check(19))

# sorted(key = , )
# map(key = , )
# filter(key = , )

# # recude
# import functools
# a = ['a', 'b', 'c','d']
# m = functools.reduce(lambda x,y: x+y, a)  # như gán x y vào a b sau đo cộng lại thành ab tiếp sau là x y với ab c thành abc cho đến khi chỉ còn 1 giá trị gán thì dừng
# print(m)  #abcd

# a = [5,4,3,2,1]
# m = functools.reduce(lambda x,y: x*y, a) 
# print(m)



# list comprehension 

#[biểu_thức for phần_tử in iterable if điều_kiện]
#[giá_trị_if_true if điều_kiện else giá_trị_if_false for x in iterable]

# a = [i*i for i in range(1,11)]
# print(a)
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [i if i >= 5 else 'fail' for i in a]
# print(b)



# dictionary comprehension

#{key: value for (key,item) in dic.items()} 
#{key: value for (key,item) in dic.items() if điều_kiện}
#{key: (if/else) for (key,item) in dic.items()}
#{key: function(value) for (key,item) in dic.items()}


#zip(*iterables):   tổng hợp từ 2 hoặc nhiều danh sách lại với nhau theo vị trí
n = [1,2,3,4]
m = ['a','b','c','d']
# use = list(zip(m,n))
# print(use)        #[('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# for i in use:
#     print(i)

# uses = dict(zip(m,n))
# print(uses)         #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for key,value in uses.items():
#     print(key + str(value))



# if __name__ == "__main__"    #kiểm tra file được chạy trực tiếp hay được improt khác vào
# và chỉ chạy khi ở file đó sang 1 file khác sẽ ko thực thi lệnh trong if __name__ == "__main__"

# if __name__ == "__main__":
#     pass

# print(__name__)



import time

# print(time.ctime(0))  #in ra kỷ nguyên
# print(time.ctime(10000)) 

# print(time.time())   # in ra số giây hiện tại đã hình thành máy tính

a = time.localtime()
print(a)
# format thời gian theo ý muốn
b = time.strftime('%B %d %Y %H:%S', a)
print(b)

#thời  gian đặt
time_str = (2026, 1, 14 , 13, 00, 0, 0, 0, 0)  #(year, month, day, hour, min, sec, wday, yday, isdst)
print(time.asctime(time_str))


# Cú pháp chuẩn hóa ngày 
# def chuan_hoa(self):
#     d, m, y = self.ngay.split('/')
#     self.ngay = f"{d.zfill(2)}/{m.zfill(2)}/{y}"   #zfill(2) chuẩn hóa ngày 2 là độ dài chuẩn hóa
