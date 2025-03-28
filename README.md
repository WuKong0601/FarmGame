# 🚜 Life of a Chill Guy - Game Nông Trại 2D

![image](https://github.com/user-attachments/assets/ec00b055-05b3-403f-ba84-8bf2b25bfcd0)


Một game nông trại 2D được phát triển bằng Pygame với đầy đủ tính năng trồng trọt, chăn nuôi và khám phá.

## 🎮 Tính Năng Chính

### 🌱 Hệ Thống Trồng Trọt
- Cuốc đất, gieo hạt và tưới nước
- 2 loại cây trồng: ngô và cà chua
- Cây phát triển theo thời gian và có thể thu hoạch

### 🐄 Hệ Thống Chăn Nuôi
- Mua bán vật nuôi: gà, bò
- Dắt vật nuôi bằng phím `W`
- Vật nuôi di chuyển tự do với AI cơ bản
- Hệ thống cá với hiệu ứng bong bóng

### 🏡 Thế Giới Mở
- Bản đồ tile-based được thiết kế bằng Tiled
- Nhà cửa, cây cối và các vật cản
- Hệ thống thời gian (ngày/đêm) và thời tiết (mưa)

### 🛒 Hệ Thống Kinh Tế
- Cửa hàng mua bán vật phẩm
- Thu hoạch và bán nông sản
- Quản lý inventory

## 🛠 Cài Đặt

1. **Yêu cầu hệ thống**:
   - Python 3.8+
   - Pygame 2.0+

2. **Cài đặt**:
   ```bash
   git clone https://github.com/username/life-of-a-chill-guy.git
   cd life-of-a-chill-guy
   pip install -r requirements.txt

3. **Chạy game**:
  python main.py

⌨️ Điều Khiển
Phím	Chức Năng
↑↓←→	Di chuyển
Space	Sử dụng công cụ
Q	Đổi công cụ
E	Đổi hạt giống
W	Dắt thả vật nuôi
Enter	Tương tác (ngủ khi "enter với giường, mua bán khi "enter" với trader)
ESC	Mở/đóng menu

📂 Cấu Trúc Dự Án
life-of-a-chill-guy/
├── data/                # File bản đồ Tiled
├── graphics/            # Assets đồ họa
│   ├── animals/         # Sprite vật nuôi
│   ├── character/       # Nhân vật chính
│   ├── soil/            # Hiệu ứng đất
│   └── ...              # Các thư mục khác
├── audio/               # Âm thanh
├── main.py              # Khởi chạy game
├── settings.py          # Cấu hình game
├── level.py             # Quản lý màn chơi
├── player.py            # Người chơi
├── animals.py           # Hệ thống vật nuôi
└── ...                  # Các file khác

🖼️ Ảnh Chụp Màn Gian


## 📌 Tiến Độ Phát Triển

| Tính Năng | Trạng Thái |
|-----------|------------|
| Trồng trọt | ✅ Hoàn thành |
| Chăn nuôi | ✅ Hoàn thành |
| Hệ thống mùa | ⏳ Đang phát triển |
