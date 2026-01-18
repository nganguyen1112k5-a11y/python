import pygame

pygame.init()

screen = pygame.display.set_mode((500,600))   #tạo màn hình trình chiều

GREY = (150,150,150)  #tạo màu

WHITE = (255,255,255) #tạo màu 

running = True

while True:
    screen.fill(GREY)   #Thay đổi màu trên màn hình thông qua fill

    pygame.draw.rect(screen,WHITE, (100,50,50,50)) #tạo hình bên trong mà hiển thị với draw.rect(tạo hình chữ nhật), màu WHITE , và tạo độ ở 100,50 kích thước hình 50,50

    for event in pygame.event.get():      #set những sự kiện ở trong event như tác động chuột
        if event.type == pygame.QUIT:      # type: Loại event , QUIT là 1 nút của pygame
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:   #sử dụng chuột để điều chỉnh thực hiện 
            if event.button == 1:   # ấn chuột trái
                print('nga')
            if event.button == 3:   # ấn chuột phải
                print('dinh')       
        

    pygame.display.flip()     #flip dùng để đưa màu vừa thay đổi hiển thị lên màn hình


pygame.quit() #dùng đề xóa toàn bộ chương trình sử dụng khi dùng xong ko lưu trữ làm nặng bộ nhớ










