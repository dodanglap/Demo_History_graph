# Sử dụng image Python cơ bản
FROM python:3.9-slim

# Cài đặt các gói cần thiết cho giao tiếp I2C và các thư viện hệ thống


# Sao chép toàn bộ mã Python và file requirements.txt vào container
COPY . /app

# Đặt thư mục làm việc
WORKDIR /app

# Cài đặt các thư viện Python được liệt kê trong requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Thiết lập lệnh mặc định khi chạy container
CMD ["python3", "run.py"]