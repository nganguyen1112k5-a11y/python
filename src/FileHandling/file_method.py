import os
'''
1. Đóng mở file open() và close()
'''
'''
2. Đọc file
- read() : đọc nội dung toàn bộ file
- readline() : đọc từng dòng một
- readlines() : đọc toàn bộ bộ và trả về danh sách các dòng trong file

- Lưu ý: có thể chỉ định số byte muốn đọc bằng cách truyền tham số vào phương thức này
'''

'''
3. Ghi file 
- write(): ghi nội dung vào file
- writelines() : ghi danh sách vào các dòng file

- Lưu ý: khi mở ở chế độ 'w' ghi nội dung cũ sẽ bị xóa, Nếu muốn giữ lại sử dụng chế độ 'a'
'''

'''
4. Quản lý vị trí
'''
# tell() trả về vị trí hiện tại hoặc đưa con chuột đến vị trí muong muốn tell(x) trong file 
# file = open("data1.txt","r")
# current_position = file.tell()               # khi mới mở file chưa thực hiện gì con trỏ sẽ ở vị trí 0
# print(f"Current position: {current_position}")
# file.close()

# seek() di chuyển con trỏ đến vị trí mong muốn
# file = open('data.txt', 'r')
# file.seek(3)                    #di chuyển con trỏ đến vị trí 3
# content = file.read(10)         #đọc 10 ký tự từ vị trí 3
# print(content)
# file.close()

'''
Lưu ý: vị trí trong file bắt đầu từ 0
'''


'''
5. Các phương thức khác
'''

#flush() buộc hệ thống ghi bộ nhớ đệm ra file

# file = open("data1.txt","w")
# file.write("Some data")
# file.flush()            #Bắt buộc ghi ra file ngay lập tức còn write thi chưa chắc đã lưu vào nó sẽ có thể bị mất khi ngắt máy đột ngột
# file.close()


#fileno() trả về số định danh của file
# file = open('data.txt', 'r')
# print(file.fileno())
# file.close()


#isatty()  kiểm tra file được kết nối với thiết bị tty không

# file = open("data.txt","r")
# print(f"Is TTY: {file.isatty()}")   #thông thường sẽ False 
# file.close()




'''
6. Các phương thức năng cao
'''
# truncate() cất bớt nội dung file

# file = open("data1.txt","w+")
# file.write("This is a long text that we want to truncate")
# file.truncate(5)              #Cắt nội dung chỉ để lại 5 ký tự đầu , không truyền sẽ không cắt
#                               # cắt từ vị trí con trỏ đang chỉ đến hết có thể dùng với  tell(trỏ con chuột vị trí mong muốn)
# file.close()

# file = open("data1.txt","r")
# print(file.read())
# file.close()