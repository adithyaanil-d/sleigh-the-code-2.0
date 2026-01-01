import tkinter as tk

window = tk.Tk()
window.title("Sleigh the Code 2.0")
window.geometry("600x600")
canvas = tk.Canvas(window, width=600, height=600, bg="black")
canvas.pack()

def snowman(x, y):
    canvas.create_oval(x-90, y-90, x+90, y+90, fill="white", outline="")
    canvas.create_oval(x-65, y-200, x+65, y-80, fill="white", outline="")
    canvas.create_oval(x-45, y-280, x+45, y-200, fill="white", outline="")

    canvas.create_oval(x-18, y-245, x-6, y-233, fill="black")
    canvas.create_oval(x+6, y-245, x+18, y-233, fill="black")

    canvas.create_polygon(
        x, y-235,
        x+18, y-230,
        x, y-225,
        fill="orange"
    )

    canvas.create_arc(
        x-18, y-235,
        x+18, y-215,
        start=200, extent=140,
        style=tk.ARC, width=2
    )

    canvas.create_rectangle(x-70, y-205, x+70, y-185, fill="red", outline="")
    canvas.create_rectangle(x+20, y-185, x+45, y-130, fill="red", outline="")

    canvas.create_oval(x-5, y-160, x+5, y-150, fill="black")
    canvas.create_oval(x-5, y-125, x+5, y-115, fill="black")
import math

def real_snowflake(x, y, s):
    for angle in range(0, 360, 60):
        rad = math.radians(angle)

        canvas.create_line(
            x, y,
            x + s * math.cos(rad),
            y + s * math.sin(rad),
            fill="white", width=2
        )

        canvas.create_line(
            x + (s * 0.6) * math.cos(rad),
            y + (s * 0.6) * math.sin(rad),
            x + (s * 0.8) * math.cos(rad + math.radians(30)),
            y + (s * 0.8) * math.sin(rad + math.radians(30)),
            fill="white", width=1
        )

        canvas.create_line(
            x + (s * 0.6) * math.cos(rad),
            y + (s * 0.6) * math.sin(rad),
            x + (s * 0.8) * math.cos(rad - math.radians(30)),
            y + (s * 0.8) * math.sin(rad - math.radians(30)),
            fill="white", width=1
        )

snowman(300,450)

real_snowflake(80,80,22)
real_snowflake(200,120,18)
real_snowflake(500,90,24)
real_snowflake(420,160,20)
real_snowflake(120,260,18)
real_snowflake(520,300,22)
real_snowflake(90,450,20)
real_snowflake(480,470,24)

window.mainloop()

