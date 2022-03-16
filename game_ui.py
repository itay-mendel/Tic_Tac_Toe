from tkinter import *


def convert_cor(event):
    if event.x < 600 and event.y < 600:
        return int(event.y / 200), int(event.x / 200)


root = Tk()
root.title("Tic Tac Toe")
root.geometry("600x800")


class Game:

    def __init__(self, master):
        self.canvas = Canvas(master, width=600, height=800)
        self.canvas.pack(fill="both", expand=True)
        bg_img = PhotoImage(file="images/board.png")
        self.canvas.create_image(0, 0, image=bg_img, anchor="nw")

    def insert(self, player, pos):
        cor_y = pos[0] * 200
        cor_x = pos[1] * 200
        if player == 1:
            img = PhotoImage(file="images/X.png")
            self.canvas.create_image(cor_x, cor_y, image=img, anchor="nw")
        else:
            img = PhotoImage(file="images/O.png")
            self.canvas.create_image(cor_x, cor_y, image=img, anchor="nw")

    def get_click(self):
        return self.canvas.bind('<Button-1>', convert_cor)


# - - - -- --- -- -- -- - - - - Check Code - -- -- - -- -- - -- --
g = Game(root)
g.insert(1, (0, 0))
while True:
    print(g.get_click())
    root.mainloop()



