# Số ngẫu nhiên và ngoại lệ

#số ngẫu nhiêu

# import random

# x = random.randint(1,6) # số ngãu nhiên từ 1 ->6
# y = random.random()     # số ngẫu nhiên từ 0->1
# my_list  = [1,2,3]
# z = random.choice(my_list) #lựa chọn ngẫu nhiên trong my_list

# a = [1,2,3,4]
# random.shuffle(a) #sắp xếp ngẫu nhiêu và thay đổi biến cũ ko tạo ra biến mới

# print(x)
# print(y)
# print(z)
# print(a)

# ngoại lệ
try:
    b,c = map(int,input().split())
    a = b/c
except ZeroDivisionError as e:   #lỗi chia 0
    print(e)
except ValueError as e:   #lỗi giá trị đầu vào
    print(e)
except Exception as e:   #lỗi cơ bản khác
    print(e)  
else:
    print(a)
finally:
    print('luôn được thực thi ở cuối dù lỗi hay không')


