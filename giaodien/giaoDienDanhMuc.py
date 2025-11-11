import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


# ======== LỚP GIAO DIỆN =========
class DanhMucApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Danh Mục Sản Phẩm")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        # --- Khung nhập thông tin ---
        frame_input = tk.LabelFrame(root, text="Thông tin danh mục", padx=10, pady=10)
        frame_input.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, sticky="w")
        self.ten_var = tk.StringVar()
        tk.Entry(frame_input, textvariable=self.ten_var, width=40).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, sticky="w")
        self.mota_var = tk.StringVar()
        tk.Entry(frame_input, textvariable=self.mota_var, width=40).grid(row=1, column=1, padx=10, pady=5)

        # --- Nút chức năng ---
        frame_btn = tk.Frame(root)
        frame_btn.pack(fill="x", padx=10, pady=5)

        tk.Button(frame_btn, text="Thêm", width=12, bg="#28a745", fg="white", command=self.add_danhmuc).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Sửa", width=12, bg="#007bff", fg="white", command=self.update_danhmuc).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Xóa", width=12, bg="#dc3545", fg="white", command=self.delete_danhmuc).grid(row=0, column=2, padx=5)
        tk.Button(frame_btn, text="Làm mới", width=12, command=self.clear_input).grid(row=0, column=3, padx=5)

        # --- Bảng hiển thị danh mục ---
        frame_table = tk.LabelFrame(root, text="Danh sách danh mục")
        frame_table.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("id", "ten_danh_muc", "mo_ta", "trang_thai")
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("ten_danh_muc", text="Tên danh mục")
        self.tree.heading("mo_ta", text="Mô tả")
        self.tree.heading("trang_thai", text="Trạng thái")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("ten_danh_muc", width=200)
        self.tree.column("mo_ta", width=300)
        self.tree.column("trang_thai", width=80, anchor="center")

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<ButtonRelease-1>", self.on_select)

        # Hiển thị dữ liệu ban đầu
        self.show_danhmuc()

    # ======= Các chức năng ========
    def add_danhmuc(self):
        name = self.ten_var.get().strip()
        desc = self.mota_var.get().strip()

        if not name:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên danh mục.")
            return

        conn = connect_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO danhmuc (ten_danh_muc, mo_ta) VALUES (%s, %s)"
                cursor.execute(query, (name, desc))
                conn.commit()
                messagebox.showinfo("Thành công", "Đã thêm danh mục mới!")
                self.show_danhmuc()
                self.clear_input()
            except Error as e:
                messagebox.showerror("Lỗi", f"Lỗi khi thêm: {e}")
            finally:
                conn.close()

    def update_danhmuc(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục để sửa.")
            return

        data = self.tree.item(selected)["values"]
        id_dm = data[0]
        name = self.ten_var.get().strip()
        desc = self.mota_var.get().strip()

        conn = connect_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE danhmuc SET ten_danh_muc=%s, mo_ta=%s WHERE id=%s"
                cursor.execute(query, (name, desc, id_dm))
                conn.commit()
                messagebox.showinfo("Thành công", "Cập nhật danh mục thành công!")
                self.show_danhmuc()
                self.clear_input()
            except Error as e:
                messagebox.showerror("Lỗi", f"Lỗi khi cập nhật: {e}")
            finally:
                conn.close()

    def delete_danhmuc(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục để xóa.")
            return

        data = self.tree.item(selected)["values"]
        id_dm = data[0]
        confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa danh mục ID = {id_dm}?")

        if confirm:
            conn = connect_mysql()
            if conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM danhmuc WHERE id=%s", (id_dm,))
                    conn.commit()
                    messagebox.showinfo("Thành công", "Đã xóa danh mục!")
                    self.show_danhmuc()
                    self.clear_input()
                except Error as e:
                    messagebox.showerror("Lỗi", f"Lỗi khi xóa: {e}")
                finally:
                    conn.close()

    def show_danhmuc(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        conn = connect_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM danhmuc")
                rows = cursor.fetchall()
                for row in rows:
                    self.tree.insert("", tk.END, values=row)
            except Error as e:
                messagebox.showerror("Lỗi", f"Lỗi khi hiển thị: {e}")
            finally:
                conn.close()

    def clear_input(self):
        self.ten_var.set("")
        self.mota_var.set("")
        self.tree.selection_remove(self.tree.selection())

    def on_select(self, event):
        selected = self.tree.focus()
        if selected:
            data = self.tree.item(selected)["values"]
            self.ten_var.set(data[1])
            self.mota_var.set(data[2])


# ======== CHẠY ỨNG DỤNG =========
if __name__ == "__main__":
    root = tk.Tk()
    app = DanhMucApp(root)
    root.mainloop()