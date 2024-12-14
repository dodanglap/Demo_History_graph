# Sử dụng hình ảnh Python chính thức với phiên bản slim nhẹ
FROM python:3.9-slim

# Cài đặt các gói cần thiết cho giao tiếp I2C và các thư viện hệ thống
RUN apt-get update && apt-get install -y \
    libffi-dev libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements.txt vào container
COPY requirements.txt ./

# Cài đặt các thư viện Python được liệt kê trong requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Thiết lập lệnh mặc định khi chạy container
CMD ["python3", "run.py"]
