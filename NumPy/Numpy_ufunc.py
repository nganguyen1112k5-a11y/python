import numpy as np
from math import log

'''
Numpy ufunc là hàm phổ quát là các hàm Numpy hoạt động trên ndarray đối tượng
-ufuncs được sử dụng để triển khai vector hóa trong NumPy

Việc chuyển đổi các câu lệnh lặp thành các phép toán dựa trên vectơ được gọi là vectơ hóa

ufuncs cũng nhận thêm các đối số khác, ví dụ như:
    whereMảng boolean hoặc điều kiện xác định nơi các thao tác nên được thực hiện.
    dtypeXác định kiểu trả về của các phần tử.
    outMảng đầu ra nơi giá trị trả về sẽ được sao chép vào.
'''

# x = [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# z = np.add(x, y)
# print(z)                  #[ 5  7  9 11]
#nó tương tự với việc sd for chạy qua từng phần tử rồi cộng lại và thêm và 1 list mới



# x = [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# z = []
# for i, j in zip(x, y):
#   z.append(i + j)
# print(z)                #[5, 7, 9, 11]



#out là tham số dùng để chỉ định nơi lưu kết quả, thay vì NumPy tạo mảng mới.
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = np.empty(3)

# np.add(a, b, out=c)
# print(c)

#tham số where= trong ufunc → chỉ tính ở vị trí thỏa điều kiện
# a = np.array([1, 2, 3, 4, 5])
# b = np.where(a > 3, a,None)       # a > 3 , đủ dk in ra a , ko đủ dk in ra None 
# print(b)                        #[None None None 4 5]

# b = np.where(a > 3)     #Tìm vị trí chỉ mục đủ điều kiện
# print(b)                          #(array([3, 4]),)



'''
UFUNC TẠO HÀM
Để tạo ufunc của riêng bạn, bạn phải định nghĩa một hàm, giống như cách bạn làm với các hàm thông thường trong Python,
sau đó thêm nó vào thư viện ufunc của NumPy bằng frompyfunc()phương thức tương ứng.

Phương thức này frompyfunc()nhận các đối số sau:
    function- Tên của hàm.
    inputs- Số lượng đối số đầu vào (mảng).
    outputs- Số lượng mảng đầu ra.
'''

# def myadd(x,y):
#     return x + y

# myadd_new = np.frompyfunc(myadd,2,1)
# print(myadd_new([1, 2, 3, 4], [5, 6, 7, 8]))




'''
HÀM SỐ HỌC ĐƠN GIẢN
'''
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# arr1 = np.array(a)
# arr2 = np.array(b)
# print(np.add(arr1,arr2))            #phép cộng

# print(np.subtract(arr1,arr2))       #phép trừ

# print(np.multiply(arr1,arr2))       #phép nhân

# print(np.divide(arr1,arr2))         #phép chia

# print(np.mod(arr1,arr2))            #lấy phần dư

# print(np.remainder(arr1,arr2))      #lấy phần dư

# print(np.divmod(arr2,arr1)[1])         #phép chia và lấy dư

# print(np.absolute(arr1,arr2))       #trị tuyệt đối

# print(np.abs(arr1,arr2))            ##trị tuyệt đối


'''
LÀM TRÒN SỐ THẬP PHÂN
'''

#lược bỏ phần thạp phân
# arr = np.array([-3.1666, 3.6667])
# print(np.trunc(arr))

# print(np.fix(arr))

# arr = np.around(3.1666, 1)      #làm tròn lên nếu >=5 còn lại xuống, làm tròn 1 chữ số sau dấu phẩy
# print(arr)

# arr = np.floor([-3.1666, 3.6667])      #làm tròn xuống
# print(arr)

# arr = np.ceil([-3.1666, 3.6667])     #làm tròn lên
# print(arr)



'''
LOGARIT
'''

arr = np.arange(1, 10)

# print(np.log2(arr))         #log cơ số 2

# print(np.log10(arr))        #log cơ số 10

# print(np.log(arr))          #log cơ số e

'''
có thể sử dụng frompyfunc() hàm kết hợp 
với hàm có sẵn math.log()với hai tham số đầu vào và một tham số đầu ra:
'''
# nplog = np.frompyfunc(log, 2, 1)
# print(nplog(100, 15))   #cơ số 15 của 100


'''
TỔNG NUMPY
'''

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])

# print( np.add(arr1, arr2))  #phép cộng giữa hai đối số

# newarr = np.sum([arr1, arr2])   #cộng tất cả các giá trị
# print(newarr)


# arr = np.array([1, 2, 3])
# newarr = np.cumsum(arr)    #ổng tích lũy [1, 1+2, 1+2+3]
# print(newarr)


'''
TÍCH NUMPY
'''


# arr = np.array([1, 2, 3, 4])
# print(np.prod(arr))           #nhân tất cả các giá trị

# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([5, 6, 7, 8])
# x = np.prod([arr1, arr2])
# print(x)   #nhân all
# print(np.cumprod([arr1,arr2])) #nhân tích lũy
