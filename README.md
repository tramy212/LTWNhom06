👨‍💼 HUMAN RESOURCE MANAGEMENT – WEB APP FOR EMPLOYEE ADMINISTRATION


Ứng dụng Human Resource Management là một hệ thống web giúp các doanh nghiệp quản lý thông tin nhân viên một cách hiệu quả. Ứng dụng hỗ trợ các chức năng thiết yếu như quản lý hồ sơ nhân viên, hợp đồng lao động, chấm công và tính lương hàng tháng.


🚀 CÔNG NGHỆ SỬ DỤNG


🔧 BACKEND
Python (Django): Framework chính để xây dựng ứng dụng theo mô hình MVC, hỗ trợ routing, ORM và các công cụ quản lý.

Django ORM: Quản lý cơ sở dữ liệu thông qua các mô hình Python, giúp đơn giản hóa việc thao tác với dữ liệu.

SQLite: Cơ sở dữ liệu nhẹ, lý tưởng cho môi trường phát triển và thử nghiệm.

ReportLab / WeasyPrint: Dùng để tạo và xuất báo cáo lương dưới dạng PDF.

Authentication Middleware: Xác thực và phân quyền người dùng khi sử dụng hệ thống.



🎨 FRONTEND
HTML / CSS / JavaScript: Tạo giao diện người dùng và xử lý các tương tác cơ bản.

Bootstrap: Framework giao diện phổ biến giúp tạo thiết kế responsive và thân thiện với người dùng.

Django Template Engine: Dùng để hiển thị dữ liệu động từ backend lên giao diện.

✅ TÍNH NĂNG CHÍNH
Quản lý thông tin nhân viên: Thêm, sửa, xem và vô hiệu hóa hồ sơ nhân viên.

Quản lý hợp đồng lao động: Theo dõi thời hạn hợp đồng, loại hợp đồng và tình trạng hiệu lực.

Chấm công:

Ghi nhận giờ vào – giờ ra hằng ngày.

Xem báo cáo chấm công theo tháng của từng nhân viên.

Tính lương:

Tự động tính lương theo số ngày làm việc.

Xuất báo cáo lương theo tháng dưới dạng PDF.

Phân quyền người dùng: Xác thực tài khoản và phân quyền truy cập chức năng hệ thống.

📷 GIAO DIỆN

Trang chủ:
![image](https://github.com/user-attachments/assets/9ad725b1-b288-4050-a804-5b59a0e900df)

Quản lý Thông tin nhân sự:
![image](https://github.com/user-attachments/assets/160a7e9a-bbe0-4ffb-ba60-f89288d6371d)

Quản lý Chấm công
![image](https://github.com/user-attachments/assets/72502b39-ba87-467f-a439-eae6a7116447)

Quán lý Tiền lương
![image](https://github.com/user-attachments/assets/2410fcd3-bbfd-4135-a78a-fb9ad3c6ef9d)

⚙️ HƯỚNG DẪN CÀI ĐẶT
Clone project về máy:
git clone (https://github.com/tramy212/LTWNhom06).git

Cấu hình cơ sở dữ liệu:
Dùng SQLite mặc định hoặc thay đổi trong settings.py nếu muốn dùng cơ sở dữ liệu khác.

Chạy migrations và khởi tạo dữ liệu:
python manage.py makemigrations  
python manage.py migrate

Chạy ứng dụng:
python manage.py runserver

Truy cập hệ thống tại:
(http://127.0.0.1:8000/)



