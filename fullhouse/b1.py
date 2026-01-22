
##DATA Type

# +chia làm 2 nhánh:

# -----primitive :nguyên thủy
# số nguyên int
# số thực float
# chuối kí tự int
# đúng sai bool
# chuỗi ký tự str
# 4 kiểu trên đều thuộc hướng đối tượng: 
# cùng 1 giá trị ->sẽ lưu cùng 1 ô nhớ(cùng id khi cùng 1 ô dữ liệu)


'''
cùng giá trị thì cùng ô nhớ
khác giá trị thì khác ô nhớ 
'''

# a = 1
# b = 1
# print(id(a))
# print(id(b))
## có cùng id <ô nhớ>

# n = input() #kết quả đưa ra là 1 chuổi ký tự
# print(type(n)) #str

# số phức complex
# chr
# ord

# (NLP natural...)

# -----non-primitive : không nguên thủy
# list
# set
# dict
# class
# function

'''
cùng giá trị có thể dùng ô nhớ trong trường hợp gán hoặc copy
khi 2 biến cùng ô nhớ từ viện copy hoặc gán thì thay đổi 1 biến, thì biến còn lại cũng bị thay đổi theo 
biến sau khi thay đổi và biến trước khi thay đổi vẫn có cùng id
'''



# ls liệt kê thư mục theo đường dẫn không có đường dẫn sẽ liệt kê các thư mục trong đường đãn hiện tại
# cd <tên thư mục> truy cập vào thư mục chỉ định
# cd .. rồi khỏi thực hiện tại
