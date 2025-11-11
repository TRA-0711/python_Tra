import mysql.connector
from mysql.connector import Error

def connect_mysql():
    try:
        # Thông tin kết nối CSDL
        connection = mysql.connector.connect(
            host='localhost',      # Địa chỉ server (thường là localhost)
            user='root',           # Tên đăng nhập MySQL
            password='',     # Mật khẩu MySQL
            database='qlthuocankhang1'  # Tên database muốn kết nối
        )

        # Kiểm tra kết nối
        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi kết nối MySQL:", e)
        return None
