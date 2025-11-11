from common.update_danhmuc import update_danhmuc

while True:
    madm = input("mã danh mục")
    ten = input("Nhập vào tên danh mục")
    mota = input("Nhập vào mô tả")
    update_danhmuc(madm,ten,mota)
    con = input("TIẾP TỤC y, THOÁT THÌ NHẤN KÝ TỰ BẤT KỲ")
    if con != "y":
        break