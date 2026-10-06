import tkinter as tk
import random

oyna = tk.Tk()
oyna.title("🎮 Kvadratni ushla")
oyna.geometry("600x500")
oyna.resizable(False, False)

ochko = 0
vaqt = 30

canvas = tk.Canvas(oyna, width=600, height=400, bg="black")
canvas.pack()

matn = tk.Label(oyna, text="Ochko: 0 | Vaqt: 30",
                font=("Arial", 18))
matn.pack()

def kvadrat_yarat():
    canvas.delete("kvadrat")

    x = random.randint(30, 550)
    y = random.randint(30, 350)

    canvas.create_rectangle(
        x, y, x + 40, y + 40,
        fill="red",
        tags="kvadrat"
    )

def bosildi(event):
    global ochko

    ochko += 1
    matn.config(text=f"Ochko: {ochko} | Vaqt: {vaqt}")
    kvadrat_yarat()

def vaqtni_kamaytir():
    global vaqt

    if vaqt > 0:
        vaqt -= 1
        matn.config(text=f"Ochko: {ochko} | Vaqt: {vaqt}")
        oyna.after(1000, vaqtni_kamaytir)
    else:
        canvas.delete("all")
        canvas.create_text(
            300, 200,
            text=f"O'YIN TUGADI!\nOchko: {ochko}",
            fill="white",
            font=("Arial", 30)
        )

canvas.bind("<Button-1>", bosildi)

kvadrat_yarat()
vaqtni_kamaytir()

oyna.mainloop()
