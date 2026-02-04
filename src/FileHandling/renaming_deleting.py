'''
Quản lý file: renaming và deleting
'''
import os

'''
1 số hàm phổ biến
▸ os.listdir() - Danh sách file trong thư mục
▸ os.mkdir() - Tạo thư mục
▸ os.rmdir() - Xóa thư mục
▸ os.rename() - Đổi tên file
▸ os.remove() - Xóa file
'''

'''
2. Đổi tên file
'''
# os.rename(cerrent_name, new_name)

'''
Lưu ý:
-Nếu thư mục không tồn lại sẽ gặp lỗi
- Nếu tên mới đã tồn tại sẽ bị ghi đè lên
'''

#xử lý khi lỗi
try:
    os.rename("nonexistent.txt","new_name.txt")
except FileNotFoundError:
    print("Lỗi: File không tồn tại!")
except PermissionError:
    print("Lỗi: Không có quyền thay đổi file!")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")


'''
3. Xóa file
'''
# os.remove(file_name)

#xử lý lỗi khi xóa

try:
    os.remove("important_data.txt")
except FileNotFoundError:
    print("Lỗi: File không tồn tại!")
except PermissionError:
    print("Lỗi: Không có quyền xóa file!")
except IsADirectoryError:
    print("Lỗi: Đây là một thư mục, không phải file!")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")


'''
4. Các trường hợp khác
'''

#đối hoặc xóa file không tồn tại
file_name ="example.txt"
if os.path.exists(file_name):     #exists() kiểm tra file có tồn tại hay không
    os.rename(file_name,"new_example.txt")
    print("Đổi tên thành công!")
else:
    print("File không tồn tại!")

#Xóa nhiều file
#    xóa nhiều file trong 1 thư mục
directory ="temp_files"
files_to_delete = ["file1.txt","file2.txt","file3.txt"]

for file in files_to_delete:
    file_path = os.path.join(directory, file)   # join dùng để nối temp_files\file3.txt 
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Đã xóa: {file_path}")
    else:
        print(f"File không tồn tại: {file_path}")
print(file_path)


#Xóa file với mở rộng cụ thể

# Xóa tất cả file .tmp trong thư mục hiện tại
for file in os.listdir('.'):
    if file.endswith('.tmp'):    
        os.remove(file)
        print(f"Đã xóa: {file}")


'''
5. So sánh với các phương pháp khác
'''

#sử dụng  module shutil cung cấp hàm mạnh mẽ hơn cho việc quản lý file

import shutil

#di chuyển và đối tên
shutil.move('old_name.txt', 'new_name.txt')

#xóa file an toàn hơn
shutil.rmtree('directory_delete')  #Xóa thư mục


#Sử dụng pathlib 
from pathlib import Path

#Đổi tên file
file = Path('old_name.txt')
file.rename('new_name.txt')

#Xóa file
file.unlink()



'''
6. Best Practice
'''

#luôn kiểm tra file tồn tại trước khi thao tác
if os.path.exists(file_name):
    os.remove(file_name)

#xử lý lỗi 1 cách chuyên nghiệp
try:
    os.remove(file_name)
except Exception as e:
    print('loi',e)

#sử dụng đường dẫn tuyệt đối khi cần
file = os.path.abspath('my_file.txt')

