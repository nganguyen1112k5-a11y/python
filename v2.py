#Dữ liệu số nguyên và số thực

#số nguyên int
num=3
print(type(num)) #giá trị đưa ra sẽ là số nguyên int

#số thực float
num=3.14
print(type(num)) #giá trị đưa ra sẽ là sô thực float

#phép toán tử trong py

print(3+2)

print(3-2)

print(3*2)

print(3/2) 

print(3//2) #phép chia lấy phần nguyên không lấy giá trị sau dấu phẩy

print(3**2) #phép thực hiện lũy thừa vd là 3 mũ 2 

print(3%2) #phép thực hiện chia lấy phần dư vd là 3 chia 2 bằng 1 lấy phần dư là 1

#cũng có thể sử dụng dấu ngoặc đơn để thưc hiện thứ tự các phép tính giống ta thực hiện bình thường

#phép toán tử số học
num=1
num=num+1
print(num)

#hoặc có thể dùng như sau
num=1
num+=1
print(num) #giá trị cho ra vẫn là num +1

#hay cũng dùng tương tự với các phép toàn khác
num=1
num*=10
print(num) #giá trị cho ra là 10

#các phép giá trị biến đổi số

#abs hàm giá trị tuyệt đối
print(abs(-3)) 

#hàm round hàm thực hiện đưa giá trị về số nguyên gần nhất

print(round(1.85))#giá trị đưa ra là 2

#hoặc có thể làm tròn số đến giá trị bao nhiêu sau dấu thập phân

print(round(3.85,1)) #giá trị đưa ra là 3.8 tức làm tròn đến vị trí thứ nhất sau dấu thập phân

#phép so sánh và sẽ đưa ra giá trị yes hoặc no

num_1=3 # dáu = ở đây là phép gán\
num_2=2

print(num_1==num_2) #phép so sánh bằng

print(num_1!=num_2) #phép so sánh không bằng

print(num_1>num_2) 

print(num_1<num_2)

print(num_1>=num_2) 

print(num_1<=num_2)

#chuối số nguyên
num_1='100'
num_2='200'
print(num_1+num_2) #nó là nối các chuối

#để đổi thành dạng số nguyên ta có thể dùng
num_1='100'
num_2='200'
num_1=int(num_1)
num_2=int(num_2)
print(num_1+num_2) #giá trị đưa ra sẽ la 300 như mong muốn


