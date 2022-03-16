from tkinter import *
from brain import Board

XO = [' ', 'X', 'O']

root = Tk()
root.title("Tic Tac Toe")
root.geometry("600x800")

board = Board()
canvas = Canvas(root, width=600, height=800)
canvas.pack(fill="both", expand=True)
bg_img = PhotoImage(file="images/board.png")
canvas.create_image(0, 0, image=bg_img, anchor="nw")

game_status = Label(bd=4, relief="solid", font="Times 22 bold", bg="white", fg="black")
game_status.place(x=220, y=700)
game_status['text'] = f"{XO[board.turn]}'s turn"


def convert_cor(event):
    """
    The function converts coordinates on 'canvas' to position in 'board'
    :param event: tuple: (x_cor, y_cor). A user click on canvas.
    :return: tuple: (y_pos, x_pos)
    """
    return int(event.y / 200), int(event.x / 200)


def convert_pos(pos):
    """
    Thee function converts position in 'board' to coordinates on 'canvas'
    :param pos: tuple: (y_pos, x_pos). Position on board
    :return: tuple: (x_cor, y_cor)
    """
    return pos[0] * 200 + 80, pos[1] * 200 + 80


def valid_click(event):
    """
    Chacks if a click is within the board area
    :param event: click on canvas
    :return: True / False
    """
    return event.x < 600 and event.y < 600


def make_play(event):
    """

    :param event:
    :return:
    """
    if not board.is_tie() and board.winner == 0:
        if valid_click(event):
            pos = convert_cor(event)
            if board.is_valid_move(pos):
                cor = convert_pos(pos)
                Label(root, text=XO[board.turn], fg="black", bg="#edf9fc", font="Time 26 bold").place(x=cor[1], y=cor[0])
                board.inset(pos=pos)
                game_status['text'] = f"{XO[board.turn]}'s turn"
                board.game_status()
    else:
        if board.winner == 0:
            game_status['text'] = "It's a tie"
        else:
            game_status['text'] = f"'{XO[int(board.winner)]}' Won !"


canvas.bind('<Button-1>', make_play)
root.mainloop()




