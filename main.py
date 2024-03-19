import os
from tkinter import *
from tkinter import colorchooser
from PIL import ImageGrab
from tkinter import messagebox


def draw(event):
    x1, y1 = event.x - 2, event.y - 2
    x2, y2 = event.x + 2, event.y + 2
    cv.create_oval(x1, y1, x2, y2, fill=col, width=width, outline=col)


def clear():
    cv.delete("all")


def save():
    try:
        n = 1
        while fr"painting{n}.png" in os.listdir("Paints"):
            n += 1

        ImageGrab.grab((cv.winfo_rootx(),
                        cv.winfo_rooty(),
                        cv.winfo_rootx() + cv.winfo_width(),
                        cv.winfo_rooty() + cv.winfo_height(),
                        )).save(fr"Paints/painting{n}.png")

        messagebox.showinfo("Saved", f"Drawing saved in directory 'Paints' with name painting{n}")
    except BaseException:
        messagebox.showerror("Error", "Unknown directory")


def bg_color_choosing():
    global bg_col
    try:
        color = colorchooser.askcolor(title="Choose background color")
        bg_col = color[1]
        cv.config(bg=bg_col)
    except BaseException:
        pass


def brush_color_choosing():
    global col
    try:
        color = colorchooser.askcolor(title="Choose brush color")
        col = f"{color[1]}"
    except BaseException:
        pass


def width_scroll(event):
    global width
    if event.delta < 0 and width >= 0.5:
        width -= 0.5
    if event.delta > 0 and width <= 150:
        width += 0.5


bg_col = "white"
col = "black"
width = 5


root = Tk()
root.resizable(False, False)
root.title("Paint")


cv = Canvas(root, width=1280, height=720, bg=bg_col)


cv.bind("<B1-Motion>", draw)
cv.bind("<MouseWheel>", width_scroll)
cv.pack(expand=True, fill=BOTH)


main_menu = Menu(root)

color_menu = Menu(main_menu, tearoff=False)
bg_color_menu = Menu(color_menu, tearoff=False)
color_menu.add_cascade(label="Background color", menu=bg_color_menu)
bg_color_menu.add_command(label="Choose color", command=bg_color_choosing)
brush_color_menu = Menu(color_menu, tearoff=False)
color_menu.add_cascade(label="Brush color", menu=brush_color_menu)
brush_color_menu.add_command(label="Choose color", command=brush_color_choosing)

main_menu.add_command(label="Save", command=save)
main_menu.add_command(label="Clear all", command=clear)
main_menu.add_separator()
main_menu.add_cascade(label="Colors", menu=color_menu)

root.config(menu=main_menu)

root.mainloop()
