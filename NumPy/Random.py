from numpy import random as rd

#LÀM VIỆC VỚI SỐ NGẪU NHIÊN randint(), rand()

# x = rd.randint(100)
# print(x)       # in ra số ngẫu nhiên từ 0-99

# x= rd.rand()
# print(x)            # in số ngẫu nhiên từ 0-1

# x = rd.randint(100,size=(5))   #in ra mảng chứa 5 số ngẫu nhiên
# y = rd.randint(100,size=(3,3))   #in ra mảng 2 chiều chứa 3 mảng mỗi mảng 3 giá trị ngẫu nhiên
# print(x,y)   

#LÀM VIỆC VỚI MẢNG GIÁ TRỊ CÓ SẴN

a = [1,2,3,4,5,6,7]
x = rd.choice(a)       #in ra giá trị bất kỳ trong a
y = rd.choice(a,size = (2,2))     #in ra mảng 2 chiều chứa giá trị ngẫu nhiên trong a
print(x,y)      
