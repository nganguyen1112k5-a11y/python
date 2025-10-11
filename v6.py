#vòng lặp for lặp lại thông qua 1 giá trị nhất định hoặc cho đến khi điều kiện được đáp ứng

nums=[1,2,3,4,5,]
for num in nums:
    print(num) #sẽ giúp liệt kê các giá trị trong danh sách 

#kết hợp vòng lặp for và câu lệnh nếu if
for num in nums:
    if num==3:
        print('found')
        break # Thoát hẳn khỏi vòng lặp.
    print(num) #khi for tìm đến giá trị 3 như yêu cầu thì câu lệnh sẽ được in ra "found"và kết thúc quá trình

#hoặc vẫn có thể giúp câu lệnh for tiếp tực bằng cách
for num in nums:
    if num==3:
        print('found')
        continue #Bỏ qua phần còn lại của vòng lặp hiện tại và sang vòng lặp kế tiếp.
    print(num) #lệnh for vẫn tiếp thưc hiện khi num đã tìm được giá trị mong muốn

#thực hiện vòng lặp chèn 
for num in nums:
    for so in 'abc':
        print(num, so)
        #giá trị đưa ra là vòng lặp từ trong ra ngoài

#vòng lặp in ra teheo phạm vị chủ định
for n in range(10):
    print(n) #giá trị đưa ra sẽ thực hiện từ 0 đến 9 không bao gồm 10

for n in range(1,10):
    print(n) #giá trị đưa ra từ 1 đến 9

# #vòng lặp while vô thời hạn cho đến khi đáp ứng được diều kiện đưa ra

x=0
while x<10:
    print(x)
    x+=1 #vòng lặp thực hiện liên tục cho đến khi x = 10 thì giá trị không thoả mãn điều kiện đưa ra khi đó vòng lặp sẽ dừng lại

while x < 10:
    x+=1
    print(x) #khi thực hiện lệnh này thì vòng lặp sẽ thực hiện vô thời định do không có bất  kì điều kiện nào chỉ định và giá trị in ra sẽ là 0 và lặp đi lặp lại
    break
#giá trị đưa ra là 1 
while x < 10:
    print(x) #khi thực hiện lệnh này thì vòng lặp sẽ thực hiện vô thời định do không có bất  kì điều kiện nào chỉ định và giá trị in ra sẽ là 0 và lặp đi lặp lại
    x+=1
    break
#giá trị đưa ra là 0
x=0
while x<10:
    if x==5:
        print('found')
        break
    print(x)
    x+=1


x=0
while True:
    if x==5:
        print('found')
        break
    print(x)
    x+=1
#khi thực hiện True thì chắc chắn phải cần lệnh break để đừng lại nếu không nó sẽ thực hiện vô hạn định

#nếu bị mắc kẹt trong vòng lặp vô hạn nhấn Ctrl c để dừng

