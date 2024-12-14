import time
import requests


def push_to_home_assistant(x1, x2, ha_url, ha_token):
    """
    Gửi dữ liệu x1, x2 lên Home Assistant thông qua REST API.

    :param x1: Giá trị đầu tiên cần gửi
    :param x2: Giá trị thứ hai cần gửi
    :param ha_url: URL của Home Assistant (ví dụ: http://localhost:8123)
    :param ha_token: Long-Lived Access Token của Home Assistant
    """
    # URL endpoint để cập nhật sensor giá trị
    endpoint = f"{ha_url}/api/states/sensor.custom_values"

    # Header để xác thực
    headers = {
        "Authorization": f"Bearer {ha_token}",
        "Content-Type": "application/json"
    }

    # Dữ liệu cần gửi
    data = {
        "state": "active",
        "attributes": {
            "x1": x1,
            "x2": x2,
            "unit_of_measurement": "custom"
        }
    }

    try:
        # Gửi request tới Home Assistant
        response = requests.post(endpoint, json=data, headers=headers)

        # Kiểm tra phản hồi
        if response.status_code in [200, 201]:
            print("Dữ liệu đã được gửi thành công!")
        else:
            print(f"Lỗi khi gửi dữ liệu: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Sử dụng hàm
if __name__ == "__main__":
    # Thay đổi các giá trị sau bằng thông tin thực tế
    x1 = 0
    x2 = 0
    ha_url = "http://192.168.239.242:8123"  # URL của Home Assistant
    ha_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2MjFkMzQxYzNmNWM0NGEyYjBlNGZkZjlkMGRhYjhiZSIsImlhdCI6MTczNDE3ODI4MSwiZXhwIjoyMDQ5NTM4MjgxfQ.BStoKwL_hLEs8UovGtR7CcSX15Fm5JmmTYoimI-"  # Token truy cập của bạn
    
    while True:
        x1 += 1
        x2 += 1
        push_to_home_assistant(x1, x2, ha_url, ha_token)
        time.sleep(1)
    

    
