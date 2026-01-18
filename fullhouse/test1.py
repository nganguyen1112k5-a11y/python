try:
    # ===== IMPORT THƯ VIỆN =====
    import pygame        # Thư viện làm game/giao diện
    import time          # Dùng sleep để tạo độ trễ
    import math          # Dùng sin, cos, pi cho kim đồng hồ

    # ===== KHỞI TẠO PYGAME =====
    pygame.init()        # Khởi tạo tất cả module pygame

    # ===== TẠO CỬA SỔ =====
    screen = pygame.display.set_mode((500, 600))  # Kích thước cửa sổ 500x600

    # ===== KHAI BÁO MÀU =====
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY  = (120, 120, 120)
    RED   = (255, 0, 0)

    # ===== FONT CHỮ =====
    font = pygame.font.SysFont('sans', 50)  # Font sans, cỡ 50

    # ===== TẠO TEXT (NÚT BẤM) =====
    text_1 = font.render('+', True, BLACK)       # + phút
    text_2 = font.render('-', True, BLACK)       # - phút
    text_3 = font.render('+', True, BLACK)       # + giây
    text_4 = font.render('-', True, BLACK)       # - giây
    text_5 = font.render('Start', True, BLACK)   # Start
    text_6 = font.render('Reset', True, BLACK)   # Reset

    # ===== BIẾN THỜI GIAN =====
    total_secs = 0      # Tổng số giây đếm ngược
    total = 0           # Lưu tổng ban đầu (dùng cho progress bar)
    is_start = False    # Trạng thái đang chạy hay không
    secs = 0            # Số giây hiển thị
    mins = 0            # Số phút hiển thị
    running = True      # Điều khiển vòng lặp chính

    # ===== BÁN KÍNH KIM =====
    r_sec = 90           # Độ dài kim giây
    r_min = 50           # Độ dài kim phút

    # ===== CLOCK FPS =====
    clock = pygame.time.Clock()  # Giới hạn tốc độ vòng lặp

    # ===== VÒNG LẶP CHÍNH =====
    while running:
        clock.tick(60)          # Giới hạn 60 FPS
        screen.fill(GREY)       # Tô nền màu xám

        # Load âm thanh báo thức
        sound = pygame.mixer.Sound('alarm.wav')

        # Lấy vị trí chuột
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # ===== VẼ CÁC NÚT =====
        pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))   # + phút
        pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))  # - phút
        pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))   # + giây
        pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))  # - giây
        pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))  # Start
        pygame.draw.rect(screen, WHITE, (300, 150, 150, 50)) # Reset

        # ===== VẼ CHỮ =====
        screen.blit(text_1, (100, 50))
        screen.blit(text_2, (100, 200))
        screen.blit(text_3, (200, 50))
        screen.blit(text_4, (200, 200))
        screen.blit(text_5, (300, 50))
        screen.blit(text_6, (300, 150))

        # ===== VẼ THANH TIẾN TRÌNH =====
        pygame.draw.rect(screen, BLACK, (50, 520, 400, 50))   # Viền ngoài
        pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))  # Bên trong

        # ===== XỬ LÝ SỰ KIỆN =====
        for event in pygame.event.get():

            # Thoát chương trình
            if event.type == pygame.QUIT:
                running = False

            # Nhấn chuột
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Chuột trái
                    pygame.mixer.pause()  # Dừng âm thanh

                    # + phút
                    if 100 < mouse_x < 150 and 50 < mouse_y < 100:
                        total_secs += 60
                        total = total_secs

                    # - phút
                    if 100 < mouse_x < 150 and 200 < mouse_y < 250:
                        total_secs -= 60
                        total = total_secs

                    # + giây
                    if 200 < mouse_x < 250 and 50 < mouse_y < 100:
                        total_secs += 1
                        total = total_secs

                    # - giây
                    if 200 < mouse_x < 250 and 200 < mouse_y < 250:
                        total_secs -= 1
                        total = total_secs

                    # Start
                    if 300 < mouse_x < 400 and 50 < mouse_y < 100:
                        is_start = True
                        total = total_secs

                    # Reset
                    if 300 < mouse_x < 400 and 150 < mouse_y < 200:
                        total_secs = 0
                        is_start = False

        # ===== ĐẾM NGƯỢC =====
        if is_start:
            total_secs -= 1          # Giảm 1 giây
            if total_secs == 0:
                pygame.mixer.Sound.play(sound)  # Hết giờ → kêu
            time.sleep(0.03)         # Làm chậm vòng lặp

        # Không cho thời gian âm
        if total_secs < 0:
            total_secs = 0
            total = 0
            is_start = False

        # ===== TÁCH PHÚT & GIÂY =====
        secs = total_secs % 60
        mins = int((total_secs - secs) / 60)

        # ===== HIỂN THỊ THỜI GIAN =====
        time_str = str(mins) + " : " + str(secs)
        text_min = font.render(time_str, True, BLACK)
        screen.blit(text_min, (120, 120))

        # ===== VẼ MẶT ĐỒNG HỒ =====
        pygame.draw.circle(screen, BLACK, (250, 400), 100)
        pygame.draw.circle(screen, WHITE, (250, 400), 95)
        pygame.draw.circle(screen, BLACK, (250, 400), 5)

        # ===== VẼ KIM GIÂY =====
        pygame.draw.line(
            screen, BLACK,
            (250, 400),
            (
                250 + int(r_sec * math.sin((secs / 180) * 6 * math.pi)),
                400 - int(r_sec * math.cos((secs / 180) * 6 * math.pi))
            )
        )

        # ===== VẼ KIM PHÚT =====
        pygame.draw.line(
            screen, RED,
            (250, 400),
            (
                250 + int(r_min * math.sin((mins / 180) * 6 * math.pi)),
                400 - int(r_min * math.cos((mins / 180) * 6 * math.pi))
            )
        )

        # ===== VẼ THANH CHẠY =====
        if total != 0:
            pygame.draw.rect(
                screen, RED,
                (60, 530, 380 * int(total_secs / total), 30)
            )

        # Cập nhật màn hình
        pygame.display.flip()

    # Thoát pygame
    pygame.quit()

except:
    pass
