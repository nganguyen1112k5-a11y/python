import socket  # Thư viện lập trình mạng trong Python

# Tạo một TCP socket sử dụng IPv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Định nghĩa địa chỉ IP và Port mà server sẽ lắng nghe
# 'localhost' = 127.0.0.1 (chỉ cho kết nối trong máy)
# 12345 là số port
server_address = ('localhost', 12345)

print(f'Starting up on {server_address}')

# Gắn socket vào IP và Port
# Sau lệnh này, hệ điều hành biết server đang dùng port 12345
server_socket.bind(server_address)

# Chuyển socket sang chế độ lắng nghe (passive mode)
# Tham số 1 là số lượng client tối đa có thể chờ trong hàng đợi
server_socket.listen(1)

# Server chạy vô hạn để luôn sẵn sàng nhận client mới
while True:
    print('Waiting for a connection')

    # accept() sẽ BLOCK chương trình
    # Nó chờ cho đến khi có client kết nối
    connection, client_address = server_socket.accept()

    try:
        print(f'Connection from {client_address}')

        # Vòng lặp nhận dữ liệu từ client
        while True:
            # recv(16) đọc tối đa 16 bytes từ TCP receive buffer
            # Nếu chưa có dữ liệu, nó sẽ BLOCK
            data = connection.recv(16)  

            # Nếu có dữ liệu (khác rỗng)
            if data:
                # decode() chuyển bytes → string
                print(f'received {data.decode()}')

                # sendall() gửi lại toàn bộ dữ liệu cho client
                # Đây là echo server (gửi lại đúng dữ liệu nhận được)
                connection.sendall(data)

            else:
                # Nếu recv() trả về b'' nghĩa là client đã đóng kết nối
                print('no more data from', client_address)
                break

    finally:
        # Luôn đóng connection khi xong (giải phóng tài nguyên)
        connection.close()
