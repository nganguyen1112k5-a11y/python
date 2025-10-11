# Tạo danh mục (dictionary)
menu = {
    "python": "Ngôn ngữ lập trình mạnh mẽ, dễ học, dùng cho AI và khoa học dữ liệu.",
    "matlab": "Phần mềm dùng cho tính toán kỹ thuật, xử lý tín hiệu và mô phỏng.",
    "html": "Ngôn ngữ đánh dấu dùng để xây dựng cấu trúc trang web.",
    "css": "Ngôn ngữ dùng để định dạng và trang trí cho trang web.",
    "java": "Ngôn ngữ lập trình hướng đối tượng, chạy trên nhiều nền tảng khác nhau."
}

print("=== TRA CỨU DANH MỤC ===")
print("Nhập từ khóa (hoặc nhiều từ khóa cách nhau bằng khoảng trắng).")
print("Gõ 'exit' hoặc 'thoat' để kết thúc chương trình.\n")

# Vòng lặp vô hạn để nhập liên tục
while True:
    user_input = input("🔎 Nhập từ khóa: ").lower().strip()

    # Lệnh thoát
    if user_input in ["exit", "thoat"]:
        print("👋 Đã thoát chương trình. Tạm biệt!")
        break

    # Tách từ khóa (cho phép nhập nhiều từ trong cùng dòng)
    keys = user_input.split()

    # Nếu người dùng không nhập gì
    if not keys:
        print("⚠️ Bạn chưa nhập từ khóa nào. Vui lòng thử lại!\n")
        continue

    # Duyệt từng từ khóa
    for key in keys:
        if key in menu:
            print(f"✅ {key.capitalize()}: {menu[key]}")
        else:
            print(f"❌ Không có mục '{key}' trong danh mục.")
    print()  # Xuống dòng cho đẹp
