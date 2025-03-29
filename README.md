# 🚜 Life of a Chill Guy - Game Nông Trại 2D
![image](https://github.com/user-attachments/assets/f24efb4f-1554-4581-a7f1-d3a65d776504)

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
   git clone https://github.com/WuKong0601/FarmGame.git
   cd FarmGame
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

## 🌳 Cấu trúc dự án

```bash
FarmingGame/
│
├── 📁 .git/                # Thư mục Git chứa thông tin version control
├── 📁 .idea/              # Cấu hình dự án cho JetBrains IDE (PyCharm)
├── 📁 .venv/              # Môi trường ảo Python chứa các dependencies
│
├── 🔊 audio/              # Thư mục chứa tất cả file âm thanh
│   ├── 🎵 success.wav     # Âm thanh khi hoàn thành nhiệm vụ
│   └── 🎵 music.mp3       # Nhạc nền game
│
├── 💻 code/               # Thư mục mã nguồn chính
│   ├── 🚀 main.py         # File khởi chạy chính của game
│   ├── 🐄 animals.py      # Logic vật nuôi (gà, bò, cá)
│   ├── 🗺 level.py        # Quản lý bản đồ và level
│   ├── 🖥 overlay.py      # Giao diện người dùng (UI)
│   ├── 🧍 player.py       # Điều khiển nhân vật chính
│   ├── ⚙️ settings.py     # Các hằng số cấu hình game
│   ├── ☁️ sky.py          # Hệ thống thời tiết (mưa, ngày/đêm)
│   ├── 🌱 soil.py         # Hệ thống trồng trọt và đất đai
│   ├── 🖼 sprites.py      # Lớp cơ sở cho các đối tượng đồ họa
│   ├── 🛠 support.py      # Các hàm tiện ích hỗ trợ
│   ├── ⏱ timer.py        # Hệ thống hẹn giờ trong game
│   └── ✨ transition.py   # Hiệu ứng chuyển cảnh
│
├── 📊 data/               # Dữ liệu bản đồ game
│   ├── 📁 Tilesets/       # Bộ tile đồ họa cho bản đồ
│   │   ├── tileset1.png
│   │   └── tileset2.png
│   └── 🗺 map.tmx         # File bản đồ chính (được tạo bằng Tiled)
│
├── 🔠 font/               # Thư mục font chữ
│   └── 🅻 LycheeSoda.ttf  # Font chữ chính của game
│
└── 🎨 graphics/           # Tất cả assets đồ họa
    ├── 🐓 animals/        # Sprite vật nuôi
    │   ├── 🐔 chicken/    # Sprite gà
    │   ├── 🐄 cow/        # Sprite bò
    │   └── 🐟 fish/       # Sprite cá
    │
    ├── 🧍 character/      # Nhân vật chính
    │   ├── up.png         # Animation đi lên
    │   ├── down.png       # Animation đi xuống
    │   └── ...            # Các hướng khác
    │
    ├── 🌽 fruit/          # Cây trồng và hoa quả
    │   ├── corn/          # Sprite ngô
    │   └── tomato/        # Sprite cà chua
    │
    ├── 🌍 world/          # Bối cảnh nền
    │   ├── ground.png     # Nền đất
    │   └── water.png      # Nền nước
    │
    ├── 💧 water/          # Hiệu ứng nước
    │   ├── frame1.png
    │   └── frame2.png
    │
    └── ...                # Các thư mục đồ họa khác

🖼️ Ảnh Chụp Màn Gian
Gameplay 1: Cuốc đất
![image](https://github.com/user-attachments/assets/8e094085-ea9b-429f-aa6b-3c2d09f6d2a6)

Gameplay 2: Trồng cây
![image](https://github.com/user-attachments/assets/5b4afe62-66e2-4046-83eb-83776a4a855b)

Gameplay 3
![image](https://github.com/user-attachments/assets/2145c6ce-46fc-4634-813a-4a2e2af7e3f3)

Gameplay 4: Chặt cây, thu gỗ và táo
![image](https://github.com/user-attachments/assets/bf5badc0-0b43-4337-9a8b-7b46dc2bf8cf)

Gameplay 5: Tưới cây
![image](https://github.com/user-attachments/assets/d029ffe9-6ea7-4979-89d7-71453280e311)

Gameplay 6: Phát triển cây theo thời gian
![image](https://github.com/user-attachments/assets/a9727bc8-fe9e-40a4-9165-6bdf424f2edc)

Gameplay 7: Thu hoạch
![image](https://github.com/user-attachments/assets/bccee0b9-b406-4a2d-9d01-b56cfb9fa34c)

Gameplay 8: Giao dịch
![image](https://github.com/user-attachments/assets/9677e559-437d-47a9-beb0-840fb2625ca5)

![image](https://github.com/user-attachments/assets/d521636f-c672-428f-827e-3eb668675250)

Gameplay 9: Chăn nuôi
![image](https://github.com/user-attachments/assets/30ab4d81-a949-4d11-9289-77d6f37d3359)

![image](https://github.com/user-attachments/assets/d489522b-e091-4fa6-b426-133bd2575b51)

## 📌 Tiến Độ Phát Triển

| Tính Năng | Trạng Thái |
|-----------|------------|
| Trồng trọt | ✅ Hoàn thành |
| Chăn nuôi | ✅ Hoàn thành |
| Hệ thống mùa | ⏳ Đang phát triển |
