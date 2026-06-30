import tkinter as tk

# ------------------------
# ตั้งค่าหน้าต่างหลัก
# ------------------------
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("420x620")
root.configure(bg="#1E1E1E")
root.resizable(False, False)

expression = ""

# ------------------------
# ฟังก์ชัน
# ------------------------
def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""

# ------------------------
# ช่องแสดงผล
# ------------------------
display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Segoe UI", 28),
    bd=0,
    bg="#2D2D2D",
    fg="white",
    justify="right",
    insertbackground="white"
)

display.pack(fill="both", padx=15, pady=20, ipady=20)

# ------------------------
# ปุ่ม
# ------------------------
buttons = [
    ["C", "(", ")", "⌫"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

frame = tk.Frame(root, bg="#1E1E1E")
frame.pack(expand=True, fill="both")

for r, row in enumerate(buttons):
    frame.rowconfigure(r, weight=1)

for c in range(4):
    frame.columnconfigure(c, weight=1)

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        bg = "#3C3F41"
        fg = "white"

        if text in ["+", "-", "*", "/", "="]:
            bg = "#FF9800"

        if text == "C":
            bg = "#D32F2F"

        if text == "⌫":
            bg = "#607D8B"

        btn = tk.Button(
            frame,
            text=text,
            font=("Segoe UI", 20, "bold"),
            bd=0,
            bg=bg,
            fg=fg,
            activebackground="#666666",
            activeforeground="white"
        )

        btn.grid(
            row=r,
            column=c,
            sticky="nsew",
            padx=5,
            pady=5,
            ipadx=10,
            ipady=20
        )

        if text == "=":
            btn.configure(command=calculate)
        elif text == "C":
            btn.configure(command=clear)
        elif text == "⌫":
            btn.configure(command=backspace)
        else:
            btn.configure(command=lambda t=text: press(t))

# ------------------------
# รองรับคีย์บอร์ด
# ------------------------
def key(event):
    global expression

    k = event.keysym

    if k == "Return":
        calculate()

    elif k == "BackSpace":
        backspace()

    elif k == "Escape":
        clear()

    else:
        allowed = "0123456789+-*/()."

        if event.char in allowed:
            press(event.char)

root.bind("<Key>", key)

root.mainloop()