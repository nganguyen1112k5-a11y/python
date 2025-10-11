#câu lệnh nếu
n=True
if n:
    print('nga') #giá trị True
else:
    print('nga')#giá trị đưa ra là rỗng

#nếu 
laguage='nga'
if laguage==12:
    print('True')
else:
    print('False')

#thực thi cho đến khi đúng hoặc đến else

# #sử dụng if and lệnh và
n='nga'
m=False
l=True
if n=='nga' and m: #do đi cũng m=False nến giá trị đưa ra cũng là sai
    print('yep')
else:
    print('??')
# if or lệnh hoặc
n='nga'
m=False
l=True
if n=='nga' or m: #chỉ cần 1 trong 2 đúng
    print('yep')
else:
    print('??')

#if not 
m=True
if not m:
    print('yep') #nếu không đúng thì là sai còn nếu không sai thì đúng
else:
    print('no')

#
a=1
b=1
print(a==b)#giá trị đưa ra là True
print(a is b) #a là b sai do id của 2 biến khác nhau chỉ có giá trị giống nhau
print(id(a))
print(id(b))


#đánh giá True False
#các tập hợp '', [], {}, () đưa ra giá trị False
#các chuỗi, số hanh danh sách đều đưa giá trị True
m=[]
if m:
    print('True')
else:
    print('False')

