from numpy import random as rd
import numpy as np
import seaborn as sns

#LÀM VIỆC VỚI SỐ NGẪU NHIÊN randint(), rand()

# x = rd.randint(100)
# print(x)       # in ra số ngẫu nhiên từ 0-99

# x= rd.rand()
# print(x)            # in số ngẫu nhiên từ 0-1

# x = rd.randint(100,size=(5))   #in ra mảng chứa 5 số ngẫu nhiên
# y = rd.randint(100,size=(3,3))   #in ra mảng 2 chiều chứa 3 mảng mỗi mảng 3 giá trị ngẫu nhiên
# print(x,y)   

#LÀM VIỆC VỚI MẢNG GIÁ TRỊ CÓ SẴN

# a = [1,2,3,4,5,6,7]
# x = rd.choice(a)       #in ra giá trị bất kỳ trong a
# y = rd.choice(a,size = (2,2))     #in ra mảng 2 chiều chứa giá trị ngẫu nhiên trong a
# print(x,y)      




'''
-PHÂN PHỐI DỮ LIỆU NGẪU NHIÊN

-có thể tọa các giá trị ngẫu nhiên dựa trên xs đã định bằng cách sử dụng choice() 
- xác xuất biểu thị nằm giữa 0 và 1, và tổng tất cả các xác suất phải bằng 1
'''
# x = rd.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(2,2,3))
# print(x)       


'''
-HOÁN VỊ NGẪU NHIÊN
'''
# XÁO TRỘN MẢNG  shuffle() thay đổi cách sắp xếp các phần tử ngay trong mảng làm thay đối mảng gốc

# arr = np.array([1, 2, 3, 4, 5])
# a = rd.shuffle(arr)
# print(a)   #None
# print(arr)    #[2 1 4 3 5] xóa trộn sau mỗi lần in ra


# TẠO HOÁN VỊ CỦA MẢNG permutation() cũng làm xóa trộn nhưng nó sẽ trả về 1 mảng mới không làm thay đổi mảng gốc

# arr = np.array([1, 2, 3, 4, 5])
# a = rd.permutation(arr)
# print(a)   #[1 5 4 3 2] xáo trộn sau mỗi lần in ra
# print(arr)      #[1 2 3 4 5]


# MÔ-DUN SEABORN

import matplotlib.pyplot as plt
import seaborn as sns

#vẽ biểu đồ displot()

# sns.displot([0, 1, 2, 3, 4, 5,0, 1, 2, 3, 4, 5, 10, 20])
# plt.show()      #theo cột  cột x là các giá trị cột y là số lượng giá trị


# sns.displot([0, 1, 2, 3, 4, 5,0, 1, 2, 3, 4, 5, 10, 20], kind="kde",cut = 0)
# plt.show()      #theo đường biểu thị theo mật độ x các giá trị y mật độ xuất hiện của chính nó và cộng các số lần giá trị xuất hiện quanh nó

'''
cột dữ liệu thật
đường ước lượng
'''

# sns.displot([1,1,2,1,2])
# plt.show()  








'''
PHÂN PHỐI CHUẨN
Phân phối chuẩn là một trong những phân phối quan trọng nhất.
Nó phù hợp với phân bố xác suất của nhiều sự kiện, ví dụ như điểm IQ, nhịp tim, v.v.
Sử dụng random.normal()phương pháp này để có được phân phối dữ liệu chuẩn.

Nó có ba tham số:
    -loc- (Trung bình) vị trí đỉnh của hình chuông.
    -scale- (Độ lệch chuẩn) Độ phẳng của đồ thị phân bố.
    -size- Hình dạng của mảng trả về.
'''

#Tạo một phân phối chuẩn ngẫu nhiên có kích thước 2x3:
# x = rd.normal(size=(2, 3))
# print(x)
        # [[ 0.67331719 -0.41811772 -1.06110305]
        #  [ 1.1730669  -0.4207576   0.313793  ]]

#Tạo một phân phối chuẩn ngẫu nhiên có kích thước 2x3 với giá trị trung bình là 1 và độ lệch chuẩn là 2:
# x = rd.normal(loc=1, scale=2, size=(2, 3))
# print(x)


# Hình ảnh trực quan của phân phối chuẩn
# sns.displot(rd.normal(size=1000),kind = 'kda')
# plt.show()






'''
Phân phối nhị thức
Phân phối nhị thức là một phân phối rời rạc .
Nó mô tả kết quả của các tình huống nhị phân, ví dụ như tung đồng xu, kết quả sẽ là mặt ngửa hoặc mặt sấp.

Nó có ba tham số:
n- Số lần thử nghiệm.
p- Xác suất xảy ra của mỗi lần thử (ví dụ: tung đồng xu, xác suất là 0,5 mỗi lần).
size- Hình dạng của mảng trả về.
'''

# Với 10 lần thử tung đồng xu, ta thu được 10 điểm dữ liệu:
# x = rd.binomial(n=10, p=0.5, size=10)
# print(x)     #10 lần thử mỗi lần thử có n lần thành công

# Hình ảnh trực quan của phân phối nhị thức
# sns.displot(rd.binomial(n=10, p=0.5, size=1000))
# plt.show()



'''
Sự khác biệt giữa phân phối chuẩn và phân phối nhị thức
Sự khác biệt chính là phân phối chuẩn là liên tục trong khi phân phối nhị thức là rời rạc, 
nhưng nếu có đủ điểm dữ liệu thì nó sẽ khá giống với phân phối chuẩn với một số vị trí và quy mô nhất định.
'''
# data = {
#   "normal": rd.normal(loc=50, scale=5, size=1000),
#   "binomial": rd.binomial(n=100, p=0.5, size=1000)
# }
# sns.displot(data, kind="kde")
# plt.show()





'''
Phân phối Poisson
Phân phối Poisson là một phân phối rời rạc .
Nó ước tính số lần một sự kiện có thể xảy ra trong một khoảng thời gian xác định.
Ví dụ: Nếu một người ăn hai bữa một ngày, thì xác suất người đó ăn ba bữa là bao nhiêu?

Nó có hai tham số:
lam- Tỷ lệ hoặc số lần xuất hiện đã biết
size- Hình dạng của mảng trả về.
'''

# Tạo mảng 1×10, mỗi phần tử là số lần xảy ra của sự kiện với trung bình 2 lần 
# x = rd.poisson(lam=2, size=100)
# print(x)


# Hình ảnh trực quan về phân phối Poisson
# sns.displot(rd.poisson(lam=2, size=100))  
# plt.show()    


'''
Sự khác biệt giữa phân phối chuẩn và phân phối Poisson
Phân phối chuẩn là liên tục trong khi phân phối Poisson là rời rạc.
Nhưng ta có thể thấy rằng, tương tự như phân phối nhị thức, đối với phân phối Poisson đủ lớn, nó sẽ trở nên tương tự như phân phối chuẩn với độ lệch chuẩn và giá trị trung bình nhất định.
'''
# data = {
#   "normal": rd.normal(loc=50, scale=7, size=1000),
#   "poisson": rd.poisson(lam=50, size=1000)
# }
# sns.displot(data, kind="kde")
# plt.show()

'''
Sự khác biệt giữa phân phối nhị thức và phân phối Poisson
Phân phối nhị thức chỉ có hai kết quả có thể xảy ra, trong khi phân phối Poisson có thể có số lượng kết quả không giới hạn.
Nhưng đối với các giá trị rất lớn nvà gần bằng 0, pphân phối nhị thức gần như giống hệt với phân phối Poisson sao cho n * pgần bằng lam.
'''
# data = {
#   "binomial": rd.binomial(n=1000, p=0.01, size=1000),
#   "poisson": rd.poisson(lam=10, size=1000)
# }
# sns.displot(data, kind="kde")
# plt.show()