#Nhập các modules
import src.test as test 
#lúc nay in ra giá trị đưa ra sẽ là giá trị của modul test

a = ['b', 'c', 'd']

index = test.find_index(a, 'c')
print(index)

#
import src.test as nga #as như thay thế cho test tạo cấu trúc giúp câu có thể ngắn và dễ nhìn hơn
index = nga.find_index(a, 'c')
print(index)

from src.test import find_index, test_1  #from tên module import tên hàm hoặc tên biến trong module

a = ['b', 'c', 'd']

index = find_index(a, 'c')
print(index)
print(test_1)

#
from src.test import find_index, test_1  

a = ['b', 'c', 'd']

index = find_index(a, 'c')
print(index)
print(test_1)

#
from src.test import find_index as fi, test_1  #find_index được thay thể bằng fi

a = ['b', 'c', 'd']

index = fi(a, 'c')
print(index)
print(test_1)

from src.test import *  #thay thế cho tất cả các biến trong module có chút bất tiện do ko biết biến nào của module khác

a = ['b', 'c', 'd']

index = find_index(a, 'c')
print(index)
print(test_1)

#
from src.test import find_index, test_1  

a = ['b', 'c', 'd']

index = find_index(a, 'c')
print(index)
print(test_1)

#appen dùng để thêm phần tử vào cuối danh sách

#lẹnh random
import random

a = ['b', 'c', 'd']

a_1=random.choice(a) #choice lệnh lựa chọn 

print(a_1)

