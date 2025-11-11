from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


def delete_danhmuc(id_danh_muc):
    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối tới MySQL.")
        return

    try:
        cursor = connection.cursor()
        query = "DELETE FROM danhmuc WHERE id = %s"
        cursor.execute(query, (id_danh_muc,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Đã xóa danh mục có ID = {id_danh_muc} thành công!")
        else:
            print(f"❌ Không tìm thấy danh mục có ID = {id_danh_muc}.")

    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối MySQL.")