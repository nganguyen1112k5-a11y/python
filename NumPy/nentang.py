'''
NUmpy là gì?
-Là 1 thư viện trong Python
-Được sử dụng để làm việc với mảng
-NumPy = Numerical Python (Python số học)
'''

'''
tạo mảng Numpy
- array (ndarray)  
🔹 Cấu trúc dữ liệu dùng để lưu trữ các giá trị số cùng kiểu dữ liệu,
🔹 được sắp xếp theo một hoặc nhiều chiều,
🔹 và cho phép tính toán nhanh trên toàn bộ dữ liệu , thống kê min max, chọn lọc boolean
- Tạo thành mảng lươc bỏ dấu phẩy (ma trận có thể công, trừ nhân các ma trận)
'''
'''
-array nhanh hơn list vì nó lưu dữ liệu liên tục trong bộ nhớ và dùng code C tối ưu + vectorization, còn list là tập hợp các con trỏ Python.
'''

import numpy as np

# # 1 chiều
# a = [1,2,3,4,5]
# b = np.array(a)
# print(b)                    # [1 2 3 4 5]
# print(type(b))              #<class 'numpy.ndarray'>


# # 2 chiều
# c = np.array([[1, 2],
#               [3, 4]])
# print(c)

# print(c.ndim)               #kiểm tra số chiều của mảng

# tạo mảng tử tuple
# m = (1,2,3,4,5)
# print(np.array(m))     #[1 2 3 4 5]

# # tính toán nhanh
# print(b**2)                 #[ 1  4  9 16 25]

'''
nguyên tắc ưu tiên kiểu dữ liệu 
bool → int → float → complex → string → object
'''

# a = [2, 'a']
# b = np.array(a)
# print(b)         #['2' 'a']



# ép kiểu thủ công theo chỉ định
# '   dtype=...   '
# arr = np.array([1, 2, 3.9], dtype=int)
# # print(arr)                          # ưu tiên đưa về dạng int

# arc = arr.astype(bool)              #ép kiểu
# print(arc)



#chỉ mục của mảng

# a = [1,2,3,4,5]
# print(np.array(a)[0:3])

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr[0,1])  #[cột , hàng]
#                 #khối cột hàng

# # chuyển đổi 

# print(np.shape(arr))    #trả về số chiểu mảng (2,5)  2 chiều trong đó có 2 mảng và mỗi mảng có 5 phần tử
# print(arr.reshape(10))   #chuyển đối mảng 1 chiều thành 1 chiều có 10 phần tử
# print(arr.reshape(5,2))  #chuyển đổi mảng thành 2 chiều có 5 mảng và mỗi mảng 2 phần tử
# #phép -1 trong reshape giúp ta tự tính kích thước chiều cho mk miễn là tổng phần tử trước sau bằng nhau
# print(arr.reshape(2,-1))

#  copy : dữ liệu ở mảng mới không bị thay đổi khi thay đổi ở mảng gốc
#  view : dữ liệu ở mảng mới sẽ bị thay đổi theo nếu thay đổi ở mảng gốc và ngược lại


#vòng lặp có thể sử dụng thông qua for nhưng sẽ phải lặp lại nhiều lần for nếu có nhiều chiều hay mảng

# thay đó sd nditer()   sẽ im ra trực tiếp ko cần sd nhiều vòng lặp

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#   print(x,end= ' ')    #1 2 3 4 5 6 7 8 

#trích xuất id hay lặp liệt kê
# for idx,x in np.ndenumerate(arr):
#   print(idx,x)
    #(0, 0, 0) 1
    #(0, 0, 1) 2
    #(0, 1, 0) 3  ....


#nối mảng concatenate()
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2)) 
# print(arr)

# arr1 = np.array([[1, 2, 10], [3,13, 4]])
# arr2 = np.array([[5, 6, 11], [7,12, 8]])
# arr = np.concatenate((arr1, arr2), axis=0)    # 0 nối theo hàng (dọc) số cột phải bằng nhau
# print(arr)                                    # 1 nối theo cột (ngang) số hàng phải bằng nhau
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)  


#tách mảng array_split()
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)
# print(newarr)       #[array([1, 2]), array([3, 4]), array([5]), array([6])]
#để chia thành các mảng
# for i in range(newarr.__len__()):
#     print(newarr[i],end= ' ')           #[1 2] [3 4] [5] [6] 




# Tìm kiếm chỉ mục theo giá trị   where()
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)                   #(array([3, 5, 6]),)

'''
np.searchsorted(a, x)
là hàm tìm vị trí (chỉ mục) mà phần tử x nên được chèn vào mảng a đã được sắp xếp tăng dần,
sao cho thứ tự sắp xếp của mảng vẫn được giữ nguyên.
'''
# arr = np.array([8, 5, 10, 9,7])
# x = np.searchsorted(arr, 7)
# print(x)                    #2 chỉ mục sau khi sắp xếp giả định

# arr = np.array([1, 3, 5, 7])
# x = np.searchsorted(arr, [2, 4, 6])
# print(x)                # [1 2 3]


#sắp xếp mảng vẫn giữa nguyên np.sort()   nhưng chỉ sắp xếp trong mảng ko thể sắp xếp các mảng khác nhau



#Lọc mảng

# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)       #[41 43]


arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)   #[False False  True  True]
print(newarr)       #[43 44]
















