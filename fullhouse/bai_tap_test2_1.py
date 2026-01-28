# đề bài 1
# name = input('Tên: ')
# nam_sinh = int(input('Năm sinh: '))
# thang_sinh = int(input('Tháng sinh (1-12): '))
# if thang_sinh > 12:
#     print(f'Xin chào {name.title()}! Bạn đã {2025 - nam_sinh -1} tuổi')
# if thang_sinh <= 12:  
#     print(f'Xin chào {name.title()}! Bạn đã {2025 - nam_sinh} tuổi')

#đề bài 2
# import math
# n = int(input('Nhập một số: '))
# tong = 0
# if n < 2:
#     print(f'{n} không phải số nguyên tố.')
# else:
#     for i in range(2,int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             tong +=1
#     if tong == 0:
#         print(f'{n} là số nguyên tố! Tuyệt vời! ')
#     else:
#         print(f'{n} không phải số nguyên tố.')

#đề bài3
# for i in range(9,1,-1):
#     for a in range(10,0,-1):
#         print(f'{i} x {a:>2} = {i*a}')

#đề bài 4
# import random
# a = random.choice(range(1,51))
# i = 0
# while i < 7:
#     b = int(input('Nhập số: '))
#     if b > a:
#         print('Quá lớn')
#     elif b < a:
#         print('Quá nhỏ')
#     else:
#         print('Đúng rồi')
#         break
#     i +=1
#     if i == 7 :
#         print(f'Thua rồi! Đáp án là {a}')

# #đề bài 5
# a = map(int,input('Nhập danh sách điểm: ').split(','))
# print(f'Danh sách điểm sau khi sắp xếp:{', '.join(map(str,sorted(a)))}')

#đề bài 6
# n = int(input('Nhập số n: '))
# tong = 0
# for i in range(2,n+1,2):
#     tong +=i
# print(f'Tổng các số chẵn từ 1 đến {n} là: {tong}')

#đề bài 7
# n = int(input('Nhập năm: '))
# def la_nam_nhuan(n):
#     a = n % 4 == 0 and ( n % 400 ==0 or n % 100 != 0 )
#     return a
# if la_nam_nhuan(n):
#     print(f'{n} là năm nhuận! ')
# else:
#     print(f'{n} không phải năm nhuận. ')

#đề bài 8
# n = input('Nhập ngày: ').title()
# lich_hoc = {'Thu 2': 'a,b,c','Thu 3': 'a,b,c','Thu 4': 'a,b,c','Thu 5': 'a,b,c','Thu 6': 'a,b,c','Thu 7': 'a,b,c'}

# if n in lich_hoc.keys():
#     print(f'Hôm nay học: {lich_hoc[n]}')
# else:
#     print('Ngày nghỉ học! Nghỉ ngơi thật vui nhé! ')

# if lich_hoc.get(n,0):
#     print(f'Hôm nay học: {lich_hoc[n]}')
# else:
#     print('Ngày nghỉ học! Nghỉ ngơi thật vui nhé! ')

#đề bài 9
# '''
# 1. Thêm điểm môn mới (tên môn + điểm)
# 2. Xem tất cả điểm
# 3. Tính điểm trung bình
# 4. Tìm môn cao điểm nhất
# 5. Thoát
# '''
# bang = {}
# def them_mon(bang):
#     mon = input('Môn: ')
#     diem = int(input('Điểm: '))
#     bang[mon] = diem
#     return 
# def xem_diem(bang):
#     for i,j in bang.items():
#         print(f'{i} - {j}')
#     return
# def diem_tb(bang):
#     tong_diem = 0
#     for i in bang.values():
#         tong_diem +=i
#     return tong_diem/len(bang)

# while True:
#     a = int(input('Nhập yêu cầu: '))
#     if a == 1:
#         them_mon(bang)
#     elif a == 2:
#         xem_diem(bang)
#     elif a == 3:
#         print(diem_tb(bang))
#     elif a == 4:
#         n = max(bang,key= lambda x : bang[x])
#         print(f'Điểm cao nhất: {bang[n]}')
#     elif a == 5:
#         break
#     else:
#         print('Nhập sai')


# đề bài 10
'''
1. Thêm học sinh mới (nhập tên, điểm Toán, điểm Văn → tự tính TB)
2. In bảng điểm toàn lớp (cột: STT | Tên | Toán | Văn | TB) – căn chỉnh đẹp
3. Tìm học sinh có điểm TB cao nhất
4. Đếm số học sinh giỏi (TB ≥ 8.0)
5. In danh sách học sinh cần nhắc nhở (TB < 5.0)
6. Thoát
'''
# bang = []
# def them():
#     ten = input('Nhap ten: ')
#     diem_toan = int(input('Nhap diem toan: '))
#     diem_van = int(input('Nhap diem van: '))
#     return {"ten":ten, "diem toan" : diem_toan, "diem van": diem_van, "diem tb": (diem_van+diem_toan)/2}
# def xem(bang):
#     stt = 0
#     for i in bang:
#         stt +=1
#         print(f"{stt:>3} | {i['ten']:>7} | {i['diem van']:>3} | {i['diem toan']:>3}")

#     return
# tong = 0
# while True:
#     a = int(input('Nhap yeu cau: '))
#     if a == 1:
#         bang.append(them())
#     elif a == 2:
#         xem(bang)
#     elif a== 3:
#         n = max(bang, key = lambda x: x['diem tb'])
#         print(n['diem tb'])
#     elif a == 4:
#         for i in bang:
#             if int(i['diem tb']) >= 8:
#                 tong +=1
#         print(f"So hoc sinh gioi: {tong}")
#     elif a == 5:
#         for i in bang:
#             if  int(i['diem tb']) < 5:
#                 print(i['ten'])
#     elif a == 6:
#         print('Thoat')
#         break
#     else:
#         print('sai cu phap')
                






# test 1

#de bai 1
# ten = input('Nhap ten: ')
# nam_sinh = int(input('Nhap nam sinh: '))
# print(f'Xin chào {ten.title()}')
# print(f'Bạn sinh năm {nam_sinh}, vậy năm nay bạn {2025-nam_sinh} tuổi.')
# print(f'Rất vui được gặp bạn! ')

#de bai 2
# diem_toan = int(input('Nhap diem Toan: '))
# if diem_toan not in range(0,11):
#     print('Điểm không hợp lệ, vui lòng nhập lại!')
# elif diem_toan == 10:
#     print("Xuất sắc! Giỏi lắm!")
# elif diem_toan == 8 or diem_toan == 9:
#     print( "Giỏi! Cố gắng giữ phong độ nhé!")
# elif diem_toan == 6 or diem_toan == 7:
#     print("Khá tốt! Cần cố gắng hơn chút nữa.")
# elif diem_toan == 5:
#     print("Trung bình, cần ôn lại bài.")
# else:
#     print("Yếu quá! Hãy học chăm chỉ hơn nhé!")


#de bai 3
# for i in range(1,11):
#     print(f'3 x {i:>2} = {i*3:>2}')

#de bai 4
# i = 10
# while i > 0:
#     print(i)
#     i -=1
# print('TÊN LỬA PHÓNG! ')

#de bai 5
# ds = []
# while True:
#     i = input('Nhap ten ban than: ')
#     if i == 'xong':
#         print('Danh sách bạn thân của bạn: ')
#         for i in range(1,len(ds)+1):
#             print(f'{i}. {ds[i-1]}')
#         break
#     else:
#         ds.append(i)

#de bai 6
# tong = 0
# print('Điểm thi đua tuần này: ')
# thu_trong_tuan = ['Thu hai', 'Thu ba','Thu tu', 'Thu nam', 'Thu sau']
# for i in thu_trong_tuan:
#     a = int(input())
#     print(f'{i} : {a}')
#     tong += a
# print(f'Tổng điểm tuần: {tong}')
# print('Chúc mừng lớp mình! ')

#de bai 7
# def tong(a,b):
#     return a + b
# a = int(input('Nhap so thu nhat: '))
# b = int(input('Nhap so thu hai: '))
# print(f'Tong la: {tong(a,b)}')

#de bai 8
# ds = []
# for i in range(3):
#     a = input(f'Nhap ten hoc sinh lan {i+1}: ')
#     b = int(input('Nhap tuoi: '))
#     c = {a : b}
#     ds.append(c)
# for hs in ds:
#     for ten, tuoi in hs.items():
#         print(f'{ten} - {tuoi} tuoi')

#de bai 9
'''
1. Chơi đoán số
2. Xem bảng cửu chương
3. Thoát
'''
# while True:
#     n = int(input('Lua chon cua ban : '))
#     if n == 1:
#         print('Bạn chọn chơi đoán số!')
#     elif n == 2:
#         print('Bạn chọn xem bảng cửu chương')
#     elif n == 3:
#         print('bạn chọn thoát')
#         break
#     else:
#         print('Sai cú pháp! Nhập lại')
# de bai 10
'''
1. Thêm học sinh 
2. Xem danh sách 
3. Tìm thủ khoa 
4. Thoát 
'''
# bang = []
# def them():
#     ten = input('Nhap ten: ')
#     diem = int(input('Nhap diem Toan: '))
#     return {'ten': ten, 'diem': diem}

# def xem(bang):
#     for i in bang:
#         print(f'{i['ten']:<7} - {i['diem']}')
#     return 

# while True:
#     n = int(input('Chon: '))
#     if n == 1:
#         bang.append(them())
#     elif n == 2:
#         xem(bang)
#     elif n == 3:
#         a = max(bang,key=lambda x : x['diem'])
#         print(a['ten'])
#     elif n == 4:
#         break
#     else:
#         print('Sai cú pháp! Chọn lại.')















