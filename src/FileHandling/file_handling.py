'''
1. Cách mở đóng file 
sử dụng open() để mở file hàm này trả về đối tượng file mà ta có thể thực hiện thao tác đọc và ghi
'''
#mở file trong chế độ đọc (mặc định)

# file = open('data.txt', 'r')   #'r' là chế độ đọc

'''
Lưu ý:
- nếu file không tồn tại và mở ở chế độ 'w' (ghi) py sữ tự động tạo file mới
- nếu file đã tồn tại và mở ở chế độ 'w' (ghi) nội dung trong file cũ cũng sẽ bị xóa đi
'''


#Các chế độ mở file phổ biến
'''
'r' Mở để đọc (mặc định)

'w' Mở để ghi, nếu file không tồn tại sẽ tạo mới

'a' Mở để ghi tiếp (append), con trỏ ở cuối file

'r+' Mở để đọc và ghi

'b' Mở dưới dạng binary (dùng kết hợp với các chế độ khác)
'''


#Dóng file  sử dụng close()

# file = open('data.txt', 'r')
#thực hiện thao tác với file
# file.close()  #đóng file sau khi sử dụng

'''
Lỗi thường gặp:
-Nếu không đóng file, hệ thống có thể không giải phóng tài nguyên, đặc biệt là khi làm việc với nhiều file lớn
'''


'''
2. Đọc dữ liệu từ file
'''

#Phương thức read() giúp đọc toàn bộ nội dung từ file và trả về dạng chuỗi
# file = open('data.txt', 'r')
# contenr = file.read()   #đọc toàn bộ nội dung trong file
# print(contenr)
# file.close()

'''
Lưu ý:
- Nếu file quá lớn đọc toàn bộ nội dung vào bộ nhớ có thể gây lỗi (MemoryError)
- Đối với file lớn nên đọc từng phần hay từng đoạn
'''

#Phương thức readline() đọc 1 dòng từ file
# file = open('data.txt', 'r')
# line = file.readline()
# while line:
#     print(line, end= '')
#     line = file.readline()
# file.close()

#Phương thức readlines() đọc toàn bộ file và trả về 1 danh sách
# file = open('data.txt', 'r')
# lines = file.readlines()
# print(lines)       # dạng danh sách
# for line in lines:
#     print(line, end= '')
# file.close()


'''
3. Ghi dữ liệu vào file
'''

#Phương thức write()
# file = open('data1.txt', 'w')
# file.write('Hello nga\n')
# file.close()

'''
Lưu ý:
- Nếu file đã tồn tại, nội dung cũ sẽ bị xóa đi
- Nếu file không tồn tại, Python sẽ tự tạo file mới
'''

#Phương thức witelines() ghi danh sách các chuỗi vào file
# lines = ["Dòng 1\n","Dòng 2\n","Dòng 3\n"]
# file = open('data1.txt', 'w')
# file.writelines(lines)
# file.close()

'''
Lưu ý:
- Mỗi phần tử trang danh sách phải là chuỗi
- Không tự động thêm kí tự xuống dòng, muốn xuống dòng sử dung ký tự '\n'
'''

'''
4. Xử lý file lớn hiệu quả
'''
#sử dụng vòng lặp for để đọc file lớn, và nên đọc từng dòng dể tiết kiệm bộ nhớ
with open('data.txt', 'r') as file:
    for line in file:
        print(line, end= '')
#sử dụng with để quản lý tài nguyên , with sẽ tự động đóng file khi hoàn thành, ngay cả khi có lỗi xảy ra
 '''
 Ưu điểm:
 - Không cần gọi đến close()
 - Dỏng bảo file đóng ngay khi có ngoại lệ
 '''

'''
5. Xử lý ngoại lệ khi làm việc với file
'''
# try expect
