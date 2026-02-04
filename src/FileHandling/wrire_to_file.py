'''
1. Cách mở file viết
-các chế độ trong file
▸ 'w' : Mở file để viết (ghi đè nếu file đã tồn tại)
▸ 'a' : Mở file để append (thêm vào cuối file)
▸ 'x' : Tạo file mới, nếu file đã tồn tại sẽ lỗi
▸ 'b' : Chế độ binary (dùng với các chế độ khác như 'wb','ab')
'''
#mở file để viết
# file = open("data.txt","w")     
#mở file để append
# file = open("data.txt","a")
#tạo file mới nếu file đã tồn lại sẽ lỗi
# file = open("new_file.txt","x")
# chế độ binary
# file = open("image.jpg","wb")

'''
2. Ghi chuỗi vào file
'''
#Chuỗi đơn giản write()
# with open('data1.txt', 'w') as file:
#     file.write('hello\n')   #\n để xuống dòng
#     file.write('nga\n')
# ghi nhiều dòng từ 1 list
# a = ['a', 'b']
# with open('data2.txt', 'w') as file:
#     file.writelines(a)

'''
3.Ghi dữ liệu nhị phân 
Khi làm việc với filr=e hình ảnh hay âm thanh, video cần ghi dữ liệu nhị phân
'''

#Ghi dự liệu nhị phân trực tiếp
# binary_data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'

# with open("binary_file.bin","wb") as file:
#     file.write(binary_data)

#Chuyển đổi từ chuỗi sang nhị phân
# text ="Hello World"
# bin = text.encode('utf-8')
# print(bin)      #b'Hello World'
# with open("binary_file.bin","wb") as file:
#     file.write(bin)


#Thêm vào cuối file(append)
# with open('data.txt', 'a') as file:
#     file.write('\n4 que Bac Giang')

'''
5. Ghi và đọc cùng lúc(chế độ 'w+')
'''

with open("data1.txt","w+") as file:
    file.write("Hello, World!")
    file.seek(0)    #đưa con trỏ về đầu file
    content = file.read()
    print(content)

'''
Lưu ý: Sau khi ghi con trỏ sẽ ở cuối file, cần dùng seek(0) để đưa nó về đầu file hay chỉ số mong muốn trước khi đọc
'''

'''
6. Ghi dữ liệu phức tạp (JSON, CSV, ...)
'''
import json

data = {"name": "John Doe","age": 30,"city": "New York"}

with open("data.json","w") as file:
    json.dump(data, file, indent=4)

import csv

data = [["Name","Age","City"],["John", 30,"New York"],["Jane", 25,"London"]]

with open("data.csv","w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)