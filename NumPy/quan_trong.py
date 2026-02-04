
'''
                    NUMPY
'''


import numpy as np


'''
TẠO MẢNG
'''

# 1 chiều
# a = [1,2,3,4,5]
# b = np.array(a)
# print(b)                    # [1 2 3 4 5]

# tạo mảng tử tuple
# m = (1,2,3,4,5)
# print(np.array(m))     #[1 2 3 4 5]

'''
KIỂU DỮ LIỆU TRONG ARRAY
'''

'''
nguyên tắc ưu tiên kiểu dữ liệu 
bool → int → float → complex → string → object
'''

#array chỉ chữa 1 kiểu dữ liệu trong 1 mảng
# a = [2, 'a']
# b = np.array(a)
# print(b)         #['2' 'a']

# a = np.array([1, 2, 3])
# print(a.dtype)   # int32 hoặc int64

#ép kiểu thủ công
# arr = np.array([1, 2, 3.9], dtype=int)
# print(arr)                          # ưu tiên đưa về dạng int


'''
HÌNH DẠNG CỦA ARRAY
'''
#trả về hình dạnh của array
# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a.shape)   # (2, 3)  

#đổi hình dạng mảng  điều kiện tổng số phần tử phải giữa nguyên
# a = np.array([1, 2, 3, 4, 5, 6])
# b = a.reshape(2,3)
# c = a.reshape(2, -1)  # phép -1 trong reshape sẽ giúp tự tính kích thước còn lại cho
# print(b,c)


'''
TRUY CẬP PHẦN TỬ
'''
# a = [1,2,3,4,5]
# print(np.array(a)[0:3])

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr[0,1])  #[cột , hàng]
#                 #khối cột hàng

'''
Slicing - cắt array
'''
# a = np.array([1, 2, 3, 4, 5])
# print(a[1:4])   # [2 3 4]

# b = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print(b[:, 1])   # lấy cột 1 → [2 5]


'''
TOÁN TỬ VECTER HÓA
'''
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a + b)   # [5 7 9]
# print(a * 2)   # [2 4 6]


'''
LÀM PHẲNG ARRAY
'''
# a = np.array([[1, 2], [3, 4]])
# b = a.flatten()

# print(b)   # [1 2 3 4]


