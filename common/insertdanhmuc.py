from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(ten_danh_muc, mo_ta):
    global cursor
    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối tới MySQL.")
        return

    try:
        cursor = connection.cursor()
        query = "INSERT INTO danhmuc (ten_danh_muc, mo_ta) VALUES (%s, %s)"
        values = (ten_danh_muc, mo_ta)
        cursor.execute(query, values)
        connection.commit()
        print(f"✅ Đã thêm danh mục '{ten_danh_muc}' thành công!")

    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối MySQL.")

