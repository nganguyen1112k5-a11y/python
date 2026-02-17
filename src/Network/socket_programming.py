'''
Python Socket Programming
-Tổng quan
Socket Programming là 1 kỹ thuật giao tiếp giữa hai nút trong mạng trong đó
server lắng nghe yêuc cầu từ client. Python cung cấp module socket mạnh mẽ để thực hiện
giao tiếp mạng này
'''

'''
1. Khái niệm cơ bản về socket
-là một cổng giao tiếp giữa ay máy. Nó kết hợp IP address và port number để tạo thành
một điểm kết nối duy nhất
'''
# Tạo socket TCP/IP
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# AF_INET = IPv4,SOCK_STREAM = TCP
print("Socket đã được tạo:", sock)
# Kết quả: Socket đã được tạo:<socket.socket fd=3, family=AddressFamily.AF_INET,type=SocketKind.SOCK_STREAM, proto=0>

'''
Lý do socket quan trong:
-cho phép giao tiếp giữa các máy trong mạng
-dùng cho cả TCP(connection-orieted) và UDP(connectionless)
-cung cấp giao diện chuẩn cho các hệ điều hành khác nhau

Các loại socket phổ biến:   (AF_INET dùng để chỉ định loại địa chỉ IP mà socket sẽ sử dụng)
-AF_INET": IPv4(dung chung nhất)
-AF_INET6: IPv6
-AF_UNIX: giao tiếp dung trong máy(unix domain sockets)

SOCK_STREAM là một kiểu socket trong lập trình mạng dùng để tạo kết nối theo giao thức TCP.
'''



'''
2. Socket trên Server
-Quá trình hoạt động của server
+1. Tạo socket
+2. Bind đến IP và port      (📌 IP:Xác định máy nào  Port:Xác định chương trình nào trên máy đó)
+3. Lắng nghe kết nối
+4. Chấp nhận kết nối từ client
'''
