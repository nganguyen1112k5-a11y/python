

## CÂU LỆNH ĐIỀU KIỆN


# độ thụt lề (indentation)


# n = int(input())

# if n > 0:
#     print('n là số dương')
# elif n > 0:
#     print('n bang 0')
# else:
#     print('n là só âm')

# trong if else
# khi cùng các điều kiện đúng thì chỉ in ra điều kiện đầu tiên
# bởi khi chứa else:có nghĩa là khác nên các điều kiện sau đó sẽ bỏ qua

# trong if if 
# còn nếu không có else câu lệnh không có mặt khác nên nó sẽ được tiếp tục khi điều kiện đúng



# điều kiện lồng nhau
# x = int(input())
# if x >=5:
#     if x <= 8 :
#         print('khá')
#     else:
#         print('giỏi')
# else:
#     if x <3:
#         print('yếu')
#     else:
#         print('trung bình')







## VÒNG LẶP 



# mục dích để thực hiện lặp đi lặp lại nhiều lần mà không cần sử dụng câu lệnh lại


#range (phạm vi): chức năng để sinh ra các phần tử 
# (start,stop,step) mặc định start = 0 step = 1
# --> chạy từ start đến stop - 1 : không lấy giá trị stop

# ds = (4,10)
# print(ds)  #range(4, 10)
# print(list(ds))  #[4, 5, 6, 7, 8, 9]

# print(list(range(1,10,2)))

#mục dích của range là để tạo ra 1 dãy số nguyên liên tiếp theo bước nhảy step

# for <tên biến> in <tập hợp> :


# name = 'nga'
# for i in name:
#     print(i,end='')

# for i in range(2,10):
#     for a in range(1,11):
#         c = i*a
#         print(f'{i} x {a} = {i*a}')


# 1 vong
# a = '*'
# for i in range(1,9):
#     print(a*i)

# 2 vong
# n = int(input())
# for i in range(n):
#     for a in range(n):
#         if n-i-1 <= a  :
#             print('*',end='')
#         else:
#             print(' ',end='')  #end='' ngắt dòng không cho câu lệnh tiếp theo xuống dòng
#     print()  #xuống hàng
    

# n = int(input())
# for a in range(n):
#     if a % 2 == 0:
#         for b in range(2*n):
#           if b == a + 2:
#             print('*',end='')
#         else:
#             print('',end='')
#     else:
#        for b in range(2*n):
#         if b == a + n:
#             print('*',end='')
#         else:
#             print('',end='')
#     print()


# for i in range(1,9):                # số dòng từ 1 → 8
#     for j in range(8 - i):           # in khoảng trắng phía trước
#         print(' ', end=' ')
#     for k in range(2 * i-1):       # in dấu * (1, 3, 5, ... tăng dần)
#         print('*', end=' ')
#     print()                          # xuống dòng
# for b in range(1,4):
#     for a in range(2,18):
#         if a<=6 or a>=12:
#             print(' ',end=' ')
#         else:
#             print('*',end=' ')
#     print()


# n = 8  # chiều cao của cây

# for i in range(1, n + 1):
#     # in khoảng trắng bên trái
#     for j in range(n - i):
#         print(' ', end=' ')
#     # in các dấu *
#     for k in range(2 * i - 1):
#         print('*', end=' ')
#     print()

#while <điều kiện xác định>:




## DANH SÁCH




# #đưa giá trị trong list append: thêm vào cuối
# danh_sach = [1,2,3,4,5]
# danh_sach.append(6)
# print(danh_sach)


# gia_tri = input().split() #1 2 3 4 5
# ds_so_nguyen = []
# for item in gia_tri:
#     ds_so_nguyen.append(int(item))  #đưa về dạng số khi cho vào danh sách
# print(ds_so_nguyen) #[1, 2, 3, 4, 5]


# nối danh sách

#extend làm thay đổi giá trị ban đầu, là giá trị bởi extend chỉ định
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# list1.extend(list2)
# print(list1)

# + khi kết list sẽ không kàm thay đổi giá trị ban đầu:
# new_list = list1 + list2
# print(new_list)


# xóa : remove (xóa theo giá trị ) và pop (xóa theo vị trí)

# ds = [1,2,3,4,5,6]
# ds.remove(3) #xóa giá trị 3
# ds.pop(1)  #xóa giá trị tại chỉ mục thứ 1 mặc định không viết xóa ở vị trí nào thì xóa ở cuối cùng
# print(ds)

# chèn thêm : insert (chèn thêm giá trị vào chỉ mục mong muốn)

# ds = [1,2,3,4,5,6]
# print(ds[0],ds[-1]) #1 6

# ds.insert(1,20)  #chèn thêm vào chỉ mục 1 giá trị 20
# print(ds) #[1, 20, 2, 3, 4, 5, 6]


# đếm số lượng giá trị và lấy vị trí giá trị đầu tiên trong danh sach trong danh sách

# ds = [1,1,2,4,5,6]
# print(ds.count(1)) #2  #đếm số lượng giá trị
# print(ds.index(1)) #0  #lấy vị trí của giá trị đầu tiên


## không nguyên thủy
#reference (tham chiều)  


# a = [1,2,3,4,5]
# b = a.copy() #đưa sang ô nhớ mới tránh anh hưởng ô nhớ ban đầu
# b.append(6)
# print(a,b)  #[1, 2, 3, 4, 5] [1, 2, 3, 4, 5, 6]



# a = [1,2,3,4,5]
# new_a = list(reversed(a)) #tạo 1 danh sách mới
# print(new_a)  #[5, 4, 3, 2, 1]
# a.reverse() #thay đổi trực tiếp ở danh sách
# print(a)  #[5, 4, 3, 2, 1]

# b = [1,2,8,6,5]
# new_b = sorted(b)
# print(new_b) #[1, 2, 5, 6, 8]
# b.sort()
# print(b) #[1, 2, 5, 6, 8]



# ## 

# x,*ds = map(int,input().split())
# # print(int(x))
# print(ds)
# # new_ds = []
# # for item in ds:
# #     new_ds.append(int(item))
# # print(new_ds)
# # print(new_ds.count(x))
# for a in range(len(ds)):
#     if x == ds[a]:
#         print(a+1,end=' ')
    





## DANH SÁCH <list slicing>

#cắt trong danh sách
#P = []
#   P[start:stop:step]

# ds = [1,2,3,4,5]
# a = ds[2:4]
# print(a)

# dựng chức năng trong list slicing
#có thể thay đổi trên nhiều danh sách

#append() : thêm giá trị vào cuối dánh sách
#List Slicing cách thêm vào cuối l[start:stop] = [...]start = stop

# ds = [1,2,3,4,5]
# ds[4:] = [100]
# ds[ds.__len__():] = [1000] #thêm vào cuối ds 
# print(ds)  #[1, 2, 3, 4, 100, 1000]

# ds[1:2] = [20]    #thay  thế
# print(ds)  #[1, 20, 3, 4, 100, 1000]

# ds[1:1] = [20]    #chèn theo vị trí bất kỳ
# print(ds)

# ds[1:] = [20]
# print(ds)   #[1,20]  thay 20 vào chỉ mục 1 đến cuối do  [20] thay thế cho [1:] 

# ds[ds.__len__()-2:] = [1000]
# print(ds)    #[1, 2, 3, 1000]


# ds[ds.__len__()-2:] = [1000]   #thay thế vào vị trí cuối -2
# print(ds)

# tương tự như xóa bằng cách chèn [] vào như chèn giá trị
#giá trị sau khi stop -1 = start  

#ex
# ds[1:2] = []    #thay  thế
# print(ds)  #[1, 3, 4, 5]

# copy_ds = ds[:]
# print(copy_ds)
# print(id(ds))
# print(id(copy_ds))



#Đảo ngược danh sách (reverse)

# reverse_ds = ds[::-1]
# print(reverse_ds)

#daor ngược đoạn bất kì
# reverse_ds = ds[1:3][::-1] #[đoạn in][đảo đoạn muốn in]
# print(reverse_ds)

# ds[1:3] = ds[1:3][::-1] #[đoạn in][đảo đoạn muốn in]
# print(ds)

ds = [1,4,9,7,6,3,8,5]
# ds[2:6] = sorted(ds[2:6]) #sắp xếp đoạn[2:6]
# print(ds)  #[1, 4, 3, 6, 7, 9, 8, 5]


# for item in ds[2:6]:
#     item = 10
# print(ds)


#Cú pháp vắn tắt của list

# [expersion for item in iterable (không bắt buộc điều kiện if else)]


# print([i*i for i in range(10)]) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# #trước for là giá trị muốn trả về

# print([i*i for i in range(10) if i % 2 == 0])  #[0, 4, 16, 36, 64]


# ds = [1,4,9,7,6,3,8,5]
# k = 3
# for i in range(0,ds.__len__()-k+1):
#     print(ds[i:i+k])




##  tuple và set  (dấu ngoặc tròn và  tập hợp )



# tuple là dạng cấu trúc không thay đổi được (immutable)


#ex
t = (1,2,3,4,5)
# t[0] = 100
# print(t)  #ko thực hiện được  <'tuple' object does not support item assignment>

# for item in t:
#     print(item*6)


#thay đổi trong tuple bằng cách ép kiểu qua list rồi thay đổi và đưa lại về tuple

# ds = list(t)
# ds[0] = 100
# t = tuple(ds)
# print(t)  #(100, 2, 3, 4, 5)


# set tập hợp 
#giao intersection
#hợp union
#khác difference

#cấu trúc dữ liệu ():sử dụng khi cần ép kiểu, {} bình thường

s1 = {1,2,3,4}
s2 = {3,4,5,6}
# print(s1.intersection(s2)) # giao
# print(s1.difference(s2))  #khác
# print(s1.union(s2)) #hợp
# print(s1.symmetric_difference(s2)) #lấy phần khác 

# a = (1,2,3,4,2,4,5,7,4,6,9,0)   #sử dụng được với () [] {}   
# print(set(a)) kết quả luôn đưa ra {}

# print(s1 | s2) #hợp
# print(s1 - s2)  #khác
# print(s1 & s2)  #giao
# print(s1 ^ s2)   # lấy phần khác nhau <triệt tiêu giá trị xác định>


## set là cấu trúc không có trật tự, vì vậy không truy cập theo vị trí được
# s = {1,2,3,4}
# l = [1,2,3,4]
# print(4 in s)  
# print(4 in l)

# s = set({})
# s.add(1)
# s.add(0)
# s.add(1)
# print(s)  #{0, 1}  các giá trị giông nhau nó sẽ đè lên nhau

# s = 'bcad'
# print(set(s))

# n = set(map(int,input().split()))
# n.discard(100)  #hàm xóa khi xóa giá trị trong hàm nó không báo lỗi và chỉ thực hiện được trên set
# print(n)

##issubset : kiểm tra tập con
##issuperset : kiểm tra tập cha

# s_child = {1,2,3}
# s_parent = {1,2,3,4,5}
# print(s_child.issubset(s_parent))   #kiểm tra s_child là con của s_parent
# print(s_parent.issuperset(s_child))  #kiểm tra s_parent là cha của s_child





## XỬ LÝ SÂU KÝ TỰ (STRING)


# string là cấu trúc tập hợp chứa được nhiều ký tư
# có thể truy cập được vào các vị trí

# - vị trí : 0 -> n-1 (n là số lượng phần tử)
#            -n -> -1

# s = 'hello'
# a = s[0]
# print(a)

# quy tắc đặt tên biến:
# - underscore case
# + tên file, fodder
# + tên biến, hàm chức năng
# - snake case

# nguyên thủy thì khi thay đổi giá trị không làm thay đổi ô nhớ

# không thể thực hiện gán giá trị s[0] = 'k' bởi nó đã được thêm vào 1 ô nhớ nên khi gán sẽ làm thay đổi ô nhớ nên không thể được

#nhân bản ký tự sử dụng phép nhân đơn giản
# a = '1'*4300
# b = int(a)
# print(a)
# print(b)

#copy() giúp đưa sang ô nhớ mới

# buldt in function
#  strip() xóa đi khoảng trắng đầu cuối
# name = '  nguyen dinh nga  '
# name = name.strip()
# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())
# print(name.split())
# name = '+'.join(name)
# print(name)



#lower viết thường các chữ cái
# upper viết hoa tất cả các chữ cái
# title viết hoa các chữ cái dầu tiên của mỗi từ
# capitalize viết hoa chữ cái đầu cửa đoạn
# split tạo khoảng trắng giữa các kí tự và các ký tự đưa vè dạng danh sách
# ''.join đưa về các kiểu dự liệu chuỗi

# islower có phải viết thường không

#ord truy cập vào vị trí ký tự

# n = input()
# danh_sach_dem = [0]*255
# for ki_tu in n:
#     danh_sach_dem[ord(ki_tu)] +=1
# max_val = -1e9
# vi_tri_max = 0
# for i in range(len(danh_sach_dem)):
#     if danh_sach_dem[i] > max_val:
#         max_val = danh_sach_dem[i]
#         vi_tri_max = i
# print(chr(vi_tri_max), max_val)




## HÀM CHỨC NĂNG (FUNCTION)




# def hello():
#     print('hello')
# hello()
# hello()
# hello()
# hello()

# return : +kết thúc chương trình
#          + trả về giá trị

# def tong(a,b):
#     print(a +b)
#     return
# tong(1,2)


# lưu ý vừa có tham số bắt buộc vừa có tham số mặc định thì tham số bắt buộc đứng sau tham số mặc định

# def tong(a, b = 0):
#        # 1 tham số bắt buộc 2 tham số mặc định
#     print(a+b)
#     return
# tong(1)

# def tong(a,*,b,c):  #bắc buộc ghi tên khi khai báo sau dấu * 
#     return a + b + c
# print(tong(1,c = 1, b = 2))

# def tong(*args):  #tham số tư do khi khai báo sẽ có dạng tuple
#     t = 0 
#     for i in args:
#         t +=i
#     print(t)
#     return
# tong(1,2,3,4,5)


# def tong(**kwargs):   #truyền theo tên
#     print(kwargs)
# tong(a = 1, b = 2, c = 3)  #{'a': 1, 'b': 2, 'c': 3}


#  hàm ưu tiên vị trí hơn là truyền theo tên

# def tong(*args, **kwargs):
#     return args, kwargs
# print(tong(1,2,3, a = 1 , b = 2, c = 3))



# #biến toàn cục 
# global    cho phép lấy giá trị toàn cục 
# local     chỉ cho phép lấy giá trị bên trong hàm
# nonlocal
# có 3 phạm vi nó không được tác động lẫn nhau


# a = 1

# def dem():
#     global a
#     a+=1
#     print(a+2)
# dem()

# a = 1
# def dem():
#     global a
#     a+=1
#     print(a+1)
#     b = 0
#     def in_dem():
#         nonlocal b #dùng để cấp quyền cho local
#         b +=1
#         print(b)
#         c = 2
#         def in_dem2():
#             nonlocal b,c
#             b+=1
#             c+=1
#             print(b,c)
#         in_dem2()
#     in_dem()
# dem()



# a =1
# def dem():
#     global a
#     a+=1
#     print(a+1)
#     b = 0
#     c = 1
#     def in_dem():
#         nonlocal b #dùng để cấp quyền cho local
#         b +=1
#         print(b)
#         # c = 2
#         def in_dem2():
#             nonlocal b,c
#             b+=1
#             c+=1
#             print(b,c)
#         in_dem2()
#     in_dem()
# dem()


# a,b,c=2,2,2

# def solve(pa=a, pb=b, pc=c):
#   global a,b,c
#   c+=1
#   non_a, non_b, non_c = a,b,c
#   def inner():
#     nonlocal non_a, non_b, non_c
#     s=non_a+non_b+non_c
#     return a+b+c/s
#   i1 = inner() * c * pa *(b-c)
#   return i1

# print(solve())






## callback(gọi lại hàm)

#truyền hàm 
# def tong(a,b):
#     return a+b

# def call_cong(fn,a,b):
#     return fn(a,b)

# print(call_cong(tong,1,2))
       

# xét theo tiêu chí
# def tieu_chi(n):
#     return abs(n)
# ds = [-10,-20,5,20,2,10,30]
# dap_an = sorted (ds,key= abs)  #[2, 5, -10, 10, -20, 20, 30]
# print(dap_an)


def tieu_chi(n):
    return abs(n)
# ds = [-10,-20,5,20,2,10,30]
# dap_an = sorted (ds,key= tieu_chi)  #[2, 5, -10, 10, -20, 20, 30]
# print(dap_an)


# def tieu_chi(n):
#     return -abs(n)
# ds = [-10,-20,5,20,2,10,30]
# dap_an = sorted (ds,key= tieu_chi)  #[30, -20, 20, -10, 10, 5, 2]
# print(dap_an)


# đa tiêu chí

# def tieu_chi(n):
#     return (
#         abs(n), #tiêu chí 1
#         -n,      #tiêu chí 2
#     )
# ds = [-10,-20,5,20,2,10,30]
# dap_an = sorted (ds,key= tieu_chi)  #[2, 5, 10, -10, 20, -20, 30]
# print(dap_an)



# s = input()
# t = [0]*255
# for i in s:
#     t[ord(i)] +=1
# max = 0
# vi_tri = 0
# for a in range(len(t)):
#     if t[a] >= max:
#         max = t[a]
#         vi_tri = a
# print(chr(vi_tri), max)

# s = 'aabbcc'
# def tieu_chi(n):
#     return(
#         s.count(n),     # tiêu chí 1 đếm số lượng từ
#         -ord(n)              #so sánh ký tự
#     )

# dap_an = sorted(s,key= tieu_chi)
# print(dap_an[-1], s.count(dap_an[-1]))       # a 2

    

# s = 'aabbcc'
# def tieu_chi(n):
#     return(
#         s.count(n),     # tiêu chí 1 đếm số lượng từ
#         n              #so sánh ký tự
#     )

# dap_an = sorted(s,key= tieu_chi)
# print(dap_an[-1], s.count(dap_an[-1]))    # c 2




# ds_sp = [
#     #10 sp
#     ['ip 10', 2000, 'red',2023],
#     ['ip 11', 3000, 'blue',2024],
#     ['ip 12', 4000, 'orange',2023],
#     ['ip 13', 5000, 'black',2022],
#     ['ip 14', 6000, 'red',2024],
#     ['ip 15', 7000, 'new',2024],
#     ['ip 16', 8000, 'red',2023]
# ]

# def tieu_chi(n):
#     return (
#         -n[3],
#         n[1]
#     )
# dap_an = sorted(ds_sp,key=tieu_chi)
# print(dap_an[0])


## hàm ẩn danh, hàm tắt:
# lamda đối_số : biểu_thức


# tong = lambda x,y :x + y
# print(tong(1,2))

# ds_sp = [
#     #10 sp
#     ['ip 10', 2000, 'red',2023],
#     ['ip 11', 3000, 'blue',2024],
#     ['ip 12', 4000, 'orange',2023],
#     ['ip 13', 5000, 'black',2022],
#     ['ip 14', 6000, 'red',2024],
#     ['ip 15', 7000, 'new',2024],
#     ['ip 16', 8000, 'red',2023]
# ]

# def tieu_chi(n):
#     return (
#         -n[3],
#         n[1]
#     )
# dap_an = sorted(ds_sp,key=lambda n:(
#     -n[3],
#     n[1]
# ))
# print(dap_an[0])


#key luôn áp dụng lên từng phần tử, không bao giờ áp dụng lên cả danh sách.




## Hàm chức năng map

# ds = [1,2,3,4]
# def binh_phuong(n):
#     return n*n

# print(list(map(binh_phuong,ds)))  #truyền qua từng giá trị
# print(list(map(lambda n : n*n,ds)))

ds = [
    ['ip 15', 2000, 2025],
    ['ip 14', 4000, 2025],
    ['ip 16', 2000, 2025],
    ['ip 13', 6000, 2025],
    ['ip 14', 2000, 2025],
    ['ip 15', 4000, 2025],
    ['ip 14', 3000, 2025]
]
def giam_gia(n):
    n[1] = n[1]*0.9
    
    return n
# print(list(map(giam_gia,ds)))





# Filter bộc lọc , kết quả trả về nếu điều kiện đúng

# print(list(filter(lambda n : n[1] == 2000, ds)))   #in ra cái đúng 
#[['ip 15', 2000, 2025], ['ip 16', 2000, 2025], ['ip 14', 2000, 2025]]




# new_ds_sp = new_ds_sp.copy()
# dap_an = sorted(new_ds_sp, key= lambda n : (
#     n[7][1],
#     -n[4][1]))
# print(dap_an)






## CHUỖI KÝ TỰ
#chuỗi kí tự được đặt trong nháy ' ' hoặc " "
# khi nháy đơn bên trong thì nháy kép bên ngoài hoặc ngoặc lại
# chuỗi là một tập hợp các kí tự -> không thay đổi được giá trị ban đầu

# chuoi = "nguyen dinh'nga'"
# chuoi1  = '''nga'nguyên' "dinh"'''
# print(chuoi,chuoi1)


#cắt chuỗi
# s = 'hello'
# print(s[:2])
# print(s[-2:])
# print(s[3:0:-1])


#format căn chỉnh trong văn bản 
# <giống như sinh ra ô trống và chèn kí tự trong ô trống sinh ra>


# name = 'menu'
# print(f'{name:^50}') #căn giữa
# print(f'{name:<50}') #căn trái
# print(f'{name:>50}') #căn phải

        
        
# for i in range(2, 10):
#     for j in range(1, 11):
#         print(f"{i} x {j:>2} = {i*j:>}")


# name = '   ngUyen vAn Nam  '
# print(name.strip().title())  #trái qua phải  và trong ra ngoài

#range(len(s)-1, -1, -1)   chạy từ cuối lên đầu

#sliding window (cửa sổ trượt):


'''
từ chuỗi đầu vào tạo cụm 3 từ liên tục từ chuỗi đã cho
vd :
dhjqeeqvn
-dhj
-hjq
...
'''






## từ điển (dictionary)





# key - value
# key không được trùng lặp nếu trùng key python sẽ lấy value của key trùng phía sau và value cũng vậy

# - dic(): khởi tạo và ép kiểu dữ liệu sang dictionary
# { key: value } : key diu nhất và kiểu dữ liệu thuộc primitive types

use = {
    'name' : 'nguyen dinh nga',
    'age' : 20,
    'city' : 'hn'
}
# print(use)
# print(use['name'])
# print(use['age'])

# use['name'] = 'nga nguyen'  # thay đổi value của key 'name'

# print(use)
# print(use['name'])


#Truy cập an toàn 
# nếu key không toàn tại trong dic thì không bị lỗi và sẽ đưa ra giá trị None hoặc giá trị đặt sẵn

# print(use.get('phone'))
# print(use.get('phone','khong co'))  

# chỉ dùng để lấy giá trị không để thay đổi giá trị

# thêm key - value
use['phone'] = 123456789
# print(use)

# print(use.keys())
# print(use.values())
# print(use.items())  #cả 2

# #copy trong dic
# use_copy = use.copy()
# print(use_copy)
# use_copy = {**use}
# print(use_copy)

# tạo dic trống cho lần tiếp theo với key giữa nguyên
# new_use = {}.fromkeys(use.keys(), )
# print(new_use)

# products = [
#     {
#         "id": 1,
#         "name": "Iphone 14",
#         "price": 2000,
#     },
#     {
#         "id": 2,
#         "name": "Iphone 15",
#         "price": 3000,
#     },
#     {
#         "id": 3,
#         "name": "Iphone 16",
#         "price": 4000,
#     },
#     {
#         "id": 4,
#         "name": "Iphone 17",
#         "price": 5000,
#     },
# ]

# def ham(n):
#     return 'price'
# dap_an = sorted(products, key = ham)
# print(dap_an[0],dap_an[-1])
# ham(products)
    




## list kết hợp với dic
# abs.py




## ĐƯỜNG DẪN TƯƠNG ĐỐI VÀ ĐƯỜNG DẪN TUYỆT ĐỐI
# path đường dẫn
#tương đối


'''
là nên dùng rel path, absolute path

rel path : xác định cho 1 thư mục không cần truy xuất tối ổ đĩa



khi truy cập cần truy cập vào đường dẫn tuyệt đối (absolute path)
'''


print(__file__)   #tìm file đang làm việc

from pathlib import Path

BASE_DIR = Path(__file__).parent #resolve trích xuất thư mục con từ parent(cấp cha)

INPUT_PATH = BASE_DIR/'test.txt'
# constant : hằng số không đối (khi viết in hoa hết thường sẽ ít hoặc không thay đổi)

print(BASE_DIR)
print(INPUT_PATH)

# with open(INPUT_PATH,"r", encoding='utf-8') as file:
    # content = file.read()  #in cả 
    # lines = file.readlines() #đọc từng dòng, sẽ trả lại 1 list
    # line = file.readline()  # đọc 1 dòng đầu
    # print(content)
    # print(lines)
    # print(line)

    # file.write("hello")  #  ??

# with open(INPUT_PATH,"r", encoding='utf-8') as file:
#     content = file.read(50)  #in ra đến vị trí n-1
#     print(content)

# os.getcwd() #trả về thư mục làm việc hiện tại




