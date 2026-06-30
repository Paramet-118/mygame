import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณ BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # แปลง cm เป็น m

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            status = "น้ำหนักน้อย"
        elif bmi < 25:
            status = "น้ำหนักปกติ"
        elif bmi < 30:
            status = "น้ำหนักเกิน"
        else:
            status = "โรคอ้วน"

        result_label.config(
            text=f"BMI = {bmi:.2f}\nสถานะ : {status}",
            fg="#00AA00"
        )

    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกตัวเลขให้ถูกต้อง")

# สร้างหน้าต่าง
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")
root.configure(bg="#E8F5E9")

# หัวข้อ
title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold"),
    bg="#E8F5E9",
    fg="#2E7D32"
)
title.pack(pady=15)

# น้ำหนัก
tk.Label(
    root,
    text="น้ำหนัก (kg)",
    font=("Arial", 12),
    bg="#E8F5E9"
).pack()

weight_entry = tk.Entry(font=("Arial", 12), justify="center")
weight_entry.pack(pady=5)

# ส่วนสูง
tk.Label(
    root,
    text="ส่วนสูง (cm)",
    font=("Arial", 12),
    bg="#E8F5E9"
).pack()

height_entry = tk.Entry(font=("Arial", 12), justify="center")
height_entry.pack(pady=5)

# ปุ่มคำนวณ
calc_btn = tk.Button(
    root,
    text="คำนวณ BMI",
    font=("Arial", 13, "bold"),
    bg="#4CAF50",
    fg="white",
    command=calculate_bmi
)
calc_btn.pack(pady=20)

# แสดงผล
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#E8F5E9"
)
result_label.pack()

root.mainloop()