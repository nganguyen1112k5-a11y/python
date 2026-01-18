

## TOÁN TỬ (MATH OPERATER )


# 1). Các phép toán 
# '+'
# '-'
# '*'
# '/'
# '%' chia lấy phần dư
# '//' chia lấy phần nguyên

a = 10
b = 2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a // b)



# TOÁN TỬ SO SÁNH (COMPARISION OPERATOR)

# '=='
# '>'
# '>='
# '<'
# '<='
# '!=' so sánh khác

# luôn đưa ra giá trị là kiểu dữ liệu bool : True, False

# print(a == b)
# print(a > b)
# print(a >= b)
# print(a < b)
# print(a <= b)
# print(a != b)


# #Tính chất mở rộng Truthy, Falsy

# -luôn đúng :
# + khác rỗng
# + có giá trị
# + mã cổ điển (0110100101011)

# -luôn sai : còn lại



# -TOÁN TỬ LOGIC ()


# and or
# print(a > b and a % b ==0) # True
# #lọc dự liệu 
# print(0 or '' or 1) # 1  
# print(0 or 2 or 1) # 2

# not (phép phủ định)
# -không đúng thì sai
# -không sai thì đúng

# print(not True)


#TOÁN TỬ THÀNH VIÊN (MEMBERSHIP OPERATER)

# in 
# - inerable ??

# print('a' in 'abc') #True
# print('a' not in 'abc')  #False


# -TOÁN TỬ NHẬN DIỆN
# print([] is []) #dưl liệu không nguyên thủy nên không cùng ô nhớ
# print(1 is 1) # dữ liệu nguyên thủy nên cùng ô nhớ

#kiểu nhận diện
# a = 1
# b = 2
# print('%i + %i = %i' %(a, b, a+b)) #1 + 2 = 3

#Format truyền vào trong{}

# print('{} {}' .format('nga','nguyen')) #nga nguyen
# print('{1} {0}' .format('nga','nguyen')) #nguyen nga

# a = 'ngà'
# print(a[0]) #n

#F-string chuyền trực tiếp
# a = 1
# b = 2
# print(f'{a} + {b} = {a + b}') #1 + 2 = 3

# name = "Ngà"
# age = 20
# print(f"Tôi tên là {name}, năm nay {age} tuổi.")
# #Tôi tên là Ngà, năm nay 20 tuổi.



# split() -> hàm chia cắt, cắt khoảng trắng
# '1 2 3'.split -> ['1' '2' '3']
# --> list[str]

# map (ánh xạ) thay cho cách ép từng phần tử 
# hay nói cách khác là gán giá trị cho tùng phần tử đầu ra ứng với các giá trị đầu vào


# sep='' khoảng cách giữa những phần tử mặc định là khoảng trắng
# end='' kết thúc câu, mặc định là xuống dòng

# kĩ thuật giải phóng tự do *
# a,*b,c = 1,2,3,4,5
# a = 1
# b = 2,3,4
# c = 5


# a,*b,c = map(int,input().split())
# print(a) #1
# print(*b)# 2 3 4
# print(c) #5


