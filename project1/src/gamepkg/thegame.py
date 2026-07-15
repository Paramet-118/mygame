import tkinter as tk
import random

# -------------------------
# ตัวแปรหลัก
# -------------------------

root = None
canvas = None

WIDTH = 0
HEIGHT = 0

PLAYER_W = 70
PLAYER_H = 30

player = None
score_text = None

score = 0
balls = []

running = False
game_over = False


# -------------------------
# ควบคุมผู้เล่น
# -------------------------

def move_left(event):
    global running

    if running:
        x1, y1, x2, y2 = canvas.coords(player)

        if x1 > 0:
            canvas.move(player, -30, 0)


def move_right(event):
    global running

    if running:
        x1, y1, x2, y2 = canvas.coords(player)

        if x2 < WIDTH:
            canvas.move(player, 30, 0)


# -------------------------
# ออกจากเกม
# -------------------------

def exit_game(event=None):
    root.destroy()


# -------------------------
# เริ่มเล่น
# -------------------------

def start_game_loop():
    global running

    if not running and not game_over:
        running = True
        game_loop()


# -------------------------
# หยุดเกม
# -------------------------

def stop_game():
    global running

    running = False


# -------------------------
# รีสตาร์ทเกม
# -------------------------

def restart_game():

    global score
    global balls
    global running
    global game_over
    global player
    global score_text

    running = False
    game_over = False
    score = 0

    canvas.delete("all")
    balls.clear()

    player = canvas.create_rectangle(
        WIDTH//2-PLAYER_W//2,
        HEIGHT-80,
        WIDTH//2+PLAYER_W//2,
        HEIGHT-50,
        fill="cyan"
    )

    score_text = canvas.create_text(
        20,
        20,
        anchor="nw",
        text="Score : 0",
        fill="white",
        font=("Arial", 22, "bold")
    )


# -------------------------
# Game Loop
# -------------------------

def game_loop():

    global running
    global game_over
    global score

    if not running:
        return

    if random.randint(1, 8) == 1:

        x = random.randint(20, WIDTH-20)

        ball = canvas.create_oval(
            x-12,
            0,
            x+12,
            24,
            fill="red",
            outline=""
        )

        balls.append(ball)

    px1, py1, px2, py2 = canvas.coords(player)

    remove = []

    for ball in balls:

        canvas.move(ball, 0, 8)

        bx1, by1, bx2, by2 = canvas.coords(ball)

        if by2 >= py1 and bx2 >= px1 and bx1 <= px2:

            running = False
            game_over = True

            canvas.create_text(
                WIDTH//2,
                HEIGHT//2,
                text=f"GAME OVER\n\nScore : {score}",
                fill="yellow",
                font=("Arial", 40, "bold"),
                justify="center"
            )

            return

        if by1 > HEIGHT:
            remove.append(ball)
            score += 1

    for ball in remove:
        balls.remove(ball)
        canvas.delete(ball)

    canvas.itemconfig(
        score_text,
        text=f"Score : {score}"
    )

    root.after(25, game_loop)
# -------------------------
# สร้างปุ่ม
# -------------------------

def create_buttons():

    button_frame = tk.Frame(root, bg="black")

    button_frame.place(
        relx=0.5,
        rely=0.96,
        anchor="center"
    )

    tk.Button(
        button_frame,
        text="▶ START",
        font=("Arial", 14, "bold"),
        width=12,
        bg="green",
        fg="white",
        command=start_game_loop
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        button_frame,
        text="⏸ STOP",
        font=("Arial", 14, "bold"),
        width=12,
        bg="orange",
        command=stop_game
    ).grid(row=0, column=1, padx=10)

    tk.Button(
        button_frame,
        text="🔄 RESTART",
        font=("Arial", 14, "bold"),
        width=12,
        bg="dodgerblue",
        fg="white",
        command=restart_game
    ).grid(row=0, column=2, padx=10)

    tk.Button(
        button_frame,
        text="❌ EXIT",
        font=("Arial", 14, "bold"),
        width=12,
        bg="red",
        fg="white",
        command=root.destroy
    ).grid(row=0, column=3, padx=10)


# -------------------------
# เปิดเกม
# -------------------------

def start_game():

    global root
    global canvas
    global WIDTH
    global HEIGHT
    global player
    global score_text
    global score
    global running
    global game_over
    global balls

    score = 0
    running = False
    game_over = False
    balls.clear()

    root = tk.Tk()
    root.title("Dodge Game")
    root.attributes("-fullscreen", True)

    WIDTH = root.winfo_screenwidth()
    HEIGHT = root.winfo_screenheight()

    canvas = tk.Canvas(
        root,
        width=WIDTH,
        height=HEIGHT,
        bg="black",
        highlightthickness=0
    )

    canvas.pack(fill="both", expand=True)

    player = canvas.create_rectangle(
        WIDTH//2-PLAYER_W//2,
        HEIGHT-80,
        WIDTH//2+PLAYER_W//2,
        HEIGHT-50,
        fill="cyan"
    )

    score_text = canvas.create_text(
        20,
        20,
        anchor="nw",
        text="Score : 0",
        fill="white",
        font=("Arial", 22, "bold")
    )

    root.bind("<Left>", move_left)
    root.bind("<Right>", move_right)
    root.bind("<Escape>", exit_game)

    create_buttons()

    root.mainloop()


# -------------------------
# รันไฟล์นี้โดยตรง
# -------------------------

if __name__ == "__main__":
    start_game()