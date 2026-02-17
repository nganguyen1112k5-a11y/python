import socket  # Thư viện socket

# Tạo TCP socket IPv4
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ server cần kết nối tới
server_address = ('localhost', 12345)

# connect() sẽ thực hiện TCP 3-way handshake
# Nó BLOCK cho đến khi kết nối hoàn tất
client_socket.connect(server_address)

try:
    while True:
        # Nhập dữ liệu từ bàn phím
        message = input("Nhập tin nhắn (exit để thoát): ")

        # Nếu nhập exit thì thoát chương trình
        if message == "exit":
            break

        # encode() chuyển string → bytes
        # Vì TCP chỉ gửi dữ liệu dạng bytes
        client_socket.sendall(message.encode())
    
        # Nhận dữ liệu phản hồi từ server
        # recv() BLOCK nếu chưa có dữ liệu trả về
        data = client_socket.recv(1024)

        # decode() chuyển bytes → string
        print("Client nhận lại:", data.decode())

finally:
    # Đóng socket khi kết thúc
    client_socket.close()
