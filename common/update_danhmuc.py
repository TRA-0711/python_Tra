from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def update_danhmuc(id_danh_muc, ten_moi, mo_ta_moi):
    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối tới MySQL.")
        return

    try:
        cursor = connection.cursor()
        query = """
            UPDATE danhmuc 
            SET ten_danh_muc = %s, mo_ta = %s
            WHERE id = %s
        """
        values = (ten_moi, mo_ta_moi, id_danh_muc)
        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục có ID = {id_danh_muc} thành công!")
        else:
            print(f"❌ Không tìm thấy danh mục có ID = {id_danh_muc}.")

    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối MySQL.")
