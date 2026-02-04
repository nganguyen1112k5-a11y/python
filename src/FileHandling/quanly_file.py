'''
Quản lý thư mục
'''
import os
import shutil

'''
1. Kiểm tra sự tồn tại của thư mục os.path.exists()
'''
os.path.exists('my_file.txt')

#kiểm tra đường dẫn đó có phải thư mục không
os.path.isdir('my_file.txt')

'''
Lưu ý:
os.path.exists() trả về True cho cả tập tin và thư mục. 
Nếu chỉ muốn kiểm tra thư mục thì sử dụng os.path,isdir()
'''


'''
2. Tạo thư mục mới
-Có hai phương pháp để tạo thư mục chính:
+os.mkdir()     : tạo 1 thư mục đơn
+os.makedirs()  : tạo thư mục và các thư mục cha nếu chưa tồn tại
'''

# try:
#     os.mkdir("new_folder")
#     print("Thư mục đã được tạo thành công!")
# except FileExistsError:
#     print("Thư mục đã tồn tại!")

# try:
#     os.makedirs("projects/2023/06/01", exist_ok=True)     #exist_ok = True giúp tránh lỗi khi thư mục đã tồn tại
#     print("Thư mục và các thư mục cha đã được tạo!")
# except OSError as e:
#     print(f"Lỗi: {e}")


'''
3. Lấy thông tin thư mục hiện tại
'''
# Lấy đường dẫn thu mục làm việc hiện tại
# current_dir = os.getcwd()
# print(f"Thư mục hiện tại: {current_dir}")

#Lấy tên thư mục làm việc hiện tại
# current_dir_name = os.path.basename(current_dir)
# print(f"Tên thư mục hiện tại: {current_dir_name}")

#Lấy đường dẫn tuyệt đối của 1 thư mục
# absolute_path = os.path.abspath("data")
# print(f"Đường dẫn tuyệt đối của 'data': {absolute_path}")


'''
4. Duyệt qua nội dung của thư mục
- Để xem nội dung của thư mục, ta sủ dụng os.listdir() hoặc os.scandir()
'''

#os.listdir()
folder_path = "c:/ABE/VSCODE/yt/src/FileHandling"
try:
    context = os.listdir(folder_path)
    print(folder_path)
    for i in context:
        print(i)
except FileNotFoundError:
    print('None')

#os.scandir(): Có hiệu suất tốt hơn với các thư mục lớn

with os.scandir("c:/ABE/VSCODE/yt/src") as entries:
    for entry in entries:
        print(f"Tên: {entry.name}, Loại: {'Thư mục' if entry.is_dir() else'Tập tin'}, Kích thước: {entry.stat().st_size} bytes")


'''
6. Thay đổi thư mục làm việc
- Thay đổi thư mục làm việc bằng os.chdir()
'''
#os.chdir()
try:
    os.chdir("D:/Projects/MyProject")
    print(f"Đã chuyển đến thư mục: {os.getcwd()}")
except FileNotFoundError:
    print("Không tìm thấy thư mục!")


'''
7. Xóa thư mục
- sử dụng: + os.rmdir()- cho thư mục rỗng
         : + shutil.rmtree()- cho thư mục có nội dung
'''
try:
    os.rmdir("empty_folder")
    print("Thư mục đã được xóa thành công!")
except FileNotFoundError:
    print("Không tìm thấy thư mục!")
except OSError:
    print("Thư mục không rỗng hoặc không thể xóa!")


try:
    shutil.rmtree("non_empty_folder")
    print("Thư mục và tất cả nội dung đã được xóa!")
except FileNotFoundError:
    print("Không tìm thấy thư mục!")
except OSError as e:
    print(f"Lỗi khi xóa thư mục: {e}")