from common.insertdanhmuc import insert_danhmuc

while True:
    ten = input("Nhập vào tên danh mục")
    mota = input("Nhập vào mô tả")
    insert_danhmuc(ten, mota)
    con = input("TIẾP TỤC y, THOÁT THÌ NHẤN KÝ TỰ BẤT KỲ")
    if con != "y":
        break