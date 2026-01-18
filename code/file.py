#kiểm tra tồn tại của đường dẫn tập tin

# import os

# path = 'C:\\ABE\\VSCODE\\yt\\code.py\\test.txt'

# if os.path.exists(path):   # kiểm tra file test.txt có tồn tại hay không
#     print('co ton tai')
#     if os.path.isfile(path):    
#         print('la file')
#     elif os.path.isdir(path):
#         print('la fodler')
# else:
#     print('ko ton tai')


# # Đọc tập tin
# try:
#     with open("C:\\ABE\\VSCODE\\yt\\code.py\\test.txt", encoding='utf-8') as file:       #nếu tập tin muốn sử dụng nằm ngoài folder đang code thì cần khai báo cả đường dẫn của tập tin nếu nằm trong cùng folder chỉ cần khai tên tập tin là được
#         print(file.read())
#         print(file.readlines())
#         print(file.readline())
#         print(file.read(10))        #tất cả sẽ thay đổi trực tiếp vào các tập trin nên khi in ra dòng đầu thì các in sau sẽ mất đi cái đã in
# except FileNotFoundError:
#     print('không được tìm thấy')

# # Viết tập tin
# text = 'xin chao \nchuc mot ngay tot lanh'
# with open("C:\\ABE\\VSCODE\\yt\\code.py\\test.txt",'w', encoding='utf-8') as file:
#     file.write(text)    # Nó sẽ thay đổi hoàn toàn tập tin thành text


# Sao chép tệp

# import shutil
# shutil.copyfile("C:\\ABE\\VSCODE\\yt\\code.py\\test.txt", 'copy.txt')
# shutil.copy("C:\\ABE\\VSCODE\\yt\\code.py\\test.txt", 'copy.txt')
# shutil.copy2("C:\\ABE\\VSCODE\\yt\\code.py\\test.txt", 'copy.txt')

# Di chuyển tập tin 

# import os
# a = 'C:\\ABE\\VSCODE\\yt\\code\\test.txt'
# b = 'C:\\ABE\\VSCODE\\yt\\src\\test.txt'
# try:
#     if os.path.exists(b):       #kiểm tra đường dẫn b đã tồn tại chưa
#         print('b da ton tai')
#     else:
#         os.replace(a,b)     #thay thế test.txt từ đường dẫn a sang đường dẫn b
#         print(a + ' da di chuyen')
# except FileNotFoundError:
#     print('a ko ton tai')

# Xóa tệp

# import os
# import shutil

# path = 'C:\\ABE\\VSCODE\\yt\\src\\test.txt'
# try:
#     os.remove(path)   # xóa tệp và thư mục nhưng không xóa được thu mục trống
#     os.rmdir(path)    #xóa thư mục trống
#     shutil.rmtree(path)  #có thể xóa các thư mục chứa các tập tin
# except FileNotFoundError:
#     print('ko tim thay')
# except PermissionError:
#     print('ko xoa thu muc trong')
# except OSError:
#     print('ko xoa thu muc co tap tin ben trong')




# Module

# import test1 as te     #cần có cùng đường dẫn hoặc chạy phải có cấp cao hơn
# te.hello()
# te.bye()

# from test1 import hello,bye   # có thể dùng * nhưng nên ko dùng 
# từ module test1.py lấy hello,bye để sử dụng
# hello()
# bye()

# help('modules')







