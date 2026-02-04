import pandas as pd

'''
chuỗi là gì
Một Pandas Series giống như một cột trong một bảng.
Nó là một mảng một chiều chứa dữ liệu thuộc bất kỳ kiểu nào.

'''

#Tạo một Pandas Series đơn giản từ một danh sách:
# a = [1, 'a', 2]
# myvar = pd.Series(a)
# print(myvar)
            # 0    1
            # 1    a
            # 2    2
            # dtype: object   #khi không có cùng kiểu dự liệu đầu vào thì dtype sẽ bằng object

'''
NHÃN
Nếu không có chỉ định nào khác, các giá trị sẽ được đánh số thứ tự. Giá trị đầu tiên có chỉ số 0, giá trị thứ hai có chỉ số 1, v.v.
Nhãn này có thể được sử dụng để truy cập một giá trị cụ thể.
'''
# print(myvar[1])   # trả về vị trí thứ 2 của Series 



a = [1, 2, [3, 4]]
b = a.copy()
b[2][0] = 9
print(b)
print(a)


