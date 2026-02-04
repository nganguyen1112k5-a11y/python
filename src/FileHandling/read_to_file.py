'''
Đọc file
'''

#1. đọc file cơ bản

'''
Phương thức:- read()       đọc toàn bộ
           :- readline()   đọc từng dòng
           :- readlines()  đọc toàn bộ và trả về danh sách các dòng
'''
# - strip() : loại bỏ các khoảng trắng

'''
Làm việc với file binary
'''

#Đọc file 
# with ('image.jpg', 'rb') as file:  #'rb' là chề độ đọc binary
#     data = file.read()
#     print(len(data))


#Ghi và đọc số nguyên
# number = 42
# with open('number.bin','wb') as file:
#     file.write(number.to_bytes(4,'big'))    #4 là byte chuyển về big là endianness thứ tự byte quan trọng nhất đứng trước
#               #chuyển từ số nguyên sang byte để viết vào file
# with open('number.bin', 'rb') as file:
#     data = file.read()
#     ab = int.from_bytes(data,'big')   #chuyển ngược lại để in ra và đọc được    
#     print(ab)

'''
4. Làm việc với file lớn
với file lớn, việc đọc toàn bộ file vào bộ nhớ khong phải là cách tốt nhất. Thay vào đó nên đọc từng phần
'''

'''
5. Phân tích file CSV là dạng bảng
'''

import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    
'''
Lưu ý:
- File CSV phải đúng định dạng , mỗi dòng phải có só cột bằng nhau
'''



