'''
Python Network Programming
-Giao tiếp mạng
'''

'''
1. giới thiệu về Networking Progamming
-Networking Programming là quá trình viết mã để các máy tính có thể giao tiếp với nhau qua mạng. 
Python cung cấp nhiều cách để là việc này, từ các module cơ bản cho đến thư cao cấp

-Networking Programming thường chia làm 2 loại chính:
+low-level: sử dụng socket API để kiểm soát tối đa
+high-level: sử dụng thư viện có sẵn cho các giao thức cụ thể (HTTP, FTP,..)

-VÍ DỤ:
+một ứng dụng server
+một client gửi yêu cầu HTTP
+một chương trình chat đơn giản
'''

'''
2. Sockets - Cổng giao tiếp cơ bản
- Socket là một điểm kết nối giữa hau ứng dụng qua mạng. 
Python cung cấp module soclet để là việc với sockets

-Cách hoạt động
1-Tạo Socket
2-kết nối(Hoặc lắng nghe)
3-gửi/nhận dữ liệu
4-đóng kết nối
'''

#ví dụ cơ bản

#Sever
# import socket

# #Tạo socket TCP/IP
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# #liên kết với địa chỉ và port
# server_address = ('localhost', 12345)
# print(f'Starting up on {server_address}')
# server_socket.bind(server_address)

# #lắng nghe kết nối
# server_socket.listen(1)

# while True:
#     #chờ kết nối
#     print('Waiting for a connection')
#     connection, client_address = server_socket.accept()

#     try:
#         print(f'Connection from {client_address}')
#         #Nhận dữ liệu
#         while True:
#             data = connection.recv(16)
#             if data:
#                 print(f'received {data.decode()}')
#                 #gửi dữ liệu
#                 connection.sendall(data)
#             else:
#                 print('no more data from', client_address)
#                 break
#     finally:
#         #đóng kết thúc
#         connection.close()


'''
-socket.AF_INET: Dùng cho IPv4
-socket.SOCK_STREAM: dùng cho TCp(giao thức có kết nối)
-bind(): liên kết socket với địa chỉ mà port
-listen(): chờ kết nối
accept(): chấp nhận kết nối mới
'''



'''
3.Threading với Networking Programming
khi làm việc với mạng chúng ta thường xử lý nhiều kết nối đồng thời.
Python cung cấp module threading để giúp chúng ta làm điều đó
'''
#Ví dụ:
# import socket
# import threading

# def hanle_client(connection, address):
#     print(f'Connected by {address}')
#     try:
#         while True:
#             data = connection.recv(1024)  #nơi nhận dữ liệu
#             if not data:
#                 break
#             print(f'Receuved: {data.decode()}')
#             connection.sendall(data)
#     finally:
#         connection.close()

# def start_server():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind('localhost', 12345)
#     server_socket.listen(5)

#     print('server is listening...')

#     while True:
#         connection, address = server_socket.accept()

#         thread = threading.Thread(target = 'handle', args= (connection, address))

#         thread.start()

# start_server()



'''
4. Các giao thức mạng phổ biến
-Python cung cấp nhiều mmodelu cho giao thức mạng phổ biến:
'''

#HTTP (Hypertext TRansfer Protocol):
import http.client   # Import thư viện http.client để làm việc với HTTP

# Tạo một kết nối HTTP tới server www.example.com (mặc định port 80)
conn = http.client.HTTPConnection("www.example.com")

# Gửi một HTTP request với phương thức GET tới đường dẫn "/"
# "/" nghĩa là trang chính (root) của website
conn.request("GET", "/")    #GET là method lấy giữ liệu , / đường dẫn path

# Nhận phản hồi (response) từ server sau khi gửi request
response = conn.getresponse()

# In ra mã trạng thái HTTP (vd: 200) và thông điệp đi kèm (vd: OK)
print(response.status, response.reason)

# Đọc toàn bộ nội dung dữ liệu mà server gửi về (dạng bytes)
data = response.read()

# Chuyển dữ liệu từ bytes sang chuỗi (string) rồi in ra màn hình
print(data.decode())

# Đóng kết nối TCP tới server (giải phóng tài nguyên)
conn.close()




#FTP (File Transfer Protocol)
from ftplib import FTP      # Import thư viện FTP

ftp = FTP('ftp.example.com')   # Kết nối TCP đến FTP server (port 21)

ftp.login('user', 'password')  # Đăng nhập với username và password

ftp.cwd('/path/to/directory')  # Chuyển vào thư mục chỉ định trên server

files = ftp.nlst()             # Lấy danh sách file trong thư mục hiện tại

print(files)                   # In danh sách file ra màn hình

ftp.quit()                     # Gửi lệnh QUIT và đóng kết nối FTP





# SMTP (Simple Mail Transfer Protocol):
import smtplib   # Import thư viện dùng để gửi email qua giao thức SMTP

# Tạo kết nối TCP đến SMTP server qua port 587 (submission port)
server = smtplib.SMTP('smtp.example.com', 587)

# Nâng cấp kết nối thường lên TLS để mã hóa dữ liệu (STARTTLS)
server.starttls()

# Đăng nhập vào SMTP server bằng tài khoản email
server.login("user@example.com", "password")

# Gửi email:
# - Địa chỉ người gửi
# - Địa chỉ người nhận
# - Nội dung email (phải có header và body, cách nhau bởi \n\n)
server.sendmail(
    "from@example.com",
    "to@example.com",
    "Subject:Test\n\nHello!"
)

# Gửi lệnh QUIT và đóng kết nối TCP
server.quit()


'''
5. Các vấn đề thường gặp
'''
#1. Timeout

import socket
socket.setdefaulttimeout(10) # thiết lập timeout mặc định


#2. Lỗi kết nối
try:
    connection = socket.create_connection(('example.com', 80))
except socket.error as e:
    print(f'Connection error: {e}')

#3. Lỗi xử lý dữ liệu lớn
def receive_large_data(connection):
    data = 'b'
    while True:
        chuck = connection.recv(4096)
        if not chuck:
            break
        data += chuck
    return data

'''
tóm tắt lại:
-socket là cơ sở cho tất cả giao tiếp mạng trong python
-Threading giúp xử lý nhiều kết nối đồng thời
-Python hỗ trợ nhiều giao thức mạng phổ biến thông qua các module riêng
-Tỉmout và xử lý lỗi rất quan trọng trong networking programming
-ví dụ thực tế là cách tốt nhất để học networking programming
'''
