import tkinter as tk

def makeBoardCanvas():
    board = [[0 for _ in range(20)] for _ in range(20)] # make 20x20 array

    for i in range(20):
        for j in range(20):
            # append canvas to the array
            board[i][j] = tk.Canvas(app, width=40,height=40,border=0,bg="white",cursor="hand2")

    return board

def setBoardPosition(board):
    for i in range(20):
        for j in range(20):
            board[i][j].grid(column=j,row=i)

    return board
    

app = tk.Tk() # create instance
app.geometry('840x840') # set window size
app.minsize(840, 840)
app.maxsize(840, 840)
app.title('Mega Clever') # set title of the window

board = setBoardPosition(makeBoardCanvas()) # initialize 20x20 board and then

app.mainloop()