'''
Quản lý File và Directory
'''

import os 


'''
1. Lấy thông tin từ thư mực hiện tại
'''
#lấy đường dẫn của thư mục hiện tại
# current_dir = os.getcwd()
# print(current_dir)

#Lấy tên thư mục cha
# print(os.path.dirname(current_dir))

#Lấy tên của thư mục hiện tại
# print(os.path.basename(current_dir))

'''
1.2 Thay đổi thư mục làm việc
'''
 
# try:
#     os.chdir('c:/ABE/VSCODE/yt/src')
#     print('yep')
# except FileNotFoundError:
#     print('no')
# except:
#     print('no1')


'''
1.3 Tạo và xóa thư mục
'''

# new_dir = 'test1'
# try:
#     os.mkdir(new_dir)
#     print('1')
# except FileExistsError:
#     print('0')

#tạo thư mục nhiều cấp
# try:
#     os.makedirs('parent/child/grandchild')
#     print("Đã tạo thư mục cấp nhiều!")
# except FileExistsError:
#     print("Thư mục cấp nhiều đã tồn tại!")

#xóa thu mục rỗng
# try:
#     os.rmdir(new_dir)
#     print(f"Đã xóa thư mục {new_dir}!")
# except FileNotFoundError:
#     print(f"Thư mục {new_dir} không tồn tại!")


'''
Lưu ý : makedirs() sẽ tạo tất cá thư mục cha nếu nó không tồn tại, còn mkdir chỉ tạo thư mục
'''

'''
2. Quản lý tập tin
'''

#liệt kê tất cả tập tin và thư mục trong thư mục hiện tại
print(os.listdir())

# kiểm tra là tập tin os.path.isfile()


# Thôngtin về tệp tin
# file_path ='data.txt'
# if os.path.exists(file_path):
#     print(f"\nThông tin về {file_path}:")
#     print(f"Đường dẫn đầy đủ: {os.path.abspath(file_path)}")
#     print(f"Kích thước: {os.path.getsize(file_path)} bytes")
#     print(f"Thời gian sửa đổi cuối: {os.path.getmtime(file_path)}")
#     print(f"Thời gian sửa đổi cuối (định dạng):{os.path.getmtime(file_path)}")
# else:
#     print(f"Tệp tin {file_path} không tồn tại!")


#di chuyển hay thay đổi tên tệp tin
#đổi tên khi trong cùng thư mục di chuyển khi khác thư mục
# old_file = 'C:\ABE\VSCODE\yt\src\data.txt'
# new_file = 'C:\ABE\VSCODE\yt\src\FileHandling\data.txt'

# os.rename(old_file, new_file)
#copy tệp file1 sang file2
# import shutil
# shutil.copy(file1, file2)

'''
os.rename có thể dùng để di chuyển tệp tin giữa các thu mục nếu cung cấp đủ đường dẫn
'''

'''
4. Quản lý quyền truy cập và thuộc tính
'''

'''
4.1 Kiểm tra quyền truy cập
'''
file_path ='data.txt'
# Kiểm tra xem tệp tin có tồn tại không
if os.access(file_path, os.F_OK):
    print("Tệp tin tồn tại!")
# Kiểm tra quyền đọc
if os.access(file_path, os.R_OK):
    print("Có quyền đọc tệp tin!")
# Kiểm tra quyền ghi
if os.access(file_path, os.W_OK):
    print("Có quyền ghi tệp tin!")
# Kiểm tra quyền thực thi
if os.access(file_path, os.X_OK):
    print("Có quyền thực thi tệp tin!")



'''
-os.path.abspath() : chuyển đường đẫn tương đối thành tuyệt đối
-os.path.basename() và os.path.dirname() : lấy tên file và thư mục cha
-os.path.exists(), os.path.isfile(), os.path.isdir(): kiểm tra tồn tại và loại file
-os.path.getsize() và os.path.getmtime() : Lấy kích thước và thời gian sửa đổi.
-os.path.join() và os.path.split() : Gộp và phân tích đường dẫn.
-os.path.islink() và os.path.realpath() : Làm việc với liên kết tượng trưng.
'''