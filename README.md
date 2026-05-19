BÀI TẬP GIỮA KÌ CỜ CARO AI 

1.Thành viên thực hiện

  Phạm Trung Hiếu - 23021264

  Nguyễn Trung Hòa - 23021266

  Nguyễn Thái Hoàng - 23021270

2.Giới thiệu bài toán

  Bài tập xây dựng chương trình chơi cờ Caro (Gomoku) trên bàn cờ kích thước 16x16. Điểm nhấn của đồ án là việc áp dụng và so sánh hai thuật toán tìm kiếm thông    minh:

  Minimax: Thuật toán tìm kiếm cơ bản trên cây quyết định.

  Alpha-Beta Pruning: Bản cải tiến giúp cắt tỉa các nhánh không cần thiết, tối ưu hóa tốc độ xử lý của AI.

3.Cấu trúc thư mục 

   ├── source_code/          # Thư mục chứa toàn bộ mã nguồn của trò chơi
   │   ├── main.py           # File chạy chính (Quản lý luồng và giao diện Tkinter)
   │   ├── ai.py             # Cài đặt thuật toán Minimax và Alpha-Beta Pruning
   │   └── logic.py          # Xử lý luật chơi, trạng thái thắng/thua và sinh nước đi hợp lệ
   ├── requirements.txt      # Khai báo các thư viện cần thiết (tkinter)
   └── README.md

4.Hướng dẫn cài đặt và chạy

  Yêu cầu: Python 3.10 trở lên

  Cách chạy chương trình

   b1.Tải 3 file .py từ source_code trên GitHub về máy 

   b2.Mở cmd tại thư mục chứa các file

   b3.Chạy lệnh python source_code/main.py để khởi động 
   
5.Đánh giá sơ bộ qua kết quả thực nghiệm

  Tính chính xác: Alpha-Beta Pruning luôn chọn ra tọa độ nước đi và điểm số đánh giá trùng khớp 100% với Minimax thuần túy, chứng minh thuật toán cắt tỉa được      cài đặt hoàn toàn chính xác.

  Hiệu suất cải tiến: Khi thế trận càng phức tạp (nhiều quân trên bàn cờ), Alpha-Beta Pruning càng phát huy sức mạnh vượt trội. Tại trạng thái 5, Minimax mất tới   14.37 giây và phải duyệt gần 100,000 node, gây ra hiện tượng giật lag màn hình; trong khi đó, Alpha-Beta chỉ mất 0.54 giây và duyệt 3,393 node (nhanh hơn gấp     khoảng 26 lần), đảm bảo phản hồi tức thì cho trải nghiệm người chơi tốt nhất.


