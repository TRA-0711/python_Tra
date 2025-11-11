
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


def get_all_danhmuc():
    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối tới MySQL.")
        return

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM danhmuc"
        cursor.execute(query)
        results = cursor.fetchall()

        if len(results) == 0:
            print("⚠️ Chưa có danh mục nào trong cơ sở dữ liệu.")
        else:
            print("📋 Danh sách danh mục:")
            print("-" * 50)
            for row in results:
                print(f"ID: {row[0]} | Tên: {row[1]} | Mô tả: {row[2]} | Trạng thái: {row[3]}")

        return results

    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối MySQL.")
